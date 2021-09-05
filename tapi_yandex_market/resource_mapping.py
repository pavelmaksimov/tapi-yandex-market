RESOURCE_MAPPING_V2 = {
    "campaigns": {
        "resource": "v2/campaigns",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns.html",
        "key": "campaigns",
    },
    "campaign": {
        "resource": "v2/campaigns/{campaignId}",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id.html",
        "key": "campaign",
    },
    "logins": {
        "resource": "v2/campaigns/{campaignId}/logins",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-logins.html",
        "key": "logins",
    },
    "campaigns_by_login": {
        "resource": "v2/campaigns/by_login/{login}",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-by-login.html",
        "key": "campaigns",
    },
    "settings": {
        "resource": "v2/campaigns/{campaignId}/settings",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-settings.html",
        "key": "settings",
    },
    "region": {
        "resource": "v2/campaigns/{campaignId}/region",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-region.html",
        "key": "region",
    },
    "feedback_updates": {
        "resource": "v2/campaigns/{campaignId}/feedback/updates",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feedback-updates.html",
        "key": ["result", "feedbackList"],
    },
    "offers": {
        "resource": "v2/campaigns/{campaignId}/offers",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offers.html",
        "key": "offers",
    },
    "all_offers": {
        "resource": "v2/campaigns/{campaignId}/offers/all",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offers-all.html",
        "key": "offers",
    },
    "feeds": {
        "resource": "v2/campaigns/{campaignId}/feeds",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds.html",
        "key": "feeds",
    },
    "feed": {
        "resource": "v2/campaigns/{campaignId}/feeds/{feedId}",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id.html",
        "key": "feed",
    },
    "feed_categories": {
        "resource": "v2/campaigns/{campaignId}/feeds/{feedId}/categories",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id-categories.html",
        "key": "categories",
    },
    "all_feeds_categories": {
        "resource": "v2/campaigns/{campaignId}/feeds/categories",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-categories.html",
        "key": "categories",
    },
    "feed_index_logs": {
        "resource": "v2/campaigns/{campaignId}/feeds/{feedId}/index-logs",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-feeds-id-index-logs.html",
        "key": "result",
    },
    "feed_parameters": {
        "resource": "v2/campaigns/{campaignId}/feeds/{feedId}/params",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-feeds-id-params.html",
        "key": "parameters",
    },
    "feed_refresh": {
        "resource": "v2/campaigns/{campaignId}/feeds/{feedId}/refresh",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-feeds-id-refresh.html",
    },
    "hidden_offers": {
        "resource": "v2/campaigns/{campaignId}/hidden-offers",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-hidden-offers.html",
        "key": ["result", "hiddenOffers"],
    },
    "update_offer_prices": {
        "resource": "v2/campaigns/{campaignId}/offer-prices/updates",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-offer-prices-updates.html",
        "key": "offers",
    },
    "remove_offer_prices": {
        "resource": "v2/campaigns/{campaignId}/offer-prices/removals",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-offer-prices-removals.html",
    },
    "offer-prices": {
        "resource": "v2/campaigns/{campaignId}/offer-prices",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-offer-prices.html",
        "key": ["result", "offers"],
    },
    "model": {
        "resource": "v2/models/{modelId}",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-models-id.html",
        "key": "models",
    },
    "models": {
        "resource": "v2/models",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-models.html",
        "key": "models",
    },
    "model_offers": {
        "resource": "v2/models/{modelId}/offers",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-models-id-offers.html",
    },
    "models_offers": {
        "resource": "v2/models/offers",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-models-offers.html",
        "key": "models",
    },
    "bids": {
        "resource": "v2/campaigns/{campaignId}/auction/bids",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-bids.html",
        "key": "bids",
    },
    "bid_recommendations": {
        "resource": "v2/campaigns/{campaignId}/auction/recommendations/bids",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-auction-recommendations-bids.html",
        "key": "offers",
    },
    "top_market_search": {
        "resource": "v2/campaigns/{campaignId}/bids/recommended/top/market-search",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-bids-recommended-top-market-search.html",
        "key": "offers",
    },
    "bids_settings": {
        "resource": "v2/campaigns/{campaignId}/bids/settings",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-bids-settings.html",
        "key": "settings",
    },
    "balance": {
        "resource": "v2/campaigns/{campaignId}/balance",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-balance.html",
        "key": "balance",
    },
    "invoice_pay_preview": {
        "resource": "v2/campaigns/{campaignId}/invoice/paypreview",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-invoice-paypreview.html",
        "key": "result",
    },
    "invoice": {
        "resource": "v2/invoice",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-invoice.html",
    },
    "campaign_invoice": {
        "resource": "v2/campaigns/{campaignId}/invoices/{invoiceId}",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-invoices-id.html",
    },
    "stats": {
        "resource": "v2/campaigns/{campaignId}/stats/main",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html",
        "key": "mainStats",
    },
    "daily_stats": {
        "resource": "v2/campaigns/{campaignId}/stats/main-daily",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html#examples__main-daily",
        "key": "mainStats",
    },
    "weekly_stats": {
        "resource": "v2/campaigns/{campaignId}/stats/main-weekly",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html#examples__main-weekly",
        "key": "mainStats",
    },
    "monthly_stats": {
        "resource": "v2/campaigns/{campaignId}/stats/main-monthly",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-main.html#examples__main-monthly",
        "key": "mainStats",
    },
    "offers_stats": {
        "resource": "v2/campaigns/{campaignId}/stats/offers",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-stats-offers.html",
        "key": ["offersStats", "offerStats"],
    },
    "geo_regions": {
        "resource": "v2/regions",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions.html",
        "key": "regions",
    },
    "geo_region": {
        "resource": "v2/regions/{regionId}",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions-id.html",
        "key": "regions",
    },
    "region_children": {
        "resource": "v2/regions/{regionId}/children",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-regions-id-children.html",
        "key": "regions",
    },
    "outlets": {
        "resource": "v2/campaigns/{campaignId}/outlets",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-outlets.html",
    },
    "outlet": {
        "resource": "v2/campaigns/{campaignId}/outlets/{outletId}",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/put-campaigns-id-outlets-id.html",
    },
    "campaign_outlets": {
        "resource": "v2/campaigns/{campaignId}/outlets",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-outlets.html",
        "key": "outlets",
    },
    "outlets_licenses": {
        "resource": "v2/campaigns/{campaignId}/outlets/licenses",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-outlets-licenses.html",
        "key": "licenses",
    },
    "delivery_services_dictionary": {
        "resource": "v2/delivery/services",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-delivery-services.html",
        "key": ["result", "deliveryService"],
    },
    "quality_tickets": {
        "resource": "v2/campaigns/{campaignId}/quality/tickets",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-tickets.html",
        "key": ["result", "tickets"],
    },
    "quality_ticket": {
        "resource": "v2/campaigns/{campaignId}/quality/tickets/{ticketId}",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-tickets-id.html",
        "key": ["result", "tickets"],
    },
    "quality_report": {
        "resource": "v2/campaigns/{campaignId}/quality/report",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/get-campaigns-id-quality-report.html",
        "key": "result",
    },
    "quality_ticket_fix": {
        "resource": "v2/campaigns/{campaignId}/quality/tickets/{ticketId}/fix",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-quality-tickets-id-fix.html",
        "key": "result",
    },
    "quality_check": {
        "resource": "v2/campaigns/{campaignId}/quality/check",
        "docs": "https://yandex.ru/dev/market/partner/doc/dg/reference/post-campaigns-id-quality-check.html",
        "key": "result",
    },
}
