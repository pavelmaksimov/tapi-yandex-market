from typing import Dict, Union

from requests import Response
from tapi2.tapi import TapiClient

"""
Error messages
https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html
"""


class ApiError(Exception):
    def __init__(
        self,
        response: Response,
        data: Union[str, dict],
        client: TapiClient,
        *args,
        **kwargs,
    ):
        self.response = response
        self.data = data
        self.client = client

    def __str__(self):
        return "{} {} {}\nHEADERS = {}\nURL = {}".format(
            self.response.status_code,
            self.response.reason,
            self.data or self.response.text,
            self.response.headers,
            self.response.url,
        )


class ClientError(ApiError):
    def __init__(
        self,
        response: Response,
        message: Dict[str, dict],
        client: TapiClient,
        *args,
        **kwargs,
    ):
        self.error = message["error"]
        self.errors = message.get("errors")
        self.error_code = message["error"]["code"]
        self.error_message = message["error"]["message"]
        super().__init__(response, message, client, *args, **kwargs)

    def __str__(self):
        return f"error_code={self.error_code}, error_message={self.error_message}, errors={self.errors}"


class MethodNotAllowedError(ApiError):
    """Documentation https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html"""

    ...


class InternalServerError(ApiError):
    """Documentation https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html"""

    ...


class ServiceUnavailableError(ApiError):
    """Documentation https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html"""

    ...


class UnauthorizedError(ClientError):
    """Documentation https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html"""

    ...


class ForbiddenError(ClientError):
    """Documentation https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html"""

    ...


class NotEnoughUnitsError(ClientError):
    """Documentation https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html"""

    ...


class UnsupportedMediaTypeError(ClientError):
    """Documentation https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html"""

    ...


class NotFoundError(ClientError):
    """Documentation https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html"""

    ...


class BadRequestError(ClientError):
    """Documentation https://yandex.ru/dev/market/partner/doc/dg/concepts/error-codes.html"""

    ...


class RequestsLimitError(ClientError):
    """Documentation: https://yandex.ru/dev/market/partner/doc/dg/concepts/limits.html"""

    def __init__(
        self,
        response: Response,
        message: Dict[str, dict],
        client: TapiClient,
        *args,
        **kwargs,
    ):
        # Contains the numeric value of the constraint.
        self.rate_limit = response.headers.get("X-RateLimit-Resource-Limit")
        # Contains the date until which the restriction is in effect.
        self.rate_limit_until = response.headers.get("X-RateLimit-Resource-Until")
        # Contains a numeric value of the volume of requests to this resource, remaining before the limit was exceeded.
        self.rate_limit_remaining = response.headers.get(
            "X-RateLimit-Resource-Remaining"
        )
        super().__init__(response, message, client, *args, **kwargs)

    def __str__(self):
        return (
            f"limit={self.rate_limit}, until={self.rate_limit_until}, remaining={self.rate_limit_remaining}, "
            + str(self)
        )


exceptions_map = {
    400: BadRequestError,
    401: UnauthorizedError,
    403: ForbiddenError,
    404: NotFoundError,
    405: MethodNotAllowedError,
    415: UnsupportedMediaTypeError,
    420: RequestsLimitError,
    500: InternalServerError,
    503: ServiceUnavailableError,
}
