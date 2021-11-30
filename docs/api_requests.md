
# API requests

how to execute various http methods:
`DELETE`, `GET`, `POST`, `PUT`.

## Example HTTP `GET` request
```python
from tapi_yandex_market import YandexMarket

client = YandexMarket(...)
result = client.campaigns().get()
# Raw data.
print(result.data)
```

## Example HTTP `POST` request
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

## Example HTTP `PUT` request
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

## Example HTTP `DELETE` request
Resource [documentation](https://yandex.ru/dev/market/partner/doc/dg/reference/delete-campaigns-id-outlets-licenses.html)
```python
from tapi_yandex_market import YandexMarket

client = YandexMarket(...)
result = client.outlets_licenses(campaignId=...).delete()
# Raw data.
print(result.data)
```
