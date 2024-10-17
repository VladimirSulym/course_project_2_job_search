from src.search import vacancies_search


def test_vacancies_search(vacancies_for_test):
    assert vacancies_search(vacancies_for_test, "Среднее профессиональное")[0].vacancy.get("id") == "108123109"
    assert vacancies_search(vacancies_for_test, "250000")[0].vacancy.get("id") == "107642936"
    assert vacancies_search([], "профессиональное") == []
    assert vacancies_search(vacancies_for_test, "") == vacancies_for_test
    assert vacancies_search(vacancies_for_test, None) == vacancies_for_test
    assert vacancies_search(None, None) == []
