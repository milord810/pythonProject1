import pytest

from src.processing import filter_by_state, sort_by_date, states

@pytest.fixture
def test_filter_by_state(states, states_executed, states_canceled):
    """Функция тестирования фильтра по значению ключа 'state'"""
    assert filter_by_state(states) == states_executed
    assert filter_by_state(states, state="CANCELED") == states_canceled


def test_sort_by_date(states, states_date):
    """Функция тестирования сортировки по дате"""
    assert sort_by_date(states) == states_date