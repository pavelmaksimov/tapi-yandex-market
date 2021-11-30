# Features

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

### Other

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
