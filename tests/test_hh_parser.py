from unittest.mock import patch


@patch("requests.get")
def test_load_vacancies(mock_get, hh_loader):
    mock_get.return_value.json.return_value = {"found": 100, "page": 0, "pages": 30, "items": {}}
    assert hh_loader.load_vacancies("инженер") == []


@patch("requests.get")
def test_load_vacancies_1(mock_get, hh_loader):
    mock_get.return_value.json.return_value = {"found": 100, "page": 0, "pages": 15, "items": {}}
    assert hh_loader.load_vacancies("инженер") == []
