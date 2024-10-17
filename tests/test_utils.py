from unittest.mock import patch

from src.utils import (bubble_sort, bubble_sort_area, filter_by_salary_range,
                       get_len_base)


@patch("json.load")
def test_get_len_base(mock_load):
    mock_load.return_value = ["a", "b", "c"]
    assert get_len_base("a") == 0


@patch("builtins.open")
@patch("json.load")
def test_get_len_base_1(mock_load, mock_open):
    mock_open.return_value = mock_open()
    mock_load.return_value = ["a", "b", "c"]
    assert get_len_base("a") == 3


def test_bubble_sort():
    assert bubble_sort([2, 3, 1, 4, 5]) == [5, 4, 3, 2, 1]


def test_bubble_sort_area(vacancies_for_test):
    assert bubble_sort_area(vacancies_for_test)[0].vacancy.get("id") == "108123109"


def test_filter_by_salary_range(vacancies_for_test):
    assert filter_by_salary_range(vacancies_for_test) == []


def test_filter_by_salary_range_1(vacancies_for_test):
    assert filter_by_salary_range(vacancies_for_test, 100, 100000000) == vacancies_for_test
