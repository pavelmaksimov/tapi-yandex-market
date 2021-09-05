import logging
import datetime as dt
import logging
import time
from typing import Union, Optional, List

import orjson
from requests import Response
from tapi2 import TapiAdapter, generate_wrapper_from_adapter, JSONAdapterMixin
from tapi2.exceptions import (
    ResponseProcessException,
    ClientError,
    TapiException,
    NotFound404Error,
)

from tapi_yandex_market import exceptions
from tapi_yandex_market.resource_mapping import RESOURCE_MAPPING_V2

logger = logging.getLogger(__name__)


def encoder(obj):
    if isinstance(obj, (dt.datetime, dt.date)):
        return obj.strftime("%d-%m-%Y")
    raise obj


class YandexMarketClientAdapter(JSONAdapterMixin, TapiAdapter):
    resource_mapping = RESOURCE_MAPPING_V2

    def get_api_root(self, api_params: dict, resource_name: str) -> str:
        return "https://api.partner.market.yandex.ru/"

    def get_request_kwargs(self, api_params: dict, *args, **kwargs) -> dict:
        """Обогащение запроса, параметрами"""
        headers = {}
        headers["Accept"] = "application/json"
        token = api_params["oauth_token"]
        oauth_client_id = api_params["oauth_client_id"]
        if token:
            headers[
                "Authorization"
            ] = f'OAuth oauth_token="{token}", oauth_client_id="{oauth_client_id}"'

        params = kwargs.get("params", {})
        if isinstance(params.get("fromDate"), (dt.date, dt.datetime)):
            params["fromDate"] = params["fromDate"].strftime("%d-%m-%Y")
        if isinstance(params.get("toDate"), (dt.date, dt.datetime)):
            params["toDate"] = params["toDate"].strftime("%d-%m-%Y")

        kwargs["params"] = params
        kwargs["headers"] = headers

        return super().get_request_kwargs(api_params, *args, **kwargs)

    def get_error_message(
        self, data: Union[None, dict], response: Response = None
    ) -> dict:
        rate_limit = response.headers.get("X-RateLimit-Resource-Limit")
        rate_limit_until = response.headers.get("X-RateLimit-Resource-Until")
        rate_limit_remaining = response.headers.get("X-RateLimit-Resource-Remaining")

        if data is None:
            data = {"error_text": response.content.decode()}

        data.update(
            {
                "rate_limit": rate_limit,
                "rate_limit_until": rate_limit_until,
                "rate_limit_remaining": rate_limit_remaining,
            }
        )

        return data

    def format_data_to_request(self, data) -> Optional[bytes]:
        if data:
            return orjson.dumps(data, default=encoder)

    def response_to_native(self, response: Response) -> Union[dict, str]:
        if response.content.strip():
            try:
                return orjson.loads(response.content.decode())
            except ValueError:
                return response.text

    def process_response(
        self, response: Response, request_kwargs: dict, **kwargs
    ) -> dict:
        data = self.response_to_native(response)

        if isinstance(data, dict) and data.get("error"):
            raise ResponseProcessException(ClientError, data)
        elif response.status_code == 200:
            return data
        elif response.status_code == 206:
            logger.warning(
                "Partial Content (https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html)"
            )
            return data
        elif response.status_code == 500:
            raise exceptions.InternalServerError(response, **kwargs)
        elif response.status_code == 503:
            raise exceptions.ServiceUnavailableError(response, **kwargs)
        elif response.status_code == 405:
            raise exceptions.MethodNotAllowedError(
                response,
                f"This resource does not support the HTTP method '{response.request.method}'",
                **kwargs,
            )
        elif response.status_code == 404 and not (
            isinstance(data, dict) and data.get("error")
        ):
            raise ResponseProcessException(NotFound404Error, None)
        else:
            raise exceptions.ApiError(response, data, **kwargs)

    def error_handling(
        self,
        tapi_exception: TapiException,
        message: dict,
        repeat_number: int,
        response: Response,
        request_kwargs: dict,
        api_params: dict,
        **kwargs,
    ) -> None:
        if "error_text" in message:
            raise exceptions.ApiError(response, message["error_text"], **kwargs)
        error_data = message.get("error", {})
        error_code = error_data.get("code", response.status_code)

        if error_code in exceptions.exceptions_map:
            raise exceptions.exceptions_map[error_code](response, message, **kwargs)
        raise exceptions.ClientError(response, message, **kwargs)

    def retry_request(
        self,
        tapi_exception: TapiException,
        error_message: dict,
        repeat_number: int,
        response: Response,
        request_kwargs: dict,
        api_params: dict,
        **kwargs,
    ) -> bool:
        status_code = response.status_code
        error_data = error_message.get("error", {})
        error_code = int(error_data.get("code", 0))

        if 420 in (status_code, error_code):
            rate_limit = response.headers.get("X-RateLimit-Resource-Limit")
            rate_limit_until = response.headers.get("X-RateLimit-Resource-Until")
            rate_limit_remaining = response.headers.get(
                "X-RateLimit-Resource-Remaining"
            )
            logger.warning(
                f"LimitError: rate limit={rate_limit}, until={rate_limit_until}, remaining={rate_limit_remaining}"
            )

            if api_params.get("retry_if_exceeded_requests_limit", True):
                logger.info("Re-request after {} seconds".format(3))
                time.sleep(3)

                return True

        return False

    def get_iterator_pages(
        self, response_data, response, request_kwargs, api_params, **kwargs
    ):
        if "offersStats" in response_data:
            return response_data["offersStats"].get("offerStats", [])

    def get_iterator_next_request_kwargs(
        self, response_data, response, request_kwargs, api_params, **kwargs
    ) -> Optional[dict]:
        if "offersStats" in response_data:
            total = response_data["offersStats"]["totalOffersCount"]
            from_offer = response_data["offersStats"]["fromOffer"]
            to_offer = response_data["offersStats"]["toOffer"]
            limit = to_offer - from_offer + 1
            page_num = int(to_offer / limit)
            if to_offer < total:
                next_page_num = page_num + 1
                request_kwargs["params"]["page"] = next_page_num
                return request_kwargs

    def _get_result_dict_keys(self, kwargs: dict) -> Optional[List[str]]:
        resource_data = self.resource_mapping[kwargs["resource_name"]]
        result_dict_keys = resource_data.get("key", [])

        if result_dict_keys is None:
            logger.warning(
                "Result extract is not implemented for method '{}'".format(
                    kwargs["resource_name"]
                )
            )
        elif not isinstance(result_dict_keys, list):
            result_dict_keys = [result_dict_keys]

        return result_dict_keys

    def extract(self, data: dict, **kwargs) -> Union[list, dict]:
        result_dict_keys = self._get_result_dict_keys(kwargs)
        if result_dict_keys is not None:
            for key in result_dict_keys:
                data = data[key]

        return data


YandexMarket = generate_wrapper_from_adapter(YandexMarketClientAdapter)
