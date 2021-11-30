Description | Client method name | HTTP Method | |
| ------------- | ------------- | ------------- | ------------- |
| [Магазины пользователя](#магазины-пользователя) | campaigns | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns.html) |
| [Информация о магазине](#информация-о-магазине) | campaign | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id.html) |
| [Логины связанные с магазином](#логины-связанные-с-магазином) | logins | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-logins.html) |
| [Магазины доступные логину](#магазины-доступные-логину) | campaigns_by_login | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-by-login.html) |
| [Настройки магазина](#настройки-магазина) | settings | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-settings.html) |
| [Регион магазина](#регион-магазина) | region | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-region.html) |
| [Новые и обновленные отзывы о магазине](#новые-и-обновленные-отзывы-о-магазине) | feedback_updates | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feedback-updates.html) |
| [Предложения магазина](#предложения-магазина) | offers | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offers.html) |
| [Все предложения магазина](#все-предложения-магазина) | all_offers | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offers-all.html) |
| [Список прайс-листов магазина](#список-прайс-листов-магазина) | feeds | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds.html) |
| [Информация о прайс-листе](#информация-о-прайс-листе) | feed | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id.html) |
| [Категории прайс-листа](#категории-прайс-листа) | feed_categories | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id-categories.html) |
| [Категории магазина](#категории-магазина) | all_feeds_categories | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-categories.html) |
| [Отчет по индексации прайс-листа](#отчет-по-индексации-прайс-листа) | feed_index_logs | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id-index-logs.html) |
| [Изменение параметров прайс-листа](#изменение-параметров-прайс-листа) | feed_parameters | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-feeds-id-params.html) |
| [Сообщить что прайс-лист обновился](#сообщить-что-прайс-лист-обновился) | feed_refresh | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-feeds-id-refresh.html) |
| [Информация о скрытых предложениях](#информация-о-скрытых-предложениях) | hidden_offers | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-hidden-offers.html) |
| [Скрытие предложений и настройки скрытия](#скрытие-предложений-и-настройки-скрытия) | hidden_offers | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-hidden-offers.html) |
| [Возобновление показа предложений](#возобновление-показа-предложений) | hidden_offers | DELETE | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/delete-campaigns-id-hidden-offers.html) |
| [Установка цен на предложения](#установка-цен-на-предложения) | update_offer_prices | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-offer-prices-updates.html) |
| [Удаление всех цен установленных через API](#удаление-всех-цен-установленных-через-api) | remove_offer_prices | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-offer-prices-removals.html) |
| [Список цен установленных через API](#список-цен-установленных-через-api) | offer_prices | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offer-prices.html) |
| [Информация о модели](#информация-о-модели) | model | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-models-id.html) |
| [Поиск модели товара](#поиск-модели-товара) | models | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-models.html) |
| [Информация о нескольких моделях](#информация-о-нескольких-моделях) | models | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-models.html) |
| [Список предложений для модели](#список-предложений-для-модели) | model_offers | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-models-id-offers.html) |
| [Список предложений для нескольких моделей](#список-предложений-для-нескольких-моделей) | models_offers | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-models-offers.html) |
| [Информация о ставках](#информация-о-ставках) | bids | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-bids.html) |
| [Установка ставок на предложения](#установка-ставок-на-предложения) | bids | PUT | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/put-campaigns-id-auction-bids.html) |
| [Рекомендации для карточки товара](#рекомендации-для-карточки-товара) | bid_recommendations | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-recommendations-bids.html) |
| [Рекомендации для поиска Маркета](#рекомендации-для-поиска-маркета) | bid_recommendations | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-recommendations-bids-market-search.html) |
| [Рекомендации по популярным запросам в поиске Маркета](#рекомендации-по-популярным-запросам-в-поиске-маркета) | top_market_search | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-bids-recommended-top-market-search.html) |
| [Рекомендации для поиска Яндекса](#рекомендации-для-поиска-яндекса) | bid_recommendations | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-recommendations-bids-search.html) |
| [Установка рекомендованных ставок](#установка-рекомендованных-ставок) | bid_recommendations | PUT | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/put-campaigns-id-auction-recommendations-bids.html) |
| [Настройки ставок](#настройки-ставок) | bids_settings | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-bids-settings.html) |
| [Баланс магазина и прогноз расходования средств](#баланс-магазина-и-прогноз-расходования-средств) | balance | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-balance.html) |
| [Базовая статистика](#базовая-статистика) | stats | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html) |
| [Статистика по предложениям](#статистика-по-предложениям) | offers_stats | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-offers.html) |
| [Поиск региона](#поиск-региона) | geo_regions | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions.html) |
| [Информация о регионе](#информация-о-регионе) | geo_region | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions-id.html) |
| [Информация о дочерних регионах](#информация-о-дочерних-регионах) | region_children | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions-id-children.html) |
| [Создание точки продаж](#создание-точки-продаж) | outlets | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-outlets.html) |
| [Изменение информации о точке продаж](#изменение-информации-о-точке-продаж) | outlet | PUT | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/put-campaigns-id-outlets-id.html) |
| [Удаление точки продаж](#удаление-точки-продаж) | outlet | DELETE | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/delete-campaigns-id-outlets-id.html) |
| [Информация о точках продаж](#информация-о-точках-продаж) | outlets | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-outlets.html) |
| [Информация о точке продаж](#информация-о-точке-продаж) | outlet | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-outlets-id.html) |
| [Создание и изменение лицензий для точек продаж](#создание-и-изменение-лицензий-для-точек-продаж) | outlets_licenses | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-outlets-licenses.html) |
| [Удаление лицензий для точек продаж](#удаление-лицензий-для-точек-продаж) | outlets_licenses | DELETE | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/delete-campaigns-id-outlets-licenses.html) |
| [Информация о лицензиях для точек продаж](#информация-о-лицензиях-для-точек-продаж) | outlets_licenses | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-outlets-licenses.html) |
| [Справочник служб доставки](#справочник-служб-доставки) | delivery_services_dictionary | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-delivery-services.html) |
| [Информация об ошибках магазина](#информация-об-ошибках-магазина) | quality_tickets | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-tickets.html) |
| [Информация об ошибке магазина](#информация-об-ошибке-магазина) | quality_ticket | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-tickets-id.html) |
| [Отчет по качеству](#отчет-по-качеству) | quality_report | GET | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-report.html) |
| [Сообщить что ошибка исправлена](#сообщить-что-ошибка-исправлена) | quality_ticket_fix | POST | [Docs](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-quality-tickets-id-fix.html) |


# Примеры

Для этих ресурсов примеры не составлены, но методы для них есть, можете их найти [тут](https://github.com/pavelmaksimov/tapi-yandex-market/blob/master/tapi_yandex_market/resource_mapping.py).
https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-invoice-paypreview.html
https://yandex.ru/dev/market/partner/doc/dg/reference/finance-cc.html
https://yandex.ru/dev/market/partner/doc/dg/reference/post-invoice.html
https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-invoices-id.html


## Магазины пользователя
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns Возвращает список магазинов, к которым имеет доступ пользователь — владелец авторизационного токена, использованного в запросе. Для агентских пользователей список состоит из подагентских магазинов. Примечание. Результаты рекомендуется получать постранично. Для этого укажите в запросе параметры page и pageSize. Иногда на последних страницах пейджера фактическое количество результатов оказывается меньше количества, указанного ранее на предыдущих страницах. В связи с этим настоятельно рекомендуется анализировать содержимое параметра pager для каждой полученной страницы.  URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
params = {
    "page": "Int32",  # optional
    "pageSize": "Int32"  # optional
}
response = client.campaigns().get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "campaigns": [
        {
            "domain": "{string}",
            "id": "{int64}",
            "clientId": "{int64}",
            "state": "{int32}",
            "stateReasons": [
                "{int32}"
            ]
        }
    ],
    "pager": {
        "currentPage": "{int32}",
        "from": "{int32}",
        "pagesCount": "{int32}",
        "pageSize": "{int32}",
        "to": "{int32}",
        "total": "{int32}"
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "campaigns": [
        {
            "domain": "nif-nif.yandex.ru",
            "id": 10001,
            "clientId": 885193,
            "state": 2,
            "stateReasons": [
                6,
                9
            ]
        },
        {
            "domain": "nuf-nuf.yandex.ru",
            "id": 10002,
            "clientId": 885193,
            "state": 4,
            "stateReasons": [
                21
            ]
        },
        {
            "domain": "naf-naf.yandex.ru",
            "id": 10003,
            "clientId": 589850,
            "state": 1
        }
    ],
    "pager": {
        "currentPage": 1,
        "from": 1,
        "pagesCount": 1,
        "pageSize": 3,
        "to": 3,
        "total": 3
    }
}</pre>
</details>


## Информация о магазине
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId} Возвращает информацию о магазине. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.campaign(campaignId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "campaign": {
        "domain": "{string}",
        "id": "{int64}",
        "clientId": "{int64}",
        "state": "{int32}",
        "stateReasons": [
            "{int32}"
        ]
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "campaign": {
        "domain": "nif-nif.yandex.ru",
        "id": 10001,
        "clientId": 885193,
        "state": 2,
        "stateReasons": [
            6,
            9
        ]
    }
}</pre>
</details>


## Логины связанные с магазином
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-logins.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/logins Возвращает список логинов, у которых есть доступ к магазину. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/logins.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.logins(campaignId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "logins": [
        "{string}"
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "logins": [
        "nif-nif",
        "naf-naf"
    ]
}</pre>
</details>


## Магазины доступные логину
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-by-login.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/by_login/{login} Возвращает список магазинов, к которым у пользователя с указанным логином есть доступ. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/by_login/{login}.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.campaigns_by_login(login=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "campaigns": [
        {
            "domain": "{string}",
            "id": "{int64}",
            "clientId": "{int64}",
            "state": "{int32}",
            "stateReasons": [
                "{int32}"
            ]
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "campaigns": [
        {
            "domain": "nuf-nuf.yandex.ru",
            "id": 10002,
            "clientId": 885193,
            "state": 4,
            "stateReasons": [
                21
            ]
        }
    ]
}</pre>
</details>


## Настройки магазина
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-settings.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/settings Возвращает информацию о настройках магазина, идентификатор которого указан в запросе. Примечание. Метод доступен начиная с версии 2.1 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/settings.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.settings(campaignId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "settings": {
        "countryRegion": "{int64}",
        "isOnline": "{boolean}",
        "shopName": "{string}",
        "showInContext": "{boolean}",
        "showInPremium": "{boolean}",
        "showInSnippets": "{boolean}",
        "useOpenStat": "{boolean}",
        "localRegion": {
            "id": "{int64}",
            "name": "{string}",
            "type": "{enum}",
            "delivery": {
                "schedule": {
                    "availableOnHolidays": "{boolean}",
                    "source": "{enum}",
                    "customHolidays": [
                        "{date}"
                    ],
                    "customWorkingDays": [
                        "{date}"
                    ],
                    "period": {
                        "fromDate": "{date}",
                        "toDate": "{date}"
                    },
                    "totalHolidays": [
                        "{date}"
                    ],
                    "weeklyHolidays": [
                        "{int8}"
                    ]
                }
            }
        }
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "settings": {
        "countryRegion": 225,
        "isOnline": true,
        "shopName": "Магазин",
        "showInContext": true,
        "showInPremium": true,
        "showInSnippets": true,
        "useOpenStat": false,
        "localRegion": {
            "id": 10740,
            "name": "Мытищи",
            "type": "CITY",
            "delivery": {
                "schedule": {
                    "availableOnHolidays": false,
                    "source": "WEB",
                    "customHolidays": [
                        "29-12-2016"
                    ],
                    "customWorkingDays": [],
                    "period": {
                        "fromDate": "23-12-2016",
                        "toDate": "10-02-2017"
                    },
                    "totalHolidays": [
                        "24-12-2016",
                        "25-12-2016",
                        "28-12-2016"
                    ],
                    "weeklyHolidays": [
                        3,
                        6,
                        7
                    ]
                }
            }
        }
    }
}</pre>
</details>


## Регион магазина
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-region.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/region Возвращает регион, в котором находится магазин.  Примечание. Метод доступен начиная с версии 1.2 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/region.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.region(campaignId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "region": {
        "id": "{int64}",
        "name": "{string}",
        "type": "{enum}",
        "parent": {
            "id": "{int64}",
            "name": "{string}",
            "type": "{enum}",
            "parent": {}
        }
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "region": {
        "id": 213,
        "name": "Москва",
        "type": "CITY",
        "parent": {
            "id": 1,
            "name": "Москва и Московская область",
            "type": "REPUBLIC",
            "parent": {
                "id": 3,
                "name": "Центральный федеральный округ",
                "type": "AREA",
                "parent": {
                    "id": 225,
                    "name": "Россия",
                    "type": "COUNTRY"
                }
            }
        }
    }
}</pre>
</details>


## Новые и обновленные отзывы о магазине
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feedback-updates.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/feedback/updates Возвращает новые и обновленные отзывы о магазине на Маркете. Результаты возвращаются постранично, одна страница содержит не более 20 отзывов. Выходные данные содержат идентификатор следующей страницы. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/feedback/updates.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В течение часа можно отправить не более 20 запросов. 
</details>

Пример:
```python
params = {
    "page_token": "String",  # optional
    "limit": "Int32",  # optional
    "from_date": "Date"  # optional
}
response = client.feedback_updates(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "status": "{enum}",
    "result": {
        "feedbackList": [
            {
                "id": "{int64}",
                "createdAt": "{date}",
                "state": "{enum}",
                "recommend": "{boolean}",
                "resolved": "{boolean}",
                "author": {
                    "name": "{string}",
                    "region": {
                        "id": "{int64}",
                        "name": "{string}",
                        "type": "{enum}"
                    }
                },
                "shop": {
                    "name": "{string}"
                },
                "grades": {
                    "average": "{int32}",
                    "agreeCount": "{int64}",
                    "rejectCount": "{int64}",
                    "factors": [
                        {
                            "id": "{int64}",
                            "title": "{string}",
                            "description": "{string}",
                            "value": "{int32}"
                        }
                    ]
                },
                "pro": "{string}",
                "contra": "{string}",
                "text": "{string}",
                "order": {
                    "shopOrderId": "{string}",
                    "delivery": "{enum}"
                },
                "comments": [
                    {
                        "id": "{int64}",
                        "createdAt": "{date}",
                        "updatedAt": "{date}",
                        "author": {
                            "type": "{enum}",
                            "name": "{string}"
                        },
                        "body": "{string}",
                        "children": [
                            {
                                "id": "{int64}",
                                "parentId": "{int64}",
                                "createdAt": "{date}",
                                "updatedAt": "{date}",
                                "author": {
                                    "type": "{enum}",
                                    "name": "{string}"
                                },
                                "body": "{string}",
                                "children": []
                            }
                        ]
                    }
                ]
            }
        ],
        "paging": {
            "nextPageToken": "{string}"
        }
    },
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
  "status": "OK",
  "result":
  {
    "feedbackList":
    [
      {
        "id": 31558,
        "createdAt": "2019-09-11T15:39:01+03:00",
        "state": "LAST",
        "recommend": true,
        "author":
        {
          "name": "Алиса Л.",
          "region":
          {
            "id": 213,
            "name": "Москва",
            "type": "CITY"
          }
        },
        "shop":
        {
          "name": "Магазин"
        },
        "grades":
        {
          "average": 5,
          "agreeCount": 11,
          "rejectCount": 2,
          "factors":
          [
            {
              "id": 0,
              "title": "Скорость обработки заказа",
              "description": "Как быстро с вами связались для подтверждения заказа?",
              "value": 5
            },
            {
              "id": 1,
              "title": "Скорость и качество доставки",
              "description": 
                "Устроила ли вас скорость доставки? Был ли заказ доставлен 
                в обозначенный срок?",
              "value": 5
            },
            {
              "id": 2,
              "title": "Общение",
              "description": "Вежливо ли с вами общались?",
              "value": 4
            },
            {
              "id": 3,
              "title": "Соответствие товара описанию",
              "description": "Вам привезли то, что вы ожидали?",
              "value": 5
            }
          ]
        },
        "pro": "Удобный сайт, большой выбор, доставили вовремя.",
        "contra": "Курьер не очень приветливый",
        "text":
          "Заказывала чайный сервиз. Тот, который хотела, был только в этом магазине.
          Почти сразу позвонили, подтвердили заказ. На следующий день сервиз уже был
          у меня. Правда, курьер был не в настроении и чуть не забыл отдать мне чек. Но
          это ничего. Спасибо вам большое!",
        "order":
        {
          "shopOrderId": "13А-1493887",
          "delivery": "DELIVERY"
        }
        "comments":
        [
          {
            "id": "992506491",
            "createdAt": "2019-09-11T19:15:27+03:00",
            "author":
            {
              "type": "SHOP",
              "name": "Магазин"
            },
            "body":
              "Спасибо большое за отзыв, Алиса! Рады, что вам все понравилось. 
              С курьером мы обязательно поговорим."
          }
        ]
      }
    ],
    "paging":
    {
      "nextPageToken": "EnJAxDO7tjZTiF7l"
    }
  }
}</pre>
</details>


## Предложения магазина
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offers.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/offers Позволяет фильтровать информацию о предложениях магазина, размещенных на Маркете, и искать предложения по заданному поисковому запросу. Поиск предложений, размещенных на Маркете, работает по поисковому запросу аналогично поиску Маркета. Результаты возвращаются с использованием пейджера. В ответе на запрос для каждого найденного предложения указывается URL и наименование этого предложения, его цена и валюта, в которой она указана, карточка модели Маркета, с которой соотнесено предложение, и аукционные ставки на него. Примечание. Из-за особенностей поиска Маркета иногда на последних страницах пейджера фактическое количество результатов оказывается меньше количества, указанного ранее на предыдущих страницах. В связи с этим настоятельно рекомендуется анализировать содержимое параметра pager для каждой полученной страницы.  URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/offers.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Количество запросов к ресурсу, которое возможно выполнить в течение суток, рассчитывается индивидуально и зависит от следующих показателей:   количество предложений.   Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  
</details>

Пример:
```python
params = {
    "currency": "Enum",  # optional
    "feedId": "Int64",  # optional
    "matched": "Boolean",  # optional
    "page": "Int32",  # optional
    "pageSize": "Int32",  # optional
    "query": "String",  # optional
    "shopCategoryId": "String"  # optional
}
response = client.offers(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "offers": [
        {
            "bid": "{double}",
            "currency": "{enum}",
            "cutPrice": "{boolean}",
            "discount": "{int32}",
            "feedId": "{int64}",
            "id": "{string}",
            "marketCategoryId": "{int32}",
            "modelId": "{int32}",
            "preDiscountPrice": "{float}",
            "price": "{float}",
            "shopCategoryId": "{string}",
            "name": "{string}",
            "url": "{string}"
        }
    ],
    "pager": {
        "currentPage": "{int32}",
        "from": "{int32}",
        "pagesCount": "{int32}",
        "pageSize": "{int32}",
        "to": "{int32}",
        "total": "{int32}"
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "offers": [
        {
            "bid": 1.16,
            "currency": "RUR",
            "cutPrice": false,
            "discount": 17,
            "feedId": 375216,
            "id": "1636288",
            "marketCategoryId": 226665,
            "modelId": 8350595,
            "preDiscountPrice": 8990,
            "price": 7490,
            "shopCategoryId": "129",
            "name": "Бинокли, Телескопы Nikon Aculon T11 8-24x25 (черный)",
            "url": "http://nuf-nuf.yandex.ru/product/21003"
        }
    ],
    "pager": {
        "currentPage": 1,
        "from": 1,
        "pagesCount": 1,
        "pageSize": 1,
        "to": 1,
        "total": 1
    }
}</pre>
</details>


## Все предложения магазина
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offers-all.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/offers/all Позволяет максимально быстро получить информацию обо всех предложениях магазина, размещенных на Маркете. Возвращает результат в виде сегментов нефиксированного размера. В ответе на запрос для каждого найденного предложения указывается URL и наименование этого предложения, его цена и валюта, в которой она указана, карточка модели Яндекс.Маркета, с которой соотнесено предложение, а также аукционные ставки на него. Примечание. Метод доступен начиная с версии 2.0 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/offers/all.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Количество запросов к ресурсу, которое возможно выполнить в течение суток, рассчитывается индивидуально и зависит от следующих показателей:   количество предложений.   Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  
</details>

Пример:
```python
params = {
    "chunk": "Int32",  # required
    "feedId": "Int64"  # required
}
response = client.all_offers(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "offers": [
        {
            "bid": "{double}",
            "blocked": "{boolean}",
            "currency": "{enum}",
            "discount": "{integer}",
            "feedId": "{integer}",
            "id": "{string}",
            "marketCategoryId": "{integer}",
            "modelId": "{integer}",
            "preDiscountPrice": "{float}",
            "price": "{float}",
            "shopCategoryId": "{string}",
            "name": "{string}",
            "url": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "offers": [
        {
            "bid": 1.16,
            "currency": "RUR",
            "discount": 17,
            "feedId": 375216,
            "id": "1636288",
            "marketCategoryId": 913,
            "modelId": 8350595,
            "preDiscountPrice": 8990,
            "price": 7490,
            "shopCategoryId": "129",
            "name": "Бинокли, Телескопы Nikon Aculon T11 8-24x25 (черный)",
            "url": "http://nuf-nuf.yandex.ru/product/21003"
        }
    ]
}</pre>
</details>


## Список прайс-листов магазина
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/feeds Возвращает список прайс-листов, размещенных на Маркете для магазина. Также ресурс возвращает результаты автоматических проверок прайс-листов. Примечание. Метод доступен начиная с версии 2.0 партнерского API Маркета. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/feeds.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.feeds(campaignId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "feeds": [
        {
            "id": "{int64}",
            "login": "{string}",
            "name": "{string}",
            "password": "{string}",
            "uploadDate": "{date}",
            "url": "{string}",
            "content": {
                "rejectedOffersCount": "{int32}",
                "status": "{enum}",
                "totalOffersCount": "{int32}",
                "error": {
                    "type": "{enum}"
                }
            },
            "download": {
                "status": "{enum}",
                "error": {
                    "httpStatusCode": "{int32}",
                    "type": "{enum}",
                    "description": "{string}"
                }
            },
            "placement": {
                "totalOffersCount": "{int32}"
            },
            "publication": {
                "status": "{enum}",
                "full": {
                    "fileTime": "{date}",
                    "publishedTime": "{date}"
                },
                "priceAndStockUpdate": {
                    "fileTime": "{date}",
                    "publishedTime": "{date}"
                }
            }
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "feeds": [
        {
            "id": 12345,
            "login": "badbadwolf",
            "password": "afraid",
            "url": "http://nuf-nuf.yandex.ru/price.xml",
            "content": {
                "rejectedOffersCount": 0,
                "status": "OK",
                "totalOffersCount": 534
            },
            "download": {
                "status": "OK"
            },
            "placement": {
                "totalOffersCount": 534
            },
            "publication": {
                "status": "OK",
                "full": {
                    "fileTime": "2017-12-14T21:42:42+03:00",
                    "publishedTime": "2017-12-14T23:42:42+03:00"
                },
                "priceAndStockUpdate": {
                    "fileTime": "2017-12-14T21:42:42+03:00",
                    "publishedTime": "2017-12-14T22:42:42+03:00"
                }
            }
        },
        {
            "id": 67891,
            "login": "badwolfbad",
            "password": "password",
            "url": "http://nuf-nuf.yandex.ru/price.xml",
            "content": {
                "status": "ERROR",
                "error": {
                    "type": "TOO_MANY_REJECTED_OFFERS"
                }
            },
            "download": {
                "status": "OK"
            },
            "placement": {
                "totalOffersCount": 0
            },
            "publication": {
                "status": "NA"
            }
        }
    ]
}</pre>
</details>


## Информация о прайс-листе
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/feeds/{feedId} Возвращает информацию о прайс-листе, размещенном на Маркете для заданного магазина. Также ресурс возвращает результаты автоматических проверок прайс-листа. Примечание. Метод доступен начиная с версии 2.0 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/feeds/{feedId}.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.feed(campaignId=..., feedId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "feed": {
        "id": "{int64}",
        "login": "{string}",
        "name": "{string}",
        "password": "{string}",
        "uploadDate": "{date}",
        "url": "{string}",
        "content": {
            "rejectedOffersCount": "{int32}",
            "status": "{enum}",
            "totalOffersCount": "{int32}",
            "error": {
                "type": "{enum}"
            }
        },
        "download": {
            "status": "{enum}",
            "error": {
                "httpStatusCode": "{int32}",
                "type": "{enum}",
                "description": "{string}"
            }
        },
        "placement": {
            "totalOffersCount": "{int32}"
        },
        "publication": {
            "status": "{enum}",
            "full": {
                "fileTime": "{date}",
                "publishedTime": "{date}"
            },
            "priceAndStockUpdate": {
                "fileTime": "{date}",
                "publishedTime": "{date}"
            }
        }
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "feed": {
        "id": 12345,
        "login": "badbadwolf",
        "password": "afraid",
        "url": "http://nuf-nuf.yandex.ru/price.xml",
        "content": {
            "rejectedOffersCount": 0,
            "status": "OK",
            "totalOffersCount": 534
        },
        "download": {
            "status": "OK"
        },
        "placement": {
            "totalOffersCount": 534
        },
        "publication": {
            "status": "OK",
            "full": {
                "fileTime": "2017-12-14T21:42:42+03:00",
                "publishedTime": "2017-12-14T23:42:42+03:00"
            },
            "priceAndStockUpdate": {
                "fileTime": "2017-12-14T21:42:42+03:00",
                "publishedTime": "2017-12-14T22:42:42+03:00"
            }
        }
    }
}</pre>
</details>


## Категории прайс-листа
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id-categories.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/feeds/{feedId}/categories Возвращает список категорий предложений из прайс-листа, размещенного на Маркете для заданного магазина. Информация о категориях для отключенных прайс-листов не предоставляется. В ответе на запрос для каждой категории возвращается ее название, идентификатор и идентификатор родительской категории. Список сортируется по возрастанию идентификатора категории. Если категорий много, результаты выдаются постранично. Примечание. Метод доступен начиная с версии 2.0 партнерского API Маркета. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/feeds/{feedId}/categories.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Для методов GET /campaigns/{campaignId}/feeds/categories и GET /campaigns/{campaignId}/feeds/{feedId}/categories действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество категорий, информация о которых запрошена при помощи этих методов. Объем запросов к ресурсу, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от следующих показателей:   количество категорий.   Примечание. Количество категорий считается за предыдущий день. 
</details>

Пример:
```python
params = {
    "page": "Int32",  # optional
    "pageSize": "Int32"  # optional
}
response = client.feed_categories(campaignId=..., feedId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "categories": [
        {
            "feedId": "{int64}",
            "id": "{string}",
            "name": "{string}",
            "parentId": "{string}"
        }
    ],
    "pager": {
        "currentPage": "{int32}",
        "from": "{int32}",
        "pagesCount": "{int32}",
        "pageSize": "{int32}",
        "to": "{int32}",
        "total": "{int32}"
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "categories": [
        {
            "feedId": 12345,
            "id": "1",
            "name": "Телевизоры"
        },
        {
            "feedId": 12347,
            "id": "2",
            "name": "ЖК",
            "parentId": "1"
        },
        {
            "feedId": 12347,
            "id": "3",
            "name": "Плазменные",
            "parentId": "1"
        }
    ],
    "pager": {
        "currentPage": 1,
        "from": 1,
        "pagesCount": 1,
        "pageSize": 3,
        "to": 3,
        "total": 3
    }
}</pre>
</details>


## Категории магазина
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-categories.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/feeds/categories Возвращает список категорий предложений для магазина по всем прайс-листам этого магазина, размещенным на Маркете. Информация о категориях для отключенных прайс-листов не предоставляется. В ответе на запрос для каждой категории указывается название, ее идентификатор и идентификатор родительской категории. Список сортируется сначала по возрастанию идентификатора прайс-листа, а затем по возрастанию идентификатора категории. Если категорий много, результаты выдаются постранично. Примечание. Метод доступен начиная с версии 2.0 партнерского API Маркета. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/feeds/categories.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Для методов GET /campaigns/{campaignId}/feeds/categories и GET /campaigns/{campaignId}/feeds/{feedId}/categories действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество категорий, информация о которых запрошена при помощи этих методов. Объем запросов к ресурсу, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от следующих показателей:   количество категорий.   Примечание. Количество категорий считается за предыдущий день. 
</details>

Пример:
```python
params = {
    "page": "Int32",  # optional
    "pageSize": "Int32"  # optional
}
response = client.all_feeds_categories(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "categories": [
        {
            "feedId": "{int64}",
            "id": "{string}",
            "name": "{string}",
            "parentId": "{string}"
        }
    ],
    "pager": {
        "currentPage": "{int32}",
        "from": "{int32}",
        "pagesCount": "{int32}",
        "pageSize": "{int32}",
        "to": "{int32}",
        "total": "{int32}"
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "categories": [
        {
            "feedId": 12345,
            "id": "1",
            "name": "Телевизоры"
        },
        {
            "feedId": 12345,
            "id": "2",
            "name": "ЖК",
            "parentId": "1"
        },
        {
            "feedId": 12345,
            "id": "3",
            "name": "Плазменные",
            "parentId": "1"
        },
        {
            "feedId": 67891,
            "id": "1",
            "name": "Телевизоры"
        },
        {
            "feedId": 67891,
            "id": "2",
            "name": "ЖК",
            "parentId": "1"
        },
        {
            "feedId": 67891,
            "id": "4",
            "name": "ЭЛТ",
            "parentId": "1"
        }
    ],
    "pager": {
        "currentPage": 1,
        "from": 1,
        "pagesCount": 1,
        "pageSize": 6,
        "to": 6,
        "total": 6
    }
}</pre>
</details>


## Отчет по индексации прайс-листа
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id-index-logs.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/feeds/{feedId}/index-logs Возвращает отчет по индексации прайс-листа для заданного магазина. Отчет позволяет получить статистику загрузки прайс-листа и результаты его автоматических проверок. Данные в отчете возвращаются в порядке убывания значений параметра generation-id. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/feeds/{feedId}/index-logs.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
params = {
    "limit": "Int32",  # optional
    "offset": "Int32",  # optional
    "page": "Int32",  # optional
    "pageSize": "Int32",  # optional
    "published_time_from": "Data",  # optional
    "published_time_to": "Data",  # optional
    "status": "Enum"  # optional
}
response = client.feed_index_logs(campaignId=..., feedId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "result": {
        "feed": {
            "id": "{int64}"
        },
        "indexLogRecords": [
            {
                "downloadTime": "{date}",
                "fileTime": "{date}",
                "generationId": "{int64}",
                "indexType": "{enum}",
                "publishedTime": "{date}",
                "status": "{enum}",
                "error": {
                    "httpStatusCode": "{int32}",
                    "type": "{enum}",
                    "description": "{string}"
                },
                "offers": {
                    "rejectedCount": "{int32}",
                    "totalCount": "{int32}"
                }
            }
        ],
        "total": "{int32}"
    },
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "result": {
        "feed": {
            "id": 12345
        },
        "indexLogRecords": [
            {
                "downloadTime": "2017-11-21T00:42:42+03:00",
                "fileTime": "2017-11-20T00:42:42+03:00",
                "generationId": 20321,
                "indexType": "FULL",
                "publishedTime": "2017-11-21T01:42:42+03:00",
                "status": "WARNING",
                "offers": {
                    "rejectedCount": 99,
                    "totalCount": 10231
                }
            },
            {
                "downloadTime": "2017-11-21T15:42:42+03:00",
                "fileTime": "2017-11-20T15:42:42+03:00",
                "generationId": 20320,
                "indexType": "FAST_PRICE",
                "publishedTime": "2017-11-21T15:42:42+03:00",
                "status": "ERROR",
                "error": {
                    "type": "DOWNLOAD_ERROR",
                    "description": "server status is no status code; ERR: errcode: 6, msg: Could not resolve host: nif-nif.yandex.ru"
                }
            }
        ],
        "total": 1229
    },
    "status": "OK"
}</pre>
</details>


## Изменение параметров прайс-листа
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-feeds-id-params.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/feeds/{feedId}/params Позволяет магазину изменить параметры прайс-листа. Чтобы отредактировать параметр прайс-листа, передайте в теле запроса: name (название параметра) и value (значение параметра). Чтобы отменить установленное значение, передайте в теле запроса: name (название параметра) и delete=true (удалить значение).  Примечание. В течение часа магазин может выполнить запрос не более трех раз для одного прайс-листа. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/feeds/{feedId}/params.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
body = {
    "parameters": [
        {
            "deleted": "{boolean}",
            "name": "{enum}",
            "values": [
                "{int32}"
            ]
        }
    ]
}
response = client.feed_parameters(campaignId=..., feedId=...).post(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>


## Сообщить что прайс-лист обновился
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-feeds-id-refresh.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/feeds/{feedId}/refresh Позволяет сообщить, что магазин обновил прайс-лист. После этого Маркет начнет обновление данных на сервисе.   Магазин обновляет прайс-лист, ссылку на который он указал в личном кабинете.   Магазин отправляет Маркету запрос методом POST /campaigns/{campaignId}/feeds/{feedId}/refresh.   Маркет начинает обновление данных магазина на сервисе.   Внимание. Запрос работает только для включенных магазинов. Если магазин выключен, данные на Маркете не обновятся, даже если HTTP-код — 200 OK. Проверить статус магазина можно с помощью базовых запросов или на странице бизнес-аккаунта. Примечание. В течение часа магазин может выполнить запрос не более трех раз для одного прайс-листа. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/feeds/{feedId}/refresh.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.feed_refresh(campaignId=..., feedId=...).post()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>


## Информация о скрытых предложениях
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-hidden-offers.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/hidden-offers Возвращает список скрытых предложений магазина. Предложения отсортированы в лексикографическом порядке: сначала по возрастанию идентификаторов прайс-листов, затем по возрастанию идентификаторов предложений. Результаты возвращаются постранично. Выходные данные содержат идентификаторы предыдущей и следующей страницы. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/hidden-offers.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно получить информацию не более чем о 500 предложениях. 
</details>

Пример:
```python
params = {
    "page_token": "String",  # optional
    "limit": "Int32",  # optional
    "offset": "Int32",  # optional
    "page_number": "Int32",  # optional
    "page_size": "Int32",  # optional
    "feed_id": "Int64",  # optional
    "offer_id": "String"  # optional
}
response = client.hidden_offers(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "result": {
        "hiddenOffers": [
            {
                "comment": "{string}",
                "feedId": "{int64}",
                "offerId": "{string}",
                "ttlInHours": "{int32}"
            }
        ],
        "total": "{int32}",
        "paging": {
            "prevPageToken": "{string}",
            "nextPageToken": "{string}"
        }
    },
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "result": {
        "hiddenOffers": [
            {
                "comment": "До поставки новой партии товара",
                "feedId": 67891,
                "offerId": "101Ab12313C",
                "ttlInHours": 1
            }
        ],
        "total": 3,
        "paging": {
            "nextPageToken": "Hj0gP0AQUIID01IE"
        }
    },
    "status": "OK"
}</pre>
</details>


## Скрытие предложений и настройки скрытия
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-hidden-offers.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/hidden-offers Метод позволяет:   Скрыть предложения магазина на Маркете на указанное время. В теле запроса можно передать от одного до 500 предложений.   Изменить время скрытия предложений и комментарии. Чтобы внести изменения, передайте в теле запроса идентификатор уже скрытого предложения, идентификатор его прайс-листа и новые значения параметров comment и / или ttl-in-hours. При этом предыдущие значения этих параметров будут удалены.   URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/hidden-offers.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно скрыть или изменить параметры скрытия не более чем 500 предложений. В течение минуты можно скрыть или изменить параметры скрытия определенного количества предложений. Если у магазина:  не более 200 000 предложений — 1000 предложений; более 200 000 предложений — ограничение определяется по формуле: (количество предложений магазина) / 200  Примечание. Количество предложений магазина считается по данным за последние семь дней (не включая сегодня).  
</details>

Пример:
```python
body = {
    "hiddenOffers": [
        {
            "feedId": "{int64}",
            "offerId": "{string}",
            "comment": "{string}",
            "ttlInHours": "{int32}"
        }
    ]
}
response = client.hidden_offers(campaignId=...).post(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>


## Возобновление показа предложений
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/delete-campaigns-id-hidden-offers.html) ресурса

<details>
<summary>Описание</summary>
Описание DELETE /campaigns/{campaignId}/hidden-offers Возобновляет показ предложений магазина на Маркете, скрытых через партнерский API запросом POST /campaigns/{campaignId}/hidden-offers. Если предложение не отображается по другой причине (например, удалено из прайс-листа или не соответствует требованиям Маркета), оно не начнет показываться. В теле запроса можно передать от одного до 500 предложений. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/hidden-offers.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно возобновить показы не более чем 500 предложений. В течение минуты можно возобновить показы определенного количества предложений. Если у магазина:  не более 200 000 предложений — 1000 предложений; более 200 000 предложений — ограничение определяется по формуле: (количество предложений магазина) / 200  Примечание. Количество предложений магазина считается по данным за последние семь дней (не включая сегодня).  
</details>

Пример:
```python
body = {
    "hiddenOffers": [
        {
            "feedId": "{int64}",
            "offerId": "{string}"
        }
    ]
}
response = client.hidden_offers(campaignId=...).delete(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>


## Установка цен на предложения
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-offer-prices-updates.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/offer-prices/updates Запрос позволяет обновлять цены предложений на часть ассортимента. Внимание. Запрос работает только для включенных магазинов. Если магазин выключен, данные на Маркете не обновятся, даже если HTTP-код — 200 OK. Проверить статус магазина можно с помощью базовых запросов или на странице бизнес-аккаунта. Чтобы установить новую цену вместо указанной в прайс-листе, передайте в теле запроса параметр price. Цена устанавливается на 30 дней с последнего обновления, после этого снова начнет действовать цена из прайс-листа. Чтобы удалить цену предложения, установленную через API, передайте в теле запроса параметр delete=true. После удаления начнет действовать цена из прайс-листа. Передача цен осуществляется в теле POST-запроса. Примечание. Запрос доступен начиная с версии 2.38 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/offer-prices/updates.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно установить или удалить цены не более чем для 2000 предложений. В течение минуты можно установить или удалить цены для определенного количества предложений. Если у магазина:  не более 10 000 предложений — 50 предложений; более 10 000 предложений — ограничение определяется по формуле: (количество предложений магазина) / 200  Примечание. Количество предложений магазина считается по данным за последние семь дней (не включая сегодня).  
</details>

Пример:
```python
body = {
    "offers": [
        {
            "feed": {
                "id": "{int64}"
            },
            "id": "{string}",
            "delete": "{boolean}",
            "price": {
                "currencyId": "{enum}",
                "value": "{float}",
                "discountBase": "{float}"
            }
        }
    ]
}
response = client.update_offer_prices(campaignId=...).post(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>


## Удаление всех цен установленных через API
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-offer-prices-removals.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/offer-prices/removals Запрос удаляет все цены на предложения, установленные через API. После удаления начнут действовать цены из прайс-листов. Внимание. Запрос работает только для включенных магазинов. Если магазин выключен, данные на Маркете не обновятся, даже если HTTP-код — 200 OK. Проверить статус магазина можно с помощью базовых запросов или на странице бизнес-аккаунта. Примечание. Запрос доступен начиная с версии 2.38 партнерского API Яндекс.Маркета. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/offer-prices/removals.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Первый запрос в минуту удаляет все цены, установленные по API. Последующие запросы в ту же минуту также удаляют все цены, но только если в предыдущем запросе не было превышено ограничение. То есть если до первого запроса в минуту установленных через API цен было больше, чем ограничение, то этот запрос, удалив цены, его превысит. Второй запрос за минуту не выполнится, и сервер вернет ошибку о превышении ограничения.  Ограничение зависит от количества предложений магазина:   для небольших магазинов (не более 10 000 предложений) — 50 предложений;   для остальных магазинов это ограничение определяется по формуле:   (количество предложений магазина) / 200    Общее количество предложений магазина считается по данным за последние семь дней, не включая текущий день. 
</details>

Пример:
```python
body = {
    "removeAll": true
}
response = client.remove_offer_prices(campaignId=...).post(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>


## Список цен установленных через API
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offer-prices.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/offer-prices Запрос возвращает список цен, установленных через партнерский API. Примечание. Запрос доступен начиная с версии 2.38 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/offer-prices.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Количество предложений, о которых можно получить информацию в течение суток, определяется по формуле:  (количество предложений магазина) * 25 Примечание. Общее количество предложений считается по данным за последние семь дней (не включая сегодня).  
</details>

Пример:
```python
params = {
    "limit": "Int32",  # optional
    "offset": "Int32",  # optional
    "page": "Int32",  # optional
    "pageSize": "Int32"  # optional
}
response = client.offer_prices(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "result": {
        "offers": [
            {
                "feed": {
                    "id": "{int64}"
                },
                "id": "{string}",
                "price": {
                    "currencyId": "{enum}",
                    "discountBase": "{float}",
                    "value": "{float}"
                },
                "updatedAt": "{string}"
            }
        ],
        "total": "{int32}"
    },
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "result": {
        "offers": [
            {
                "feed": {
                    "id": 479633
                },
                "id": "1636288",
                "price": {
                    "currencyId": "RUR",
                    "value": 1500.0
                },
                "updatedAt": "2018-04-13T13:13:01+03:00"
            },
            {
                "feed": {
                    "id": 479633
                },
                "id": "1687614",
                "price": {
                    "currencyId": "RUR",
                    "discountBase": 900.0,
                    "value": 820.0
                },
                "updatedAt": "2018-04-12T09:44:42+03:00"
            }
        ],
        "total": 4
    },
    "status": "OK"
}</pre>
</details>


## Информация о модели
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-models-id.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /models/{modelId} Возвращает информацию о модели товара. Примечание. Метод доступен начиная с версии 1.2 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/models/{modelId}.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Для методов GET /models, GET /models/{modelId} и POST /models действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество моделей, информация о которых запрошена при помощи этих методов. Объем запросов к ресурсу, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от следующих показателей:   количество предложений на карточках моделей;   количество активных магазинов клиента.   Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  Для клиентов с несколькими магазинами ограничение рассчитывается с учетом количества предложений, являющегося максимальным среди всех магазинов клиента. Для агентств ограничение суммируется по всем субклиентам агентства. 
</details>

Пример:
```python
params = {
    "regionId": "Int64",  # required
    "currency": "Enum"  # optional
}
response = client.model(modelId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "models": [
        {
            "id": "{int64}",
            "name": "{string}",
            "prices": {
                "avg": "{float}",
                "max": "{float}",
                "min": "{float}"
            }
        }
    ],
    "currency": "{enum}",
    "regionId": "{int64}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "models": [
        {
            "id": 7012977,
            "name": "Galaxy S II I9100",
            "prices": {
                "avg": 22690,
                "max": 50000,
                "min": 14130
            }
        }
    ],
    "currency": "RUR",
    "regionId": 213
}</pre>
</details>


## Поиск модели товара
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-models.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /models Возвращает информацию о моделях, удовлетворяющих заданным в запросе условиям поиска. В одном запросе можно получить информацию не более чем о 100 моделях. Примечание. Метод доступен начиная с версии 1.2 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/models.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно получить информацию не более чем о 100 моделях. Для методов GET /models, GET /models/{modelId} и POST models действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество моделей, информация о которых запрошена при помощи этих методов. Объем запросов к ресурсу, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от следующих показателей:   количество предложений на карточках моделей;   количество активных магазинов клиента.   Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  Для клиентов с несколькими магазинами ограничение рассчитывается с учетом количества предложений, являющегося максимальным среди всех магазинов клиента. Для агентств ограничение суммируется по всем субклиентам агентства. 
</details>

Пример:
```python
params = {
    "query": "String",  # required
    "regionId": "Int64",  # required
    "currency": "Enum",  # optional
    "page": "Int32",  # optional
    "pageSize": "Int32"  # optional
}
response = client.models().get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "models": [
        {
            "id": "{int64}",
            "name": "{string}",
            "prices": {
                "avg": "{float}",
                "max": "{float}",
                "min": "{float}"
            }
        }
    ],
    "currency": "{enum}",
    "regionId": "{int64}",
    "pager": {
        "currentPage": "{int32}",
        "from": "{int32}",
        "pageSize": "{int32}",
        "pagesCount": "{int32}",
        "to": "{int32}",
        "total": "{int32}"
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "models": [
        {
            "id": 7717706,
            "name": "Apple iPhone 4S 16 Gb",
            "prices": {
                "avg": 24990,
                "max": 68400,
                "min": 21500
            }
        },
        {
            "id": 7717686,
            "name": "Apple iPhone 4S 32 Gb",
            "prices": {
                "avg": 28500,
                "max": 46000,
                "min": 24450
            }
        },
        {
            "id": 7717687,
            "name": "Apple iPhone 4S 64 Gb",
            "prices": {
                "avg": 32500,
                "max": 89950,
                "min": 27200
            }
        }
    ],
    "pager": {
        "currentPage": 1,
        "from": 1,
        "pageSize": 3,
        "pagesCount": 1088,
        "to": 3,
        "total": 3263
    },
    "currency": "RUR",
    "regionId": 2
}</pre>
</details>


## Информация о нескольких моделях
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-models.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /models Возвращает информацию о моделях товаров. В одном запросе можно получить информацию не более чем о 100 моделях. Примечание. Метод доступен начиная с версии 1.2 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/models.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно получить информацию не более чем о 100 моделях. Для методов GET /models, GET /models/{modelId} и POST /models действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество моделей, информация о которых запрошена при помощи этих методов. Объем запросов к ресурсу, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от следующих показателей:   количество предложений на карточках моделей;   количество активных магазинов клиента.   Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  Для клиентов с несколькими магазинами ограничение рассчитывается с учетом количества предложений, являющегося максимальным среди всех магазинов клиента. Для агентств ограничение суммируется по всем субклиентам агентства. 
</details>

Пример:
```python
body = {
    "models": [
        "{int64}"
    ]
}
params = {
    "regionId": "Int64",  # required
    "currency": "Enum"  # optional
}
response = client.models().post(data=body, params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "models": [
        {
            "id": "{int64}",
            "name": "{string}",
            "prices": {
                "avg": "{float}",
                "max": "{float}",
                "min": "{float}"
            }
        }
    ],
    "currency": "{enum}",
    "regionId": "{int64}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "models": [
        {
            "id": 1234567,
            "name": "Apple iPhone 6S 32 Gb",
            "prices": {
                "avg": 24990,
                "max": 68400,
                "min": 21500
            }
        },
        {
            "id": 8910111,
            "name": "Apple iPhone 6S 64 Gb",
            "prices": {
                "avg": 28500,
                "max": 46000,
                "min": 24450
            }
        }
    ],
    "currency": "RUR",
    "regionId": 2
}</pre>
</details>


## Список предложений для модели
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-models-id-offers.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /models/{modelId}/offers Возвращает информацию о первых десяти предложениях, расположенных на карточке модели. Предложения выдаются для определенного региона и располагаются в том же порядке, в котором они показываются в выдаче Маркета на карточке модели. Для групповых моделей метод не поддерживается. Идентификатор групповой модели игнорируется. Примечание. Метод доступен начиная с версии 1.2 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/models/{modelId}/offers.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Для методов GET /models/{modelId}/offers и POST /models/offers действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество моделей, информация о которых запрошена при помощи этих методов. Объем запросов к ресурсу, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от следующих показателей:   количество предложений на карточках моделей;   количество активных магазинов клиента.   Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  Для клиентов с несколькими магазинами ограничение рассчитывается с учетом количества предложений, являющегося максимальным среди всех магазинов клиента. Для агентств ограничение суммируется по всем субклиентам агентства. 
</details>

Пример:
```python
params = {
    "regionId": "Int64",  # required
    "currency": "Enum",  # optional
    "orderByPrice": "Enum"  # optional
}
response = client.model_offers(modelId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "currency": "{enum}",
    "models": [
        {
            "id": "{int64}",
            "offers": [
                {
                    "discount": "{int32}",
                    "name": "{string}",
                    "pos": "{int32}",
                    "preDiscountPrice": "{float}",
                    "price": "{float}",
                    "regionId": "{int64}",
                    "shippingCost": "{float}",
                    "shopName": "{string}",
                    "shopRating": "{int32}",
                    "inStock": "{int32}"
                }
            ],
            "offlineOffers": "{int32}",
            "onlineOffers": "{int32}"
        }
    ],
    "regionId": "{int64}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "models": [
        {
            "id": 11002659,
            "offers": [
                {
                    "name": "Стиральная машина Bosch WOT 20255",
                    "pos": 1,
                    "price": 37970,
                    "regionId": 213,
                    "shippingCost": 490,
                    "shopName": "Магазин.Ру",
                    "shopRating": 5
                },
                {
                    "name": "Стиральная машина Bosch WOT20255OE",
                    "pos": 2,
                    "price": 47990,
                    "regionId": 213,
                    "shippingCost": 490,
                    "shopName": "Ниф-Ниф.Ру",
                    "shopRating": 4
                },
                {
                    "name": "Стиральная машина Bosch WOT 20255OE",
                    "pos": 3,
                    "price": 47990,
                    "regionId": 213,
                    "shippingCost": 600,
                    "shopName": "Наф-Наф.Ру",
                    "shopRating": 5
                },
                {
                    "discount": 15,
                    "name": "Bosch WOT 20255",
                    "pos": 4,
                    "preDiscountPrice": 40000,
                    "price": 34000,
                    "regionId": 213,
                    "shippingCost": 999,
                    "shopName": "Нуф-Нуф.Ру",
                    "shopRating": 3
                },
                {
                    "name": "Стиральная машина с вертикальной загрузкой Bosch WOT20255OE",
                    "pos": 5,
                    "price": 38990,
                    "regionId": 213,
                    "shippingCost": 490,
                    "shopName": "Волк.Ру",
                    "shopRating": 4
                },
                {
                    "name": "Стиральная машина Bosch WOT20255OE",
                    "pos": 6,
                    "price": 38989,
                    "regionId": 213,
                    "shippingCost": 450,
                    "shopName": "Белоснежка.Ру",
                    "shopRating": 4
                },
                {
                    "name": "Стиральная машина Bosch WOT 20255OE",
                    "pos": 7,
                    "price": 47990,
                    "regionId": 213,
                    "shippingCost": 600,
                    "shopName": "ИльяМуромец.Ру",
                    "shopRating": 5
                },
                {
                    "name": "Стиральная машина с вертикальной загрузкой Bosch WOT20255OE",
                    "pos": 8,
                    "price": 37390,
                    "regionId": 213,
                    "shippingCost": 0,
                    "shopName": "ДобрыняНикитич.Ру",
                    "shopRating": 4
                },
                {
                    "name": "Стиральная машина Bosch WOT 20255",
                    "pos": 9,
                    "price": 36740,
                    "regionId": 213,
                    "shippingCost": 600,
                    "shopName": "АлешаПопович.Ру",
                    "shopRating": 4
                },
                {
                    "name": "Стиральная машина с вертикальной загрузкой Bosch WOT20255OE",
                    "pos": 10,
                    "price": 37390,
                    "regionId": 213,
                    "shippingCost": 700,
                    "shopName": "Медведь.Ру",
                    "shopRating": 3
                }
            ],
            "offlineOffers": 258,
            "onlineOffers": 15
        }
    ],
    "currency": "RUR",
    "regionId": 213
}</pre>
</details>


## Список предложений для нескольких моделей
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-models-offers.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /models/offers Возвращает информацию о первых десяти предложениях, расположенных на карточках моделей, идентификаторы которых указаны в запросе. Предложения выдаются для определенного региона и располагаются в том же порядке, в котором они показываются в выдаче Маркета на карточке модели. Для групповых моделей выдача предложений не поддерживается. Идентификаторы групповых моделей игнорируются. В одном запросе можно получить информацию о предложениях не более чем для 100 моделей. Примечание. Метод доступен начиная с версии 1.2 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/models/offers.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно получить информацию о предложениях не более чем для 100 моделей. Для методов GET /models/{modelId}/offers и POST /models/offers действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество моделей, информация о которых запрошена при помощи этих методов. Объем запросов к ресурсу, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от следующих показателей:   количество предложений на карточках моделей;   количество активных магазинов клиента.   Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  Для клиентов с несколькими магазинами ограничение рассчитывается с учетом количества предложений, являющегося максимальным среди всех магазинов клиента. Для агентств ограничение суммируется по всем субклиентам агентства. 
</details>

Пример:
```python
body = {
    "models": [
        "{int64}"
    ]
}
params = {
    "regionId": "Int64",  # required
    "currency": "Enum",  # optional
    "orderByPrice": "Enum"  # optional
}
response = client.models_offers().post(data=body, params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "models": [
        {
            "id": "{int64}",
            "name": "{string}",
            "offers": [
                {
                    "discount": "{int32}",
                    "name": "{string}",
                    "pos": "{int32}",
                    "preDiscountPrice": "{float}",
                    "price": "{float}",
                    "regionId": "{int64}",
                    "shippingCost": "{float}",
                    "shopName": "{string}",
                    "shopRating": "{int32}",
                    "inStock": "{int32}"
                }
            ],
            "prices": {
                "avg": "{double}",
                "max": "{double}",
                "min": "{double}"
            },
            "offlineOffers": "{int32}",
            "onlineOffers": "{int32}"
        }
    ],
    "currency": "{enum}",
    "regionId": "{int64}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "models": [
        {
            "id": 11002659,
            "name": "Стиральная машина Bosch WOT 20255",
            "offers": [
                {
                    "name": "Стиральная машина Bosch WOT 20255",
                    "pos": 1,
                    "price": 37970,
                    "regionId": 213,
                    "shippingCost": 490,
                    "shopName": "Магазин.Ру",
                    "shopRating": 5
                },
                {
                    "name": "Стиральная машина Bosch WOT20255OE",
                    "pos": 2,
                    "price": 47990,
                    "regionId": 213,
                    "shippingCost": 490,
                    "shopName": "Ниф-Ниф.Ру",
                    "shopRating": 4
                },
                {
                    "name": "Стиральная машина Bosch WOT 20255OE",
                    "pos": 3,
                    "price": 47990,
                    "regionId": 213,
                    "shippingCost": 600,
                    "shopName": "Наф-Наф.Ру",
                    "shopRating": 5
                },
                {
                    "discount": 15,
                    "name": "Bosch WOT 20255",
                    "pos": 4,
                    "preDiscountPrice": 40000,
                    "price": 34000,
                    "regionId": 213,
                    "shippingCost": 999,
                    "shopName": "Нуф-Нуф.Ру",
                    "shopRating": 3
                },
                {
                    "name": "Стиральная машина с вертикальной загрузкой Bosch WOT20255OE",
                    "pos": 5,
                    "price": 38990,
                    "regionId": 213,
                    "shippingCost": 490,
                    "shopName": "Волк.Ру",
                    "shopRating": 4
                },
                {
                    "name": "Стиральная машина Bosch WOT20255OE",
                    "pos": 6,
                    "price": 38989,
                    "regionId": 213,
                    "shippingCost": 450,
                    "shopName": "Белоснежка.Ру",
                    "shopRating": 4
                },
                {
                    "name": "Стиральная машина Bosch WOT 20255OE",
                    "pos": 7,
                    "price": 47990,
                    "regionId": 213,
                    "shippingCost": 600,
                    "shopName": "ИльяМуромец.Ру",
                    "shopRating": 5
                },
                {
                    "name": "Стиральная машина с вертикальной загрузкой Bosch WOT20255OE",
                    "pos": 8,
                    "price": 37390,
                    "regionId": 213,
                    "shippingCost": 0,
                    "shopName": "ДобрыняНикитич.Ру",
                    "shopRating": 4
                },
                {
                    "name": "Стиральная машина Bosch WOT 20255",
                    "pos": 9,
                    "price": 36740,
                    "regionId": 213,
                    "shippingCost": 600,
                    "shopName": "АлешаПопович.Ру",
                    "shopRating": 4
                },
                {
                    "name": "Стиральная машина Bosch WOT 20255 OE",
                    "pos": 10,
                    "price": 38990,
                    "regionId": 213,
                    "shippingCost": 0,
                    "shopName": "Медведь.Ру",
                    "shopRating": 3
                }
            ],
            "offlineOffers": 258,
            "onlineOffers": 14
        }
    ],
    "prices": {
        "avg": 40995,
        "max": 47990,
        "min": 34000
    },
    "currency": "RUR",
    "regionId": 213
}</pre>
</details>


## Информация о ставках
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-bids.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/auction/bids Возвращает информацию об установленных ставках на предложения для магазина. Предложения, для которых нужно получить информацию, передаются в теле POST-запроса. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/auction/bids.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно получить информацию не более чем о 500 предложениях. Количество запросов к ресурсу, которое возможно выполнить в течение суток, рассчитывается индивидуально и зависит от количества предложений магазина. Примечание. Количество предложений магазина считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  
</details>

Пример:
```python
body = {
    "offers": [
        {
            "feedId": "{int64}",
            "offerId": "{string}"
        }
    ]
}
response = client.bids(campaignId=...).post(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "status": "{enum}",
    "result": {
        "bids": [
            {
                "feedId": "{int64}",
                "offerId": "{string}",
                "bid": "{double}",
                "dontPullUpBids": "{boolean}",
                "status": "{enum}",
                "modified": "{date}"
            }
        ]
    },
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK",
    "result": {
        "bids": [
            {
                "feedId": 31920,
                "offerId": "120",
                "bid": 0.22,
                "dontPullUpBids": false,
                "status": "PUBLISHED",
                "modified": "2018-12-11T14:28:00+03:00"
            },
            {
                "feedId": 31920,
                "offerId": "122",
                "status": "ERROR_OFFER_NOT_FOUND"
            },
            {
                "feedId": 31920,
                "offerId": "121",
                "bid": 0.51,
                "dontPullUpBids": false,
                "status": "INDEXING",
                "modified": "2018-12-19T10:33:27+03:00"
            }
        ]
    }
}</pre>
</details>


## Установка ставок на предложения
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/put-campaigns-id-auction-bids.html) ресурса

<details>
<summary>Описание</summary>
Описание PUT /campaigns/{campaignId}/auction/bids Устанавливает или удаляет ставки на предложения. Внимание. Для использования этого запроса необходимо, чтобы в личном кабинете в качестве источника информации о ставках был выбран личный кабинет и API. Значения ставок передаются в теле PUT-запроса. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/auction/bids.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно установить ставки не более чем для 500 предложений. Для запросов PUT /campaigns/{campaignId/auction/bids, POST /campaigns/{campaignId}/auction/recommendations/bids, POST /campaigns/{campaignId}/bids/recommended/top/market-search и PUT /campaigns/{campaignId}/auction/recommendations/bids действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество предложений, по которым при помощи этих методов выставлены ставки или получены рекомендации. Объем запросов к ресурсам, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от количества предложений магазина на карточках товаров. Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  
</details>

Пример:
```python
body = {
    "bids": [
        {
            "feedId": "{int64}",
            "offerId": "{string}",
            "bid": "{double}",
            "dontPullUpBids": "{boolean}"
        }
    ]
}
response = client.bids(campaignId=...).put(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "status": "{enum}",
    "result": {
        "bidsSet": [
            {
                "feedId": "{int64}",
                "offerId": "{string}",
                "bid": "{double}",
                "dontPullUpBids": "{boolean}",
                "error": "{enum}"
            }
        ]
    },
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK",
    "result": {
        "bidsSet": [
            {
                "feedId": 30919,
                "offerId": "239982",
                "bid": 0.22
            },
            {
                "feedId": 30919,
                "offerId": "239983",
                "bid": 0.22
            },
            {
                "feedId": 30919,
                "offerId": "239984",
                "error": "OFFER_NOT_FOUND"
            }
        ]
    }
}</pre>
</details>


## Рекомендации для карточки товара
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-recommendations-bids.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/auction/recommendations/bids Возвращает рекомендованные значения ставок на предложения для размещения этих предложений на карточках товаров. Внимание. Возвращаемые ставки являются прогнозируемыми и не гарантируют попадание предложения на указанное место размещения.  Предложения, для которых нужно получить рекомендации, передаются в теле POST-запроса. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/auction/recommendations/bids.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно получить рекомендованные ставки не более чем для 500 предложений. Для запросов PUT /campaigns/{campaignId/auction/bids, POST /campaigns/{campaignId}/auction/recommendations/bids, POST /campaigns/{campaignId}/bids/recommended/top/market-search и PUT /campaigns/{campaignId}/auction/recommendations/bids действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество предложений, по которым при помощи этих методов выставлены ставки или получены рекомендации. Объем запросов к ресурсам, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от количества предложений магазина на карточках товаров. Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  
</details>

Пример:
```python
params = {
    "target": "Enum",  # optional
    "positions": "String",  # optional
    "region_id": "Int64"  # optional
}
response = client.bid_recommendations(campaignId=...).post(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "status": "{enum}",
    "result": {
        "recommendations": [
            {
                "feedId": "{int64}",
                "offerId": "{string}",
                "bid": "{double}",
                "minBid": "{double}",
                "dontPullUpBids": "{boolean}",
                "error": "{enum}",
                "modelCard": {
                    "currentPosAll": "{int64}",
                    "currentPosTop": "{int64}",
                    "topOffersCount": "{int64}",
                    "error": "{enum}",
                    "posRecommendations": [
                        {
                            "pos": "{int64}",
                            "bid": "{double}",
                            "error": "{enum}"
                        }
                    ]
                }
            }
        ]
    },
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK",
    "result": {
        "recommendations": [
            {
                "feedId": 3456,
                "offerId": "12",
                "bid": 0.32,
                "minBid": 0.32,
                "dontPullUpBids": false,
                "modelCard": {
                    "currentPosAll": 5,
                    "currentPosTop": 5,
                    "posRecommendations": [
                        {
                            "pos": 1,
                            "error": "UNREACHABLE"
                        },
                        {
                            "pos": 2,
                            "error": "UNREACHABLE"
                        },
                        {
                            "pos": 3,
                            "error": "UNREACHABLE"
                        },
                        {
                            "pos": 4,
                            "error": "UNREACHABLE"
                        },
                        {
                            "pos": 5,
                            "bid": 3.87
                        },
                        {
                            "pos": 6,
                            "bid": 1.03
                        },
                        {
                            "pos": 7,
                            "bid": 0.89
                        },
                        {
                            "pos": 8,
                            "bid": 0.86
                        },
                        {
                            "pos": 9,
                            "bid": 0.51
                        },
                        {
                            "pos": 10,
                            "bid": 0.5
                        }
                    ]
                }
            }
        ]
    }
}</pre>
</details>


## Рекомендации для поиска Маркета
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-recommendations-bids-market-search.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/auction/recommendations/bids Возвращает рекомендованные значения ставок на предложения для размещения среди первых 12 предложений магазинов в поиске Маркета. Внимание. Возвращаемые ставки являются прогнозируемыми и не гарантируют попадание предложения на указанное место размещения.  Предложения, для которых нужно получить рекомендации, передаются в теле POST-запроса. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/auction/recommendations/bids.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно получить рекомендованные ставки не более чем для 500 предложений. Для запросов PUT /campaigns/{campaignId/auction/bids, POST /campaigns/{campaignId}/auction/recommendations/bids, POST /campaigns/{campaignId}/bids/recommended/top/market-search и PUT /campaigns/{campaignId}/auction/recommendations/bids действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество предложений, по которым при помощи этих методов выставлены ставки или получены рекомендации. Объем запросов к ресурсам, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от количества предложений на карточках товаров. Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  
</details>

Пример:
```python
body = {
    "offers": [
        {
            "feedId": "{int64}",
            "offerId": "{string}",
            "query": "{string}"
        }
    ]
}
params = {
    "target": "Enum",  # required
    "positions": "String",  # optional
    "region_id": "Int64"  # optional
}
response = client.bid_recommendations(campaignId=...).post(data=body, params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "status": "{enum}",
    "result": {
        "recommendations": [
            {
                "feedId": "{int64}",
                "offerId": "{string}",
                "bid": "{double}",
                "minBid": "{double}",
                "dontPullUpBids": "{boolean}",
                "error": "{enum}",
                "marketSearch": {
                    "currentPosAll": "{int64}",
                    "modelCount": "{int64}",
                    "error": "{enum}",
                    "posRecommendations": [
                        {
                            "pos": "{int64}",
                            "bid": "{double}",
                            "error": "{enum}"
                        }
                    ]
                }
            }
        ]
    },
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK",
    "result": {
        "recommendations": [
            {
                "feedId": 383610,
                "offerId": "1234",
                "bid": 0.34,
                "minBid": 0.27,
                "dontPullUpBids": false,
                "marketSearch": {
                    "currentPosAll": 2,
                    "modelCount": 0,
                    "posRecommendations": [
                        {
                            "pos": 1,
                            "error": "UNREACHABLE"
                        },
                        {
                            "pos": 2,
                            "bid": 0.27
                        },
                        {
                            "pos": 3,
                            "bid": 0.27
                        },
                        {
                            "pos": 4,
                            "bid": 0.27
                        },
                        {
                            "pos": 5,
                            "bid": 0.27
                        },
                        {
                            "pos": 6,
                            "bid": 0.27
                        },
                        {
                            "pos": 7,
                            "bid": 0.27
                        },
                        {
                            "pos": 8,
                            "bid": 0.27
                        },
                        {
                            "pos": 9,
                            "bid": 0.27
                        },
                        {
                            "pos": 10,
                            "bid": 0.27
                        },
                        {
                            "pos": 11,
                            "bid": 0.27
                        },
                        {
                            "pos": 12,
                            "bid": 0.27
                        }
                    ]
                }
            }
        ]
    }
}</pre>
</details>


## Рекомендации по популярным запросам в поиске Маркета
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-bids-recommended-top-market-search.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/bids/recommended/top/market-search Возвращает:   список популярных запросов в поиске Маркета, рекомендованных для предложения;   рекомендованные значения ставок.   Рекомендации возвращаются для размещения среди первых 12 предложений магазинов в поиске Маркета и рассчитываются для региона, в котором находится магазин. Внимание. Запрос работает только для товаров без карточек. Если у товара есть карточка, для предложения вернется пустой список рекомендаций. Подробнее см. в разделе Как понять, есть ли у товара карточка Справки Маркета для модели ADV. Возвращаемые ставки являются прогнозируемыми и не гарантируют попадание предложения на указанное место размещения.  Cписок предложений, для которых необходимо получить рекомендации, передается в теле POST-запроса. Действует ограничение на количество предложений в одном запросе: 500 предложений. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/bids/recommended/top/market-search.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Для запросов PUT /campaigns/{campaignId/auction/bids, POST /campaigns/{campaignId}/auction/recommendations/bids, POST /campaigns/{campaignId}/bids/recommended/top/market-search и PUT /campaigns/{campaignId}/auction/recommendations/bids действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество предложений, по которым при помощи этих методов выставлены ставки или получены рекомендации. Объем запросов к ресурсам, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от количества предложений магазина на карточках товаров. Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  
</details>

Пример:
```python
body = {
    "offers": [
        {
            "feedId": "{int64}",
            "id": "{string}"
        }
    ]
}
response = client.top_market_search(campaignId=...).post(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "result": {
        "topRecommendations": [
            {
                "bid": "{double}",
                "dontPullUpBids": "{boolean}",
                "feedId": "{double}",
                "minBid": "{double}",
                "offerId": "{string}",
                "name": "{string}",
                "queries": [
                    {
                        "averageOfferPos": "{int32}",
                        "currentPosAll": "{int32}",
                        "modelCount": "{int32}",
                        "offerShowCount": "{int32}",
                        "queryShowCount": "{int32}",
                        "text": "{string}",
                        "type": "{enum}",
                        "positions": [
                            {
                                "bid": "{double}",
                                "error": "{enum}",
                                "pos": "{int32}"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "result": {
        "topRecommendations": [
            {
                "bid": 0.12,
                "feedId": 789101,
                "minBid": 0.12,
                "offerId": "123456",
                "name": "Lenovo G5045 80E301Q9RK black 15.6 HD E1-6010 / 2 Gb / 500 Gb / noDVD / W10",
                "queries": [
                    {
                        "averageOfferPos": 2,
                        "currentPosAll": 1,
                        "modelCount": 0,
                        "offerShowCount": 22,
                        "queryShowCount": 50,
                        "text": "80E301Q9RK",
                        "type": "TOP_OFFER",
                        "positions": [
                            {
                                "bid": 0.12,
                                "pos": 1
                            },
                            {
                                "bid": 0.12,
                                "pos": 2
                            },
                            {
                                "bid": 0.12,
                                "pos": 3
                            },
                            {
                                "bid": 0.12,
                                "pos": 4
                            },
                            {
                                "bid": 0.12,
                                "pos": 5
                            },
                            {
                                "bid": 0.12,
                                "pos": 6
                            },
                            {
                                "bid": 0.12,
                                "pos": 7
                            },
                            {
                                "pos": 8,
                                "bid": 0.12
                            },
                            {
                                "pos": 9,
                                "bid": 0.12
                            },
                            {
                                "bid": 0.12,
                                "pos": 10
                            },
                            {
                                "bid": 0.12,
                                "pos": 11
                            },
                            {
                                "bid": 0.12,
                                "pos": 12
                            }
                        ]
                    },
                    {
                        "averageOfferPos": 47,
                        "currentPosAll": 1,
                        "modelCount": 0,
                        "offerShowCount": 17,
                        "queryShowCount": 2478,
                        "text": "9RK",
                        "type": "TOP_OFFER",
                        "positions": [
                            {
                                "bid": 0.12,
                                "pos": 1
                            },
                            {
                                "bid": 0.12,
                                "pos": 2
                            },
                            {
                                "bid": 0.12,
                                "pos": 3
                            },
                            {
                                "bid": 0.12,
                                "pos": 4
                            },
                            {
                                "bid": 0.12,
                                "pos": 5
                            },
                            {
                                "bid": 0.12,
                                "pos": 6
                            },
                            {
                                "bid": 0.12,
                                "pos": 7
                            },
                            {
                                "bid": 0.12,
                                "pos": 8
                            },
                            {
                                "bid": 0.12,
                                "pos": 9
                            },
                            {
                                "bid": 0.12,
                                "pos": 10
                            },
                            {
                                "bid": 0.12,
                                "pos": 11
                            },
                            {
                                "bid": 0.12,
                                "pos": 12
                            }
                        ]
                    }
                ]
            },
            {
                "bid": 0.13,
                "feedId": 789101,
                "minBid": 0.13,
                "offerId": "112131",
                "name": "Компьютер C400008Ц-NORBEL Office Base ATI-Intel Core i3 4170 / H81M-P33 / 4 Gb / 500 Gb",
                "queries": [
                    {
                        "averageOfferPos": 10,
                        "currentPosAll": 10,
                        "modelCount": 0,
                        "offerShowCount": 14,
                        "queryShowCount": 267,
                        "text": "H81M-P33",
                        "type": "TOP_ALL",
                        "positions": [
                            {
                                "bid": 0.68,
                                "pos": 1
                            },
                            {
                                "bid": 0.68,
                                "pos": 2
                            },
                            {
                                "bid": 0.63,
                                "pos": 3
                            },
                            {
                                "bid": 0.6,
                                "pos": 4
                            },
                            {
                                "bid": 0.55,
                                "pos": 5
                            },
                            {
                                "bid": 0.52,
                                "pos": 6
                            },
                            {
                                "bid": 0.52,
                                "pos": 7
                            },
                            {
                                "bid": 0.4,
                                "pos": 8
                            },
                            {
                                "bid": 0.18,
                                "pos": 9
                            },
                            {
                                "bid": 0.13,
                                "pos": 10
                            },
                            {
                                "bid": 0.13,
                                "pos": 11
                            },
                            {
                                "bid": 0.13,
                                "pos": 12
                            }
                        ]
                    },
                    {
                        "averageOfferPos": 9,
                        "modelCount": 0,
                        "offerShowCount": 7,
                        "queryShowCount": 73,
                        "text": "H81M-P33 PLUS",
                        "type": "TOP_ALL",
                        "positions": [
                            {
                                "error": "UNREACHABLE",
                                "pos": 1
                            },
                            {
                                "error": "UNREACHABLE",
                                "pos": 2
                            },
                            {
                                "bid": 0.49,
                                "pos": 3
                            },
                            {
                                "bid": 0.41,
                                "pos": 4
                            },
                            {
                                "bid": 0.41,
                                "pos": 5
                            },
                            {
                                "bid": 0.41,
                                "pos": 6
                            },
                            {
                                "bid": 0.38,
                                "pos": 7
                            },
                            {
                                "bid": 0.34,
                                "pos": 8
                            },
                            {
                                "bid": 0.13,
                                "pos": 9
                            },
                            {
                                "bid": 0.13,
                                "pos": 10
                            },
                            {
                                "bid": 0.13,
                                "pos": 11
                            },
                            {
                                "bid": 0.13,
                                "pos": 12
                            }
                        ]
                    },
                    {
                        "averageOfferPos": 10,
                        "currentPosAll": 9,
                        "modelCount": 0,
                        "offerShowCount": 4,
                        "queryShowCount": 51,
                        "text": "H81M-P",
                        "type": "TOP_ALL",
                        "positions": [
                            {
                                "bid": 1.0,
                                "pos": 1
                            },
                            {
                                "bid": 0.99,
                                "pos": 2
                            },
                            {
                                "bid": 0.61,
                                "pos": 3
                            },
                            {
                                "bid": 0.59,
                                "pos": 4
                            },
                            {
                                "bid": 0.51,
                                "pos": 5
                            },
                            {
                                "bid": 0.49,
                                "pos": 6
                            },
                            {
                                "bid": 0.49,
                                "pos": 7
                            },
                            {
                                "bid": 0.27,
                                "pos": 8
                            },
                            {
                                "bid": 0.13,
                                "pos": 9
                            },
                            {
                                "bid": 0.13,
                                "pos": 10
                            },
                            {
                                "bid": 0.13,
                                "pos": 11
                            },
                            {
                                "bid": 0.13,
                                "pos": 12
                            }
                        ]
                    },
                    {
                        "averageOfferPos": 10,
                        "currentPosAll": 10,
                        "modelCount": 0,
                        "offerShowCount": 14,
                        "queryShowCount": 267,
                        "text": "H81M-P33",
                        "type": "TOP_OFFER",
                        "positions": [
                            {
                                "bid": 0.68,
                                "pos": 1
                            },
                            {
                                "bid": 0.68,
                                "pos": 2
                            },
                            {
                                "bid": 0.63,
                                "pos": 3
                            },
                            {
                                "bid": 0.6,
                                "pos": 4
                            },
                            {
                                "bid": 0.55,
                                "pos": 5
                            },
                            {
                                "bid": 0.52,
                                "pos": 6
                            },
                            {
                                "bid": 0.52,
                                "pos": 7
                            },
                            {
                                "bid": 0.4,
                                "pos": 8
                            },
                            {
                                "bid": 0.18,
                                "pos": 9
                            },
                            {
                                "bid": 0.13,
                                "pos": 10
                            },
                            {
                                "bid": 0.13,
                                "pos": 11
                            },
                            {
                                "bid": 0.13,
                                "pos": 12
                            }
                        ]
                    },
                    {
                        "averageOfferPos": 9,
                        "modelCount": 0,
                        "offerShowCount": 7,
                        "queryShowCount": 73,
                        "text": "H81M-P33 PLUS",
                        "type": "TOP_OFFER",
                        "positions": [
                            {
                                "error": "UNREACHABLE",
                                "pos": 1
                            },
                            {
                                "error": "UNREACHABLE",
                                "pos": 2
                            },
                            {
                                "bid": 0.49,
                                "pos": 3
                            },
                            {
                                "bid": 0.41,
                                "pos": 4
                            },
                            {
                                "bid": 0.41,
                                "pos": 5
                            },
                            {
                                "bid": 0.41,
                                "pos": 6
                            },
                            {
                                "bid": 0.38,
                                "pos": 7
                            },
                            {
                                "bid": 0.34,
                                "pos": 8
                            },
                            {
                                "bid": 0.13,
                                "pos": 9
                            },
                            {
                                "bid": 0.13,
                                "pos": 10
                            },
                            {
                                "bid": 0.13,
                                "pos": 11
                            },
                            {
                                "bid": 0.13,
                                "pos": 12
                            }
                        ]
                    },
                    {
                        "averageOfferPos": 10,
                        "currentPosAll": 9,
                        "modelCount": 0,
                        "offerShowCount": 4,
                        "queryShowCount": 51,
                        "text": "H81M-P",
                        "type": "TOP_OFFER",
                        "positions": [
                            {
                                "bid": 1.0,
                                "pos": 1
                            },
                            {
                                "bid": 0.99,
                                "pos": 2
                            },
                            {
                                "bid": 0.61,
                                "pos": 3
                            },
                            {
                                "bid": 0.59,
                                "pos": 4
                            },
                            {
                                "bid": 0.51,
                                "pos": 5
                            },
                            {
                                "bid": 0.49,
                                "pos": 6
                            },
                            {
                                "bid": 0.49,
                                "pos": 7
                            },
                            {
                                "bid": 0.27,
                                "pos": 8
                            },
                            {
                                "bid": 0.13,
                                "pos": 9
                            },
                            {
                                "bid": 0.13,
                                "pos": 10
                            },
                            {
                                "bid": 0.13,
                                "pos": 11
                            },
                            {
                                "bid": 0.13,
                                "pos": 12
                            }
                        ]
                    }
                ]
            }
        ]
    }
}</pre>
</details>


## Рекомендации для поиска Яндекса
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-recommendations-bids-search.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/auction/recommendations/bids Возвращает рекомендованные значения ставок на предложения для размещения этих предложений в поиске Яндекса. Внимание. Возвращаемые ставки являются прогнозируемыми и не гарантируют попадание предложения на указанное место размещения. Предложения, для которых нужно получить рекомендации, передаются в теле POST-запроса. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/auction/recommendations/bids.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно получить рекомендованные ставки не более чем для 500 предложений. Для запросов PUT /campaigns/{campaignId/auction/bids, POST /campaigns/{campaignId}/auction/recommendations/bids, POST /campaigns/{campaignId}/bids/recommended/top/market-search и PUT /campaigns/{campaignId}/auction/recommendations/bids действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество предложений, по которым при помощи этих методов выставлены ставки или получены рекомендации. Объем запросов к ресурсам, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от количества предложений магазина на карточках моделей. Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  
</details>

Пример:
```python
body = {
    "offers": [
        {
            "feedId": "{int64}",
            "offerId": "{string}",
            "query": "{string}"
        }
    ]
}
params = {
    "target": "Enum",  # required
    "positions": "String",  # optional
    "region_id": "Int64"  # optional
}
response = client.bid_recommendations(campaignId=...).post(data=body, params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "status": "{enum}",
    "result": {
        "recommendations": [
            {
                "feedId": "{int64}",
                "offerId": "{string}",
                "bid": "{double}",
                "minBid": "{double}",
                "dontPullUpBids": "{boolean}",
                "error": "{enum}",
                "search": {
                    "error": "{enum}",
                    "posRecommendations": [
                        {
                            "pos": "{int64}",
                            "bid": "{double}",
                            "error": "{enum}"
                        }
                    ]
                }
            }
        ]
    },
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
  "status": "OK",
  "result":
  {
    "recommendations":
    [
      {
        "offerName": "Часы Casio SHE-3800SG-7A (серебристый)",
        "bid": 5.00,
        "minBid": 0.32,
        "dontPullUpBids": false,
        "search":
        {
          "posRecommendations":
          [
            "1":
            {
              "bid": 55.01
            },
            "5":
            {
              "bid": 0.36
            }
          ]
        }
      }
    ]
  }
}</pre>
</details>


## Установка рекомендованных ставок
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/put-campaigns-id-auction-recommendations-bids.html) ресурса

<details>
<summary>Описание</summary>
Описание PUT /campaigns/{campaignId}/auction/recommendations/bids Устанавливает рекомендованные значения ставок на предложения для размещения этих предложений на приоритетных местах на Маркете. При установке ставок возможно применение модификаторов к рекомендованным значениям этих ставок: относительного (задается в процентах) и абсолютного (задается в условных единицах). Если указаны одновременно оба модификатора, сначала применяется относительный, затем — абсолютный. Также возможно задать максимальный лимит на устанавливаемые значения ставок. Лимит проверяется после применения к ставкам модификаторов. Если в результате применения модификаторов значения какой-либо ставки вышли за допустимые пределы, ставка корректируется до ближайшего допустимого значения. Внимание. Для использования этого метода необходимо, чтобы в личном кабинете в качестве источника информации о ставках был выбран вариант В личном кабинете, в PriceLabs или через API. Предложения, для которых нужно установить рекомендованные ставки, передаются в теле POST-запроса. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/auction/recommendations/bids.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В одном запросе можно установить рекомендованные ставки не более чем для 500 предложений. Для запросов PUT /campaigns/{campaignId/auction/bids, POST /campaigns/{campaignId}/auction/recommendations/bids, POST /campaigns/{campaignId}/bids/recommended/top/market-search и PUT /campaigns/{campaignId}/auction/recommendations/bids действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество предложений, по которым при помощи этих методов выставлены ставки или получены рекомендации. Объем запросов к ресурсам, который возможно выполнить в течение суток, рассчитывается индивидуально и зависит от количества предложений магазина на карточках товаров. Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  
</details>

Пример:
```python
body = {
    "offers": [
        {
            "feedId": "{int64}",
            "offerId": "{string}",
            "query": "{string}"
        }
    ]
}
params = {
    "position": "Int32",  # required
    "target": "Enum",  # optional
    "offset_pct": "Double",  # optional
    "offset": "Double",  # optional
    "max_bid": "Double",  # optional
    "region_id": "Int64"  # optional
}
response = client.bid_recommendations(campaignId=...).put(data=body, params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "status": "{enum}",
    "result": {
        "bidsSet": [
            {
                "feedId": "{int64}",
                "offerId": "{string}",
                "bid": "{double}",
                "error": "{enum}"
            }
        ]
    },
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK",
    "result": {
        "bidsSet": [
            {
                "feedId": 30919,
                "offerId": "239982",
                "bid": 0.33
            },
            {
                "feedId": 30919,
                "offerId": "239983",
                "bid": 0.27
            },
            {
                "feedId": 30919,
                "offerId": "239984",
                "error": "OFFER_NOT_FOUND"
            }
        ]
    }
}</pre>
</details>


## Настройки ставок
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-bids-settings.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/bids/settings Возвращает информацию о настройках установленных ставок для магазина. Примечание. Метод доступен начиная с версии 2.1 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/bids/settings.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.bids_settings(campaignId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "settings": {
        "autobrokerEnabled": "{boolean}",
        "bidsFrom": "{enum}",
        "offerIdBy": "{enum}",
        "bookBids": {
            "bid": "{int64}"
        },
        "shopBids": {
            "bid": "{int64}"
        }
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "settings": {
        "autobrokerEnabled": true,
        "bidsFrom": "UI_OR_API",
        "offerIdBy": "OFFER_ID",
        "bookBids": {
            "bid": 10
        },
        "shopBids": {
            "bid": 10
        }
    }
}</pre>
</details>


## Баланс магазина и прогноз расходования средств
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-balance.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/balance Возвращает актуальный баланс средств магазина, а также прогноз расходования средств и рекомендации по размеру платежа. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/balance.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.balance(campaignId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "balance": {
        "balance": "{double}",
        "daysLeft": "{int32}",
        "recommendedPayment": "{double}"
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "balance": {
        "balance": 85.74,
        "daysLeft": 4,
        "recommendedPayment": 415.0
    }
}</pre>
</details>


## Базовая статистика
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/stats/main
GET /campaigns/{campaignId}/stats/main-daily
GET /campaigns/{campaignId}/stats/main-weekly
GET /campaigns/{campaignId}/stats/main-monthly Методы возвращают базовую статистику (клики, показы и расход) по магазину за запрашиваемый период времени. Максимальный период времени для получения статистики в одном запросе — 180 дней.  Вы можете получить статистику по кликам, которые система зафиксировала:   в момент их совершения (по дате события);   после проверки кликов на наличие недействительного трафика (по дате учета).   Примечание. Чтобы отсеять недействительный трафик, требуется некоторое время. Поэтому если клик был совершен пользователем в конце дня, а система завершила проверку клика на следующий день, то дата события и дата учета будут отличаться. Статистика по кликам доступна за все время с момента размещения магазина. Статистика по показам доступна за последние 30 дней размещения. Статистика суммируется и выводится в зависимости от ресурса запроса:   /campaigns/{campaignId}/stats/main — для каждого дня запрашиваемого периода;   /campaigns/{campaignId}/stats/main-daily — для каждого дня запрашиваемого периода (аналогично /campaigns/{campaignId}/stats/main);   /campaigns/{campaignId}/stats/main-weekly — по неделям запрашиваемого периода;   /campaigns/{campaignId}/stats/main-monthly — по месяцам запрашиваемого периода.   URL ресурсов: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/stats/main.[format]
https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/stats/main-daily.[format]
https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/stats/main-weekly.[format]
https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/stats/main-monthly.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
params = {
    "fromDate": "Date",  # required
    "byEventtime": "Boolean",  # optional
    "byPlaces": "Boolean",  # optional
    "clickType": "Int32",  # optional
    "fields": "Enum",  # optional
    "spendingFilter": "Enum",  # optional
    "toDate": "Date"  # optional
}
response = client.stats(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "mainStats": [
        {
            "clicks": "{int32}",
            "date": "{date}",
            "placeGroup": "{int32}",
            "shows": "{int32}",
            "spending": "{double}",
            "detailedStats": [
                {
                    "clicks": "{int32}",
                    "shows": "{int32}",
                    "spending": "{double}",
                    "type": "{enum}"
                }
            ]
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>None</pre>
</details>


## Статистика по предложениям
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-offers.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/stats/offers Возвращает базовую статистику (клики и расход) по предложениям магазина за запрашиваемый период времени. В статистике собраны клики по дате события, которые не вошли в недействительный трафик. Возможна фильтрация предложений по поисковому запросу. Начиная с версии 2.0 партнерского API статистику можно получить для конкретного предложения при указании в запросе его идентификатора из прайс-листа. Статистика по предложениям доступна за последние 30 дней, не включая текущий. Данные за вчерашний день доступны после 12:00 сегодня. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/stats/offers.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Количество запросов к ресурсу, которое возможно выполнить в течение суток, рассчитывается индивидуально и зависит от следующих показателей:   количество предложений.   Примечание. Количество предложений считается по данным за последние семь дней (не включая сегодня). Для новых магазинов, еще не разместивших предложения, ограничение равно 0 и пересчитывается на следующий день после размещения первых предложений.  
</details>

Пример:
```python
params = {
    "fromDate": "Date",  # required
    "feedId": "Int64",  # optional
    "fields": "Enum",  # optional
    "offerId": "String",  # optional
    "page": "Int32",  # optional
    "pageSize": "Int32",  # optional
    "toDate": "Date"  # optional
}
response = client.offers_stats(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "offersStats": {
        "fromOffer": "{int32}",
        "toOffer": "{int32}",
        "totalOffersCount": "{int32}",
        "offerStats": [
            {
                "clicks": "{int32}",
                "feedId": "{int64}",
                "offerId": "{string}",
                "spending": "{string}",
                "detailedStats": [
                    {
                        "clicks": "{int32}",
                        "spending": "{string}",
                        "type": "{enum}"
                    }
                ],
                "offerName": "{string}",
                "url": "{string}"
            }
        ]
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
  "offersStats":
  {
    "fromOffer": 1,
    "toOffer": 10,
    "totalOffersCount": 21739,
    "offerStats":
    [
      {
        "clicks": 474,
        "offerName": "PocketBook IQ 701, Dark Blue",
        "spending": 52.86
      },
      {
        "clicks": 204,
        "offerName": "Nokia N9 16 GB, Black",
        "spending": 174.04
      },
      {
        "clicks": 203,
        "offerName": "PocketBook IQ 701, Glossy White",
        "spending": 20.30
      },
      {
        "clicks": 194,
        "offerName": "Samsung GT-S5830 Galaxy Ace, Black",
        "spending": 161.02
      },
      {
        "clicks": 172,
        "offerName": "Samsung GT-i9100 Galaxy S II, Noble Black",
        "spending": 213.56
      },
      {
        "clicks": 165,
        "offerName": "Samsung GT-N7000 Galaxy Note",
        "spending": 81.67
      },
      {
        "clicks": 160,
        "offerName": "Samsung GT-i9001 Galaxy S Plus 8 GB, Metallic Black",
        "spending": 78.37
      },
      {
        "clicks": 96,
        "offerName": "Тамара Глоба "Самый полный гороскоп на 2012 год"",
        "spending": 10.17
      },
      {
        "clicks": 92,
        "offerName": "Маскарадный костюм "Дед Мороз", размер 48-54",
        "spending": 18.40
      },
      {
        "clicks": 88,
        "offerName": "LG P698 Optimus Net, Black",
        "spending": 16.26
      }
    ]
  }
}</pre>
</details>


## Поиск региона
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /regions Возвращает информацию о регионе, удовлетворяющем заданным в запросе условиям поиска.  Если найдено несколько регионов, удовлетворяющих условиям поиска, возвращается информация по каждому найденному региону (но не более десяти регионов) для возможности определения нужного региона по родительским регионам. Примечание. Метод доступен начиная с версии 1.2 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/regions.[format]?name={regionName} 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Для методов GET /regions, GET /regions/{regionId} и GET /regions/{regionId}/children действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество регионов, информация о которых запрошена при помощи этих методов (не более 100 000 регионов). Объем запросов к ресурсу, который возможно выполнить в течение суток, зависит от суммарного количества регионов. 
</details>

Пример:
```python
params = {
    "name": "String"  # required
}
response = client.geo_regions().get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "regions": [
        {
            "id": "{int64}",
            "name": "{string}",
            "type": "{enum}",
            "parent": {
                "id": "{int64}",
                "name": "{string}",
                "type": "{enum}",
                "parent": {}
            }
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "regions": [
        {
            "id": 11380,
            "name": "Ивановка",
            "type": "TOWN",
            "parent": {
                "id": 100295,
                "name": "Ивановский район",
                "type": "REPUBLIC_AREA",
                "parent": {
                    "id": 11375,
                    "name": "Амурская область",
                    "type": "REPUBLIC",
                    "parent": {
                        "id": 73,
                        "name": "Дальневосточный федеральный округ",
                        "type": "AREA",
                        "parent": {
                            "id": 225,
                            "name": "Россия",
                            "type": "COUNTRY"
                        }
                    }
                }
            }
        },
        {
            "id": 28630,
            "name": "Ивановка",
            "type": "TOWN",
            "parent": {
                "id": 24533,
                "name": "Ивановский район",
                "type": "REPUBLIC_AREA",
                "parent": {
                    "id": 20548,
                    "name": "Одесская область",
                    "type": "REPUBLIC",
                    "parent": {
                        "id": 20527,
                        "name": "Юг",
                        "type": "REGION",
                        "parent": {
                            "id": 187,
                            "name": "Украина",
                            "type": "COUNTRY"
                        }
                    }
                }
            }
        }
    ]
}</pre>
</details>


## Информация о регионе
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions-id.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /regions/{regionId} Возвращает информацию о регионе.  Примечание. Метод доступен начиная с версии 1.2 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/regions/{regionId}.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Для методов GET /regions, GET /regions/{regionId} и GET /regions/{regionId}/children действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество регионов, информация о которых запрошена при помощи этих методов (не более 100 000 регионов). Объем запросов к ресурсу, который возможно выполнить в течение суток, зависит от суммарного количества регионов. 
</details>

Пример:
```python
response = client.geo_region(regionId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "regions": [
        {
            "id": "{int64}",
            "name": "{string}",
            "type": "{enum}",
            "parent": {
                "id": "{int64}",
                "name": "{string}",
                "type": "{enum}",
                "parent": {}
            }
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "regions": [
        {
            "id": 213,
            "name": "Москва",
            "type": "CITY",
            "parent": {
                "id": 1,
                "name": "Москва и Московская область",
                "type": "REPUBLIC",
                "parent": {
                    "id": 3,
                    "name": "Центральный федеральный округ",
                    "type": "AREA",
                    "parent": {
                        "id": 225,
                        "name": "Россия",
                        "type": "COUNTRY"
                    }
                }
            }
        }
    ]
}</pre>
</details>


## Информация о дочерних регионах
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions-id-children.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /regions/{regionId}/children Возвращает информацию о регионах, являющихся дочерними по отношению к региону, идентификатор которого указан в запросе.  Примечание. Метод доступен начиная с версии 2.3 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/regions/{regionId}/children.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения Для методов GET /regions, GET /regions/{regionId} и GET /regions/{regionId}/children действует групповое ресурсное ограничение. Ограничение вводится на суммарное количество регионов, информация о которых запрошена при помощи этих методов (не более 100 000 регионов). Объем запросов к ресурсу, который возможно выполнить в течение суток, зависит от суммарного количества регионов. 
</details>

Пример:
```python
params = {
    "page": "Int32",  # optional
    "pageSize": "Int32"  # optional
}
response = client.region_children(regionId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "pager": {
        "currentPage": "{int32}",
        "from": "{int32}",
        "pagesCount": "{int32}",
        "pageSize": "{int32}",
        "to": "{int32}",
        "total": "{int32}"
    },
    "regions": {
        "id": "{int64}",
        "name": "{string}",
        "type": "{enum}",
        "children": [
            {
                "id": "{int64}",
                "name": "{string}",
                "type": "{enum}"
            }
        ],
        "parent": {
            "id": "{int64}",
            "name": "{string}",
            "type": "{enum}",
            "parent": {}
        }
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "pager": {
        "currentPage": 2,
        "from": 21,
        "pagesCount": 4,
        "pageSize": 20,
        "to": 40,
        "total": 75
    },
    "regions": {
        "id": 1,
        "name": "Москва и Московская область",
        "type": "REPUBLIC",
        "children": [
            {
                "id": 98580,
                "name": "Волоколамский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98581,
                "name": "Воскресенский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98582,
                "name": "Дмитровский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98589,
                "name": "Коломенский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98592,
                "name": "Лотошинский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98593,
                "name": "Луховицкий район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98594,
                "name": "Люберецкий район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98595,
                "name": "Можайский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98596,
                "name": "Мытищинский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98597,
                "name": "Наро-Фоминский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98598,
                "name": "Ногинский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98599,
                "name": "Одинцовский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98600,
                "name": "Озерский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98601,
                "name": "Орехово-Зуевский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98602,
                "name": "Павлово-Посадский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98603,
                "name": "Подольский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98604,
                "name": "Пушкинский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98605,
                "name": "Раменский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98606,
                "name": "Рузский район",
                "type": "REPUBLIC_AREA"
            },
            {
                "id": 98607,
                "name": "Ступинский район",
                "type": "REPUBLIC_AREA"
            }
        ],
        "parent": {
            "id": 3,
            "name": "Центральный федеральный округ",
            "type": "AREA",
            "parent": {
                "id": 225,
                "name": "Россия",
                "type": "COUNTRY"
            }
        }
    }
}</pre>
</details>


## Создание точки продаж
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-outlets.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/outlets Создает точку продаж магазина на Маркете.  URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/outlets.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В течение суток этим и другими запросами о точках продаж, кроме запроса GET /delivery/services, можно получить и изменить информацию об определенном суммарном количестве точек продаж. Оно зависит от количества точек продаж магазина. 
</details>

Пример:
```python
body = {
    "name": "{string}",
    "type": "{enum}",
    "coords": "{string}",
    "isMain": "{boolean}",
    "shopOutletCode": "{string}",
    "visibility": "{enum}",
    "isBookNow": "{boolean}",
    "address": {
        "regionId": "{int64}",
        "street": "{string}",
        "number": "{string}",
        "building": "{string}",
        "estate": "{string}",
        "block": "{string}",
        "additional": "{string}",
        "km": "{integer}"
    },
    "phones": [
        "{string}"
    ],
    "workingSchedule": {
        "workInHoliday": "{boolean}",
        "scheduleItems": [
            {
                "startDay": "{enum}",
                "endDay": "{enum}",
                "startTime": "{string}",
                "endTime": "{string}"
            }
        ]
    },
    "deliveryRules": [
        {
            "cost": "{double}",
            "minDeliveryDays": "{int32}",
            "maxDeliveryDays": "{int32}",
            "deliveryServiceId": "{int64}",
            "orderBefore": "{int32}",
            "priceFreePickup": "{double}",
            "unspecifiedDeliveryInterval": "{boolean}"
        }
    ],
    "emails": [
        "{string}"
    ]
}
response = client.outlets(campaignId=...).post(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "result": {
        "id": "{int64}"
    },
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "result": {
        "id": 171819
    },
    "status": "OK"
}</pre>
</details>


## Изменение информации о точке продаж
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/put-campaigns-id-outlets-id.html) ресурса

<details>
<summary>Описание</summary>
Описание PUT /campaigns/{campaignId}/outlets/{outletId} Изменяет информацию о точке продаж магазина на Маркете.  URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/outlets/{outletId}.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В течение суток этим и другими запросами о точках продаж, кроме запроса GET /delivery/services, можно получить и изменить информацию об определенном суммарном количестве точек продаж. Оно зависит от количества точек продаж магазина. 
</details>

Пример:
```python
body = {
    "name": "{string}",
    "type": "{enum}",
    "coords": "{string}",
    "isMain": "{boolean}",
    "shopOutletCode": "{string}",
    "visibility": "{enum}",
    "isBookNow": "{boolean}",
    "address": {
        "regionId": "{int64}",
        "street": "{string}",
        "number": "{string}",
        "building": "{string}",
        "estate": "{string}",
        "block": "{string}",
        "additional": "{string}",
        "km": "{integer}"
    },
    "phones": [
        "{string}"
    ],
    "workingSchedule": {
        "workInHoliday": "{boolean}",
        "scheduleItems": [
            {
                "startDay": "{enum}",
                "endDay": "{enum}",
                "startTime": "{string}",
                "endTime": "{string}"
            }
        ]
    },
    "deliveryRules": [
        {
            "cost": "{double}",
            "minDeliveryDays": "{int32}",
            "maxDeliveryDays": "{int32}",
            "deliveryServiceId": "{int64}",
            "orderBefore": "{int32}",
            "priceFreePickup": "{double}",
            "unspecifiedDeliveryInterval": "{boolean}"
        }
    ],
    "emails": [
        "{string}"
    ]
}
response = client.outlet(campaignId=..., outletId=...).put(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>


## Удаление точки продаж
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/delete-campaigns-id-outlets-id.html) ресурса

<details>
<summary>Описание</summary>
Описание DELETE /campaigns/{campaignId}/outlets/{outletId} Удаляет точку продаж магазина на Маркете.  URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/outlets/{outletId}.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В течение суток этим и другими запросами о точках продаж, кроме запроса GET /delivery/services, можно получить и изменить информацию об определенном суммарном количестве точек продаж. Оно зависит от количества точек продаж магазина. 
</details>

Пример:
```python
response = client.outlet(campaignId=..., outletId=...).delete()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "status": "{enum}"
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>


## Информация о точках продаж
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-outlets.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/outlets Возвращает список точек продаж магазина.  Примечание. Метод доступен начиная с версии 2.4 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/outlets.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В течение суток этим и другими запросами о точках продаж, кроме запроса GET /delivery/services, можно получить и изменить информацию об определенном суммарном количестве точек продаж. Оно зависит от количества точек продаж магазина. 
</details>

Пример:
```python
params = {
    "page_token": "String",  # optional
    "limit": "Int32",  # optional
    "page": "Int32",  # optional
    "pageSize": "Int32",  # optional
    "region_id": "Int64",  # optional
    "shop_outlet_code": "String",  # optional
    "regionId": "Int64"  # optional
}
response = client.outlets(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "outlets": [
        {
            "coords": "{string}",
            "id": "{int64}",
            "isMain": "{boolean}",
            "name": "{string}",
            "reason": "{string}",
            "shopOutletCode": "{string}",
            "status": "{enum}",
            "type": "{enum}",
            "visibility": "{enum}",
            "isBookNow": "{boolean}",
            "shopOutletId": "{string}",
            "workingTime": "{string}",
            "address": {
                "regionId": "{int64}",
                "street": "{string}",
                "number": "{string}",
                "building": "{string}",
                "estate": "{string}",
                "block": "{string}",
                "additional": "{string}",
                "km": "{integer}",
                "city": "{string}"
            },
            "deliveryRules": [
                {
                    "cost": "{double}",
                    "minDeliveryDays": "{int32}",
                    "maxDeliveryDays": "{int32}",
                    "deliveryServiceId": "{int64}",
                    "orderBefore": "{int32}",
                    "priceFreePickup": "{double}",
                    "unspecifiedDeliveryInterval": "{boolean}",
                    "dateSwitchHour": "{int32}",
                    "priceFrom": "{double}",
                    "priceTo": "{double}",
                    "shipperHumanReadableId": "{string}",
                    "shipperId": "{int64}",
                    "shipperName": "{string}",
                    "workInHoliday": "{boolean}"
                }
            ],
            "emails": [
                "{string}"
            ],
            "phones": [
                "{string}"
            ],
            "region": {
                "id": "{int64}",
                "name": "{string}",
                "type": "{enum}",
                "parent": {
                    "id": "{int64}",
                    "name": "{string}",
                    "type": "{enum}",
                    "parent": {}
                }
            },
            "workingSchedule": {
                "workInHoliday": "{boolean}",
                "scheduleItems": [
                    {
                        "startDay": "{enum}",
                        "endDay": "{enum}",
                        "startTime": "{string}",
                        "endTime": "{string}"
                    }
                ]
            }
        }
    ],
    "paging": {
        "nextPageToken": "{string}"
    },
    "pager": {
        "currentPage": "{int32}",
        "from": "{int32}",
        "pageSize": "{int32}",
        "to": "{int32}"
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "outlets": [
        {
            "coords": "20.4522144, 54.7104264",
            "id": 171819,
            "isMain": false,
            "name": "На Озёрной",
            "shopOutletCode": "419",
            "status": "AT_MODERATION",
            "type": "DEPOT",
            "visibility": "VISIBLE",
            "address": {
                "regionId": 22,
                "street": "ОЗЕРНАЯ",
                "number": "20А"
            },
            "deliveryRules": [
                {
                    "cost": 285,
                    "minDeliveryDays": 19,
                    "maxDeliveryDays": 30,
                    "deliveryServiceId": 100,
                    "orderBefore": 24,
                    "priceFreePickup": 120,
                    "unspecifiedDeliveryInterval": true
                }
            ],
            "emails": [
                "example-shop@yandex.ru"
            ],
            "phones": [
                "+7 (401) 212-22-32 #123"
            ],
            "region": {
                "id": 22,
                "name": "Калининград",
                "type": "CITY",
                "parent": {
                    "id": 121022,
                    "name": "Городской округ Калининград",
                    "type": "REPUBLIC_AREA",
                    "parent": {
                        "id": 10857,
                        "name": "Калининградская область",
                        "type": "REPUBLIC",
                        "parent": {
                            "id": 17,
                            "name": "Северо-Западный федеральный округ",
                            "type": "COUNTRY_DISTRICT",
                            "parent": {
                                "id": 225,
                                "name": "Россия",
                                "type": "COUNTRY"
                            }
                        }
                    }
                }
            },
            "workingSchedule": {
                "workInHoliday": false,
                "scheduleItems": [
                    {
                        "startDay": "MONDAY",
                        "endDay": "FRIDAY",
                        "startTime": "09:00",
                        "endTime": "19:00"
                    },
                    {
                        "startDay": "SATURDAY",
                        "endDay": "SATURDAY",
                        "startTime": "10:00",
                        "endTime": "16:00"
                    }
                ]
            }
        }
    ],
    "paging": {
        "nextPageToken": "baYYHyRuNfRhPyTr"
    },
    "pager": {
        "from": 1,
        "to": 1,
        "currentPage": 1,
        "pageSize": 1
    }
}</pre>
</details>


## Информация о точке продаж
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-outlets-id.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/outlets/{outletId} Возвращает информацию о точках продаж магазина.  Примечание. Метод доступен начиная с версии 2.4 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/outlets/{outletId}.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В течение суток этим и другими запросами о точках продаж, кроме запроса GET /delivery/services, можно получить и изменить информацию об определенном суммарном количестве точек продаж. Оно зависит от количества точек продаж магазина. 
</details>

Пример:
```python
response = client.outlet(campaignId=..., outletId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "coords": "{string}",
    "id": "{int64}",
    "isMain": "{boolean}",
    "name": "{string}",
    "reason": "{string}",
    "shopOutletCode": "{string}",
    "status": "{enum}",
    "type": "{enum}",
    "visibility": "{enum}",
    "isBookNow": "{boolean}",
    "shopOutletId": "{string}",
    "workingTime": "{string}",
    "address": {
        "regionId": "{int64}",
        "street": "{string}",
        "number": "{string}",
        "building": "{string}",
        "estate": "{string}",
        "block": "{string}",
        "additional": "{string}",
        "km": "{integer}",
        "city": "{string}"
    },
    "deliveryRules": [
        {
            "cost": "{double}",
            "minDeliveryDays": "{int32}",
            "maxDeliveryDays": "{int32}",
            "deliveryServiceId": "{int64}",
            "orderBefore": "{int32}",
            "priceFreePickup": "{double}",
            "unspecifiedDeliveryInterval": "{boolean}",
            "dateSwitchHour": "{int32}",
            "priceFrom": "{double}",
            "priceTo": "{double}",
            "shipperHumanReadableId": "{string}",
            "shipperId": "{int64}",
            "shipperName": "{string}",
            "workInHoliday": "{boolean}"
        }
    ],
    "emails": [
        "{string}"
    ],
    "phones": [
        "{string}"
    ],
    "region": {
        "id": "{int64}",
        "name": "{string}",
        "type": "{enum}",
        "parent": {
            "id": "{int64}",
            "name": "{string}",
            "type": "{enum}",
            "parent": {}
        }
    },
    "workingSchedule": {
        "workInHoliday": "{boolean}",
        "scheduleItems": [
            {
                "startDay": "{enum}",
                "endDay": "{enum}",
                "startTime": "{string}",
                "endTime": "{string}"
            }
        ]
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "coords": "20.4522144, 54.7104264",
    "id": 171819,
    "isMain": false,
    "name": "На Озёрной",
    "shopOutletCode": "419",
    "status": "AT_MODERATION",
    "type": "DEPOT",
    "visibility": "VISIBLE",
    "address": {
        "regionId": 22,
        "street": "ОЗЕРНАЯ",
        "number": "20А"
    },
    "deliveryRules": [
        {
            "cost": 285,
            "minDeliveryDays": 19,
            "maxDeliveryDays": 30,
            "deliveryServiceId": 100,
            "orderBefore": 24,
            "priceFreePickup": 120,
            "unspecifiedDeliveryInterval": true
        }
    ],
    "emails": [
        "example-shop@yandex.ru"
    ],
    "phones": [
        "+7 (401) 212-22-32 #123"
    ],
    "region": {
        "id": 22,
        "name": "Калининград",
        "type": "CITY",
        "parent": {
            "id": 121022,
            "name": "Городской округ Калининград",
            "type": "REPUBLIC_AREA",
            "parent": {
                "id": 10857,
                "name": "Калининградская область",
                "type": "REPUBLIC",
                "parent": {
                    "id": 17,
                    "name": "Северо-Западный федеральный округ",
                    "type": "COUNTRY_DISTRICT",
                    "parent": {
                        "id": 225,
                        "name": "Россия",
                        "type": "COUNTRY"
                    }
                }
            }
        }
    },
    "workingSchedule": {
        "workInHoliday": false,
        "scheduleItems": [
            {
                "startDay": "MONDAY",
                "endDay": "FRIDAY",
                "startTime": "09:00",
                "endTime": "19:00"
            },
            {
                "startDay": "SATURDAY",
                "endDay": "SATURDAY",
                "startTime": "10:00",
                "endTime": "16:00"
            }
        ]
    }
}</pre>
</details>


## Создание и изменение лицензий для точек продаж
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-outlets-licenses.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/outlets/licenses Передает информацию о новых и существующих лицензиях для точек продаж. Поддерживаются только лицензии на розничную продажу алкоголя. Чтобы размещать алкогольную продукцию на Маркете, надо также прислать гарантийное письмо (если вы еще не делали этого раньше) и правильно оформить предложения в прайс-листе. Подробнее см. в разделе Как разместить на Маркете алкогольную продукцию Справки Маркета для модели ADV. Информация о лицензиях проходит проверку. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/outlets/licenses.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В течение суток этим и другими запросами о точках продаж, кроме запроса GET /delivery/services, можно получить и изменить информацию об определенном суммарном количестве точек продаж. Оно зависит от количества точек продаж магазина. 
</details>

Пример:
```python
body = {
    "licenses": [
        {
            "id": "{int64}",
            "outletId": "{int64}",
            "licenseType": "{enum}",
            "number": "{string}",
            "dateOfIssue": "{date}",
            "dateOfExpiry": "{date}"
        }
    ]
}
response = client.outlets_licenses(campaignId=...).post(data=body)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "status": "{enum}",
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>


## Удаление лицензий для точек продаж
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/delete-campaigns-id-outlets-licenses.html) ресурса

<details>
<summary>Описание</summary>
Описание DELETE /campaigns/{campaignId}/outlets/licenses Удаляет информацию о лицензиях для точек продаж. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/outlets/licenses.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В течение суток этим и другими запросами о точках продаж, кроме запроса GET /delivery/services, можно получить и изменить информацию об определенном суммарном количестве точек продаж. Оно зависит от количества точек продаж магазина. 
</details>

Пример:
```python
params = {
    "ids": "String"  # required
}
response = client.outlets_licenses(campaignId=...).delete(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "status": "{enum}",
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>


## Информация о лицензиях для точек продаж
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-outlets-licenses.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/outlets/licenses Возвращает информацию о лицензиях для точек продаж. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/outlets/licenses.[format] 
</details>

<details>
<summary>Ограничения</summary>
Ограничения В течение суток этим и другими запросами о точках продаж, кроме запроса GET /delivery/services, можно получить и изменить информацию об определенном суммарном количестве точек продаж. Оно зависит от количества точек продаж магазина. 
</details>

Пример:
```python
params = {
    "outletIds": "String",  # required
    "ids": "String"  # required
}
response = client.outlets_licenses(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "status": "{enum}",
    "result": {
        "licenses": [
            {
                "id": "{int64}",
                "outletId": "{int64}",
                "licenseType": "{enum}",
                "number": "{string}",
                "dateOfIssue": "{date}",
                "dateOfExpiry": "{date}",
                "checkStatus": "{enum}",
                "comment": "{string}"
            }
        ]
    },
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ]
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK",
    "result": {
        "licenses": [
            {
                "id": 14,
                "outletId": 171819,
                "licenseType": "ALCOHOL",
                "number": "01АБВ23456789",
                "dateOfIssue": "2017-11-13T00:00:00+03:00",
                "dateOfExpiry": "2022-11-20T00:00:00+03:00",
                "checkStatus": "SUCCESS"
            }
        ]
    }
}</pre>
</details>


## Справочник служб доставки
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-delivery-services.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /delivery/services Возвращает справочник служб доставки: идентификаторы и наименования. URL ресурса: https://api.partner.market.yandex.ru/v2/delivery/services.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.delivery_services_dictionary().get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "result": {
        "deliveryService": [
            {
                "id": "{int64}",
                "name": "{string}"
            }
        ]
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "result": {
        "deliveryService": [
            {
                "id": 128,
                "name": "Hongkong Post"
            }
        ]
    }
}</pre>
</details>


## Информация об ошибках магазина
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-tickets.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/quality/tickets Возвращает данные о текущих ошибках магазина, выявленных службой контроля качества Маркета. Примечание. Метод доступен начиная с версии 2.7 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/quality/tickets.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
params = {
    "actualType": "Enum"  # optional
}
response = client.quality_tickets(campaignId=...).get(params=params)
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "result": {
        "tickets": [
            {
                "checkMethod": "{int8}",
                "errorCode": "{int32}",
                "errorFoundTime": "{date}",
                "errorText": "{string}",
                "feedTime": "{date}",
                "offerURL": "{string}",
                "orderId": "{string}",
                "status": "{int8}",
                "ticketId": "{int64}"
            }
        ]
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "result": {
        "tickets": [
            {
                "checkMethod": 1,
                "errorCode": 3,
                "errorFoundTime": "2017-06-05T00:42:42",
                "errorText": "Реальная цена выше",
                "feedTime": "2015-12-27T00:42:42",
                "offerURL": "http://shop.seller.ru/products/56789",
                "status": 1,
                "ticketId": 1011121
            }
        ]
    }
}</pre>
</details>


## Информация об ошибке магазина
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-tickets-id.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/quality/tickets/{ticketId} Возвращает данные об ошибке магазина, выявленной службой контроля качества Маркета.  Примечание. Метод доступен начиная с версии 2.7 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/quality/tickets/{ticketId}.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.quality_ticket(campaignId=..., ticketId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "result": {
        "tickets": [
            {
                "checkMethod": "{int8}",
                "errorCode": "{int32}",
                "errorFoundTime": "{date}",
                "errorText": "{string}",
                "feedTime": "{date}",
                "offerURL": "{string}",
                "orderId": "{string}",
                "status": "{int8}",
                "ticketId": "{int64}"
            }
        ]
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "result": {
        "tickets": [
            {
                "checkMethod": 1,
                "errorCode": 3,
                "errorFoundTime": "2016-01-05T01:44:30",
                "errorText": "Реальная цена выше",
                "feedTime": "2015-12-27T05:36:17",
                "offerURL": "http://shop.seller.ru/products/10087",
                "status": 1,
                "ticketId": 2799068
            }
        ]
    }
}</pre>
</details>


## Отчет по качеству
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-report.html) ресурса

<details>
<summary>Описание</summary>
Описание GET /campaigns/{campaignId}/quality/report Возвращает отчет по качеству работы магазина, составленный службой контроля качества Маркета. Отчет содержит всю информацию о качестве работы вашего магазина, результатах регулярных проверок, выявленных ошибках и проблемах. Примечание. Метод доступен начиная с версии 2.7 партнерского API. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/quality/report.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.quality_report(campaignId=...).get()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "result": {
        "actualErrorCount": "{int32}",
        "ageBonus": "{float}",
        "archiveErrorCount": "{int32}",
        "checkCount": "{int32}",
        "cloneCount": "{int32}",
        "errorCount": "{int32}",
        "gradeCount": "{int32}",
        "marketRating": "{float}",
        "modificationTime": "{date}",
        "opinionCount": "{int32}",
        "opinionUrl": "{string}",
        "qualityBonus": "{float}",
        "qualityServiceRating": "{float}"
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "result": {
        "actualErrorCount": 5,
        "ageBonus": 1,
        "archiveErrorCount": 5,
        "checkCount": 8,
        "cloneCount": 1,
        "errorCount": 8,
        "gradeCount": 109,
        "marketRating": 0.74,
        "modificationTime": "2016-03-21T00:00:00",
        "opinionCount": 717,
        "opinionUrl": "https://partner.market.yandex.ru/shop-opinions.xml?id...",
        "qualityBonus": 0,
        "qualityServiceRating": 0.1
    }
}</pre>
</details>


## Сообщить что ошибка исправлена
Официальная [документация](https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-quality-tickets-id-fix.html) ресурса

<details>
<summary>Описание</summary>
Описание POST /campaigns/{campaignId}/quality/tickets/{ticketId}/fix Сообщает службе контроля качества Маркета, что ошибка исправлена. Примечание. Метод доступен начиная с версии 2.7 партнерского API Яндекс.Маркета. URL ресурса: https://api.partner.market.yandex.ru/v2/campaigns/{campaignId}/tickets/{ticketId}/fix.[format] 
</details>

<details>
<summary>Ограничения</summary>
None
</details>

Пример:
```python
response = client.quality_ticket_fix(campaignId=..., ticketId=...).post()
print(response.data)
```

<details>
<summary>Возвращаемые данные</summary>
<pre>{
    "errors": [
        {
            "code": "{enum}",
            "message": "{string}"
        }
    ],
    "status": "{enum}",
    "result": {
        "status": "{enum}"
    }
}</pre>
</details>

<details>
<summary>Пример возвращаемых данных</summary>
<pre>{
    "status": "OK"
}</pre>
</details>
