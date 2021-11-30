# Quickstart
[Instructions](https://yandex.ru/dev/market/partner/doc/dg/concepts/authorization.html) for get OAUTH_TOKEN and OAUTH_CLIENT_ID
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
campaigns = client.campaigns().get()
print(campaigns.data)
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
