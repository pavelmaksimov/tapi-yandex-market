# Example of exporting statistics from API Yandex Market
Resource [documentation](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html)
```python
import datetime as dt

from tapi_yandex_market import YandexMarket
from tapi_yandex_market.helper import iter_flatten_stats_row

OAUTH_TOKEN = "{oauth_token}"
OAUTH_CLIENT_ID = "{oauth_client_id}"

client = YandexMarket(
    # https://yandex.ru/dev/market/partner/doc/dg/concepts/authorization.html
    oauth_token=OAUTH_TOKEN,
    oauth_client_id=OAUTH_CLIENT_ID,
)
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

# Flatten data

new_column_names = {"clicksMobile": "my_custom_col_name_for_clicks_mobile"}
data = list(iter_flatten_stats_row(data, **new_column_names))
print(data[0])
# {'clicks': 282,
#  'my_custom_col_name_for_clicks_mobile': 259,
#  'date': '2021-09-03',
#  'placeGroup': 3,
#  'shows': '1409982',
#  'showsMobile': '1077017',
#  'spending': 36.29,
#  'spendingMobile': 33.37}
```
