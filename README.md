# Python client for [API Yandex Market](https://yandex.ru/dev/metrika/doc/api2/concept/about-docpage/)

![Supported Python Versions](https://img.shields.io/static/v1?label=python&message=>=3.6&color=green)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/vintasoftware/tapioca-wrapper/master/LICENSE)
[![Downloads](https://pepy.tech/badge/tapi-yandex-market)](https://pepy.tech/project/tapi-yandex-market)
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>


## Installation
    pip install --upgrade tapi-yandex-market==1.0.1


## [API docs](https://yandex.ru/dev/market/partner/doc/dg/concepts/about.html)

## Documentation
```python
from tapi_yandex_market import YandexMarket

OAUTH_TOKEN = "{oauth_token}"
OAUTH_CLIENT_ID = "{oauth_client_id}"

client = YandexMarket(
    # https://yandex.ru/dev/market/partner/doc/dg/concepts/authorization.html
    oauth_token=OAUTH_TOKEN,
    oauth_client_id=OAUTH_CLIENT_ID,
    # Will retry the request if the request limit is reached.
    retry_if_exceeded_requests_limit=True,
)
```

### Resource methods
```python
print(dir(client))
[
    'all_feeds_categories',
    'all_offers',
    'balance',
    'bid_recommendations',
    'bids',
    'bids_settings',
    'campaign',
    'campaign_invoice',
    'campaign_outlets',
    'campaigns',
    'campaigns_by_login',
    'daily_stats',
    'delivery_services_dictionary',
    'feed',
    'feed_categories',
    'feed_index_logs',
    'feed_parameters',
    'feed_refresh',
    'feedback_updates',
    'feeds',
    'geo_region',
    'geo_regions',
    'hidden_offers',
    'invoice',
    'invoice_pay_preview',
    'logins',
    'model',
    'model_offers',
    'models',
    'models_offers',
    'monthly_stats',
    'offer_prices',
    'offers',
    'offers_stats',
    'outlet',
    'outlets',
    'outlets_licenses',
    'quality_check',
    'quality_report',
    'quality_ticket',
    'quality_ticket_fix',
    'quality_tickets',
    'region',
    'region_children',
    'remove_offer_prices',
    'settings',
    'stats',
    'top_market_search',
    'update_offer_prices',
    'weekly_stats'
 ]
```

Detailed resource [information](tapi_yandex_market/resource_mapping.py)

### API requests

API requests are made using HTTP [methods](https://yandex.ru/dev/market/partner/doc/dg/concepts/method-call.html):
`DELETE`, `GET`, `POST`, `PUT`.

An example of an HTTP `GET` request
```python
from tapi_yandex_market import YandexMarket

client = YandexMarket(...)
result = client.campaigns().get()
# Raw data.
print(result.data)
```

An example of an HTTP `POST` request\
Resource [documentation](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-feeds-id-params.html)
```python
from tapi_yandex_market import YandexMarket

client = YandexMarket(...)
body = {
  "parameters":
  [
    {
      "deleted": {boolean},
      "name": "{enum}",
      "values":
      [
        {int32},
        ...
      ]
    },
    ...
  ]
}
result = client.feed_parameters(campaignId=..., feedId=...).post(data=body)
# Raw data.
print(result.data)
```

An example of an HTTP `PUT` request\
Resource [documentation](https://yandex.ru/dev/market/partner/doc/dg/reference/put-campaigns-id-auction-bids.html)
```python
from tapi_yandex_market import YandexMarket

client = YandexMarket(...)
body = {
  "bids":
  [
    {
      "feedId": {int64},
      "offerId": "{string}",
      "bid": {double},
      "dontPullUpBids": {boolean}
    },
    ...
  ]
}
result = client.bids(campaignId=...).put(data=body)
# Raw data.
print(result.data)
```

An example of an HTTP `DELETE` request\
Resource [documentation](https://yandex.ru/dev/market/partner/doc/dg/reference/delete-campaigns-id-outlets-licenses.html)
```python
from tapi_yandex_market import YandexMarket

client = YandexMarket(...)
result = client.outlets_licenses(campaignId=...).delete()
# Raw data.
print(result.data)
```

### Client response methods

Result extraction method.

```python
from tapi_yandex_market import YandexMarket

client = YandexMarket(...)
campaign = client.campaign(campaignId=100500).get()

print(type(campaign))
# <class 'tapi2.tapi.TapiClient'>
print(campaign)
# <class 'tapi2.tapi.TapiClient'>
# <TapiClient object
# {   'campaign': {   'clientId': 992161,
#                     'domain': 'lady-xl.ru',
#                     'id': 21033612,
#                     'state': 1}}>
print(campaign.status_code)
# 200

print(campaign.response)
# <Response [200]>

print(campaign.request_kwargs)
# {'url': 'https://api.partner.market.yandex.ru/v2/campaigns/100500', 'params': {}, 'headers': {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'OAuth oauth_token="...", oauth_client_id="..."'}, 'data': None}

print(type(campaign.data))
# <class 'dict'>

print(campaign.data)
# {'campaign': {'id': 123456789, 'clientId': 100999, 'domain': 'shop100500', 'state': 1}}

print(type(campaign["campaign"]))
# <class 'dict'>

print(campaign["campaign"])
# {'id': 123456789, 'clientId': 100999, 'domain': 'shop100500', 'state': 1}
```

### .extract()

Result extraction method.

```python
from tapi_yandex_market import YandexMarket

client = YandexMarket(...)
campaigns = client.campaigns().get()

print(campaigns.data)
# {'pager': {'total': 1, 'from': 1, 'to': 1, 'currentPage': 1, 'pagesCount': 1, 'pageSize': 1}, 'campaigns': [{'id': 21033612, 'clientId': 992161, 'domain': 'lady-xl.ru', 'state': 1}]}

campaigns_list = campaigns().extract()

print(type(campaigns_list))
# <class 'list'>

print(campaigns_list)
# [{'id': 21033612, 'clientId': 992161, 'domain': 'lady-xl.ru', 'state': 1}]

# Or

print(campaigns["campaigns"] == campaigns_list)
# True


# Or

print(campaigns.data["campaigns"] == campaigns["campaigns"] == campaigns_list)
```

## Example of exporting statistics
Resource [documentation](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html)
```python
import datetime as dt

from tapi_yandex_market import YandexMarket
from tapi_yandex_market.helper import iter_flatten_stats_row

client = YandexMarket(...)

campaign_id = 100500
params = dict(
    fromDate=dt.date.today() - dt.timedelta(days=3),
    toDate=dt.date.today(),
    byPlaces=True,
    fields="shows,mobile,model"
)
result = client.stats(campaignId=campaign_id).get(params=params)
data = result().extract()

print(data[0])
# {'clicks': 282,
# 'date': '2021-09-03',
# 'detailedStats': [{'clicks': 259,
#                 'shows': '1077017',
#                 'spending': 33.37,
#                 'type': 'mobile'}],
# 'placeGroup': 3,
# 'shows': '1409982',
# 'spending': 36.29}

new_column_names = {"clicksMobile": "clicks_mobile"}
data = list(iter_flatten_stats_row(data, **new_column_names))
print(data[0])
# {'clicks': 282,
#  'clicks_mobile': 259,
#  'date': '2021-09-03',
#  'placeGroup': 3,
#  'shows': '1409982',
#  'showsMobile': '1077017',
#  'spending': 36.29,
#  'spendingMobile': 33.37}
```


## Features

Information about the resource.
```python
client.campaigns().help()
```

Open resource documentation
```python
client.campaigns().open_docs()
```

Send a request in the browser.
```python
client.campaigns().open_in_browser()
```


## Dependences
- requests
- [tapi_wrapper](https://github.com/pavelmaksimov/tapi-wrapper)


## CHANGELOG
### v1.0.1
2021-09-06
- fix bugs

## Author
Pavel Maksimov

You can contact me at
[Телеграм](https://t.me/pavel_maksimow),
[Facebook](https://www.facebook.com/pavel.maksimow)

Good luck friend! Put an asterisk;)

Удачи тебе, друг! Поставь звездочку ;)
