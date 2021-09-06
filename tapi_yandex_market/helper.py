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
            for field_name_detailed_stats in list(detailed_stats.keys()):
                field_name = field_name_detailed_stats + type_stats.title()
                row[field_name] = detailed_stats.pop(field_name_detailed_stats)

        for field_name in list(row.keys()):
            new_field_name = new_field_names.get(field_name, field_name)
            row[new_field_name] = row.pop(field_name)

        yield row
