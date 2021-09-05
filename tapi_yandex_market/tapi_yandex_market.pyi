from logging import Logger
from typing import List, Iterator, Union

import requests
from requests import Response

logger: Logger

__author__: str
__email__: str
__version__: str

class BaseMethodsTapiResponse:
    @property
    def data(self) -> dict: ...
    @property
    def request_kwargs(self) -> dict: ...
    @property
    def response(self) -> Response: ...
    @property
    def status_code(self) -> int: ...
    def __getitem__(self, item) -> Union[dict, list]: ...
    def __iter__(self) -> Iterator: ...

class TapiResponse(BaseMethodsTapiResponse):
    def __call__(self) -> TapiExecutorResponse: ...

class TapiExecutorResponse(BaseMethodsTapiResponse):
    def extract(self) -> Union[dict, List[dict]]: ...

class TapiExecutorResponsePageIterator(TapiExecutorResponse):
    def pages(self, *, max_pages: int = None) -> Iterator["TapiResponse"]: ...

class TapiResponsePageIterator(TapiResponse):
    def __call__(self) -> TapiExecutorResponsePageIterator: ...

class TapiExecutor:
    def open_docs(self) -> TapiExecutor:
        """Open API official docs of resource in browser."""
    def open_in_browser(self) -> TapiExecutor:
        """Send a request in the browser."""
    def help(self) -> TapiExecutor:
        """Print docs of resource."""
    def get(
        self, *, params: dict = None, data: dict = None, headers: dict = None
    ) -> TapiResponse:
        """
        Send HTTP 'GET' request.

        :param params: querystring arguments in the URL
        :param data: send data in the body of the request
        """
    def post(
        self, *, params: dict = None, data: dict = None, headers: dict = None
    ) -> TapiResponse:
        """
        Send HTTP 'POST' request.

        :param params: querystring arguments in the URL
        :param data: send data in the body of the request
        """
    def delete(
        self, *, params: dict = None, data: dict = None, headers: dict = None
    ) -> TapiResponse:
        """
        Send HTTP 'DELETE' request.

        :param params: querystring arguments in the URL
        :param data: send data in the body of the request
        """
    def put(
        self, *, params: dict = None, data: dict = None, headers: dict = None
    ) -> TapiResponse:
        """
        Send HTTP 'PUT' request.

        :param params: querystring arguments in the URL
        :param data: send data in the body of the request
        """

class TapiExecutorWithPageIterator:
    def open_docs(self) -> TapiExecutorWithPageIterator:
        """Open API official docs of resource in browser."""
    def open_in_browser(self) -> TapiExecutorWithPageIterator:
        """Send a request in the browser."""
    def help(self) -> TapiExecutorWithPageIterator:
        """Print docs of resource."""
    def get(
        self, *, params: dict = None, data: dict = None, headers: dict = None
    ) -> TapiResponsePageIterator:
        """
        Send HTTP 'GET' request.

        :param params: querystring arguments in the URL
        :param data: send data in the body of the request
        """

class YandexMarket:
    def __init__(
        self,
        *,
        oauth_token: str,
        oauth_client_id: str,
        retry_if_exceeded_requests_limit: bool = True,
        session: requests.sessions.Session = requests.Session(),
        headers: dict = None,
    ):
        """
        :param skip_report_summary: (report resource) Do not display a line with the number of statistics lines in the report.
        """
    def campaigns(self) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns.html
        """
    def campaign(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id.html
        """
    def logins(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-logins.html
        """
    def campaigns_by_login(self, login: str) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-by-login.html
        """
    def settings(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-settings.html
        """
    def region(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-region.html
        """
    def feedback_updates(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feedback-updates.html
        """
    def offers(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offers.html
        """
    def all_offers(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offers-all.html
        """
    def feeds(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds.html
        """
    def feed(
        self, *, campaignId: Union[int, str], feedId: Union[int, str]
    ) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id.html
        """
    def feed_categories(
        self, *, campaignId: Union[int, str], feedId: Union[int, str]
    ) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id-categories.html
        """
    def all_feeds_categories(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-categories.html
        """
    def feed_index_logs(
        self, *, campaignId: Union[int, str], feedId: Union[int, str]
    ) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id-index-logs.html
        """
    def feed_parameters(
        self, *, campaignId: Union[int, str], feedId: Union[int, str]
    ) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-feeds-id-params.html
        """
    def feed_refresh(
        self, *, campaignId: Union[int, str], feedId: Union[int, str]
    ) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-feeds-id-refresh.html
        """
    def hidden_offers(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-hidden-offers.html
        """
    def update_offer_prices(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-offer-prices-updates.html
        """
    def remove_offer_prices(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-offer-prices-removals.html
        """
    def offer_prices(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offer-prices.html
        """
    def model(self, *, modelId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-models-id.html
        """
    def models(self) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-models.html
        """
    def model_offers(self, *, modelId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-models-id-offers.html
        """
    def models_offers(self) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-models-offers.html
        """
    def bids(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-bids.html
        """
    def bid_recommendations(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-recommendations-bids.html
        """
    def top_market_search(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-bids-recommended-top-market-search.html
        """
    def bids_settings(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-bids-settings.html
        """
    def balance(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-balance.html
        """
    def invoice_pay_preview(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-invoice-paypreview.html
        """
    def invoice(self) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-invoice.html
        """
    def campaign_invoice(
        self, *, campaignId: Union[int, str], invoiceId: Union[int, str]
    ) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-invoices-id.html
        """
    def stats(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html
        """
    def daily_stats(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html#examples__main-daily
        """
    def weekly_stats(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html#examples__main-weekly
        """
    def monthly_stats(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html#examples__main-monthly
        """
    def offers_stats(
        self, *, campaignId: Union[int, str]
    ) -> TapiExecutorWithPageIterator:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-offers.html
        """
    def geo_regions(self) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions.html
        """
    def geo_region(self, regionId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions-id.html
        """
    def region_children(self, regionId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions-id-children.html
        """
    def outlets(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-outlets.html
        """
    def outlet(
        self, *, campaignId: Union[int, str], outletId: Union[int, str]
    ) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/put-campaigns-id-outlets-id.html
        """
    def campaign_outlets(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-outlets.html
        """
    def outlets_licenses(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-outlets-licenses.html
        """
    def delivery_services_dictionary(self) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-delivery-services.html
        """
    def quality_tickets(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-tickets.html
        """
    def quality_ticket(
        self, *, campaignId: Union[int, str], ticketId: Union[int, str]
    ) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-tickets-id.html
        """
    def quality_report(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-report.html
        """
    def quality_ticket_fix(
        self, *, campaignId: Union[int, str], ticketId: Union[int, str]
    ) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-quality-tickets-id-fix.html
        """
    def quality_check(self, *, campaignId: Union[int, str]) -> TapiExecutor:
        """
        https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-quality-check.html
        """
