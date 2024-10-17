from src.vacancy import Vacancy


def test_vacancy(test_vacancy):
    assert isinstance(test_vacancy, Vacancy)


def test_str_vacancy(test_vacancy):
    assert isinstance(str(test_vacancy), str)


def test_lt_vacancy(test_vacancy):
    assert not test_vacancy < test_vacancy


def test_gt_vacancy(test_vacancy):
    assert not test_vacancy > test_vacancy
