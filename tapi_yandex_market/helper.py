from typing import List, Union, Any, Dict

NewNameT = str


def iter_flatten_stats_row(
    rows: List[Dict[str, Union[dict, Any]]], **new_field_names: NewNameT
) -> List[Dict[str, Any]]:
    """
    Example transform:

    :param rows:
        [{'clicks': 295,
        'date': '2021-08-30',
         'detailedStats': [{'clicks': 273, 'shows': '1225793', 'spending': 31.19, 'type': 'mobile'}],
        'placeGroup': 3,
        'shows': '1525855',
        'spending': 33.74}]

    :return: [{'clicks': 295,
        'date': '2021-08-30',
        'placeGroup': 3,
        'shows': '1525855',
        'spending': 33.74,
        'clicksMobile': 273,
        'showsMobile': '1225793',
        'spendingMobile': 31.19}]



    """
    for row in rows:
        for detailed_stats in row.pop("detailedStats", []):
            type_stats = detailed_stats.pop("type")
            for metrika in list(detailed_stats.keys()):
                metrika_name = metrika + type_stats.title()
                metrika_name = new_field_names.get(metrika_name, metrika_name)
                row[metrika_name] = detailed_stats.pop(metrika)
        yield row
