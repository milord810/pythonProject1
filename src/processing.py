states = (
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
)


def filter_by_state(states: list) -> list[dict]:
    """Функция принимает список словарей и опционально значение для ключа
    state"""
    return [state for state in states if state["state"] == "EXECUTED"]


def sort_by_date(states: tuple) -> list[dict]:
    """Функция принимает список словарей и необязательный параметр, задающий порядок сортировки"""
    sorted_states = sorted(states, key=lambda states: states["date"], reverse=True)
    return sorted_states
