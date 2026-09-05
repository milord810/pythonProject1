import pytest

from src.processing import filter_by_state, sort_by_date, states
from tests.conftest import transactions, transactions_executed, transactions_canceled


def test_filter_by_state(transactions, transactions_executed, transactions_canceled):
    """Функция тестирования фильтра по значению ключа 'state'"""
    assert filter_by_state(transactions, target="EXECUTED") == transactions_executed
    assert filter_by_state(transactions, target="CANCELED") == transactions_canceled


def test_sort_by_date(transactions, transactions_date):
    """Функция тестирования сортировки по дате"""
    assert sort_by_date(transactions) == transactions_date
