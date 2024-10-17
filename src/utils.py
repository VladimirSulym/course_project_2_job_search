import json
import logging
import os

from config import DATA_PATH, LOG_FORMAT, LOG_LEVEL

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(LOG_FORMAT)
logger.addHandler(console_handler)
logger.setLevel(LOG_LEVEL)


def get_len_base(file_name: str) -> int:
    """Функция считает количество вакансий в локальной базе."""
    path = os.path.join(DATA_PATH, file_name)
    try:
        with open(path, "r") as f:
            return len(json.load(f))
    except FileNotFoundError:
        logger.error(f"Файл с базой вакансий не найден: {path}")
        return 0


def bubble_sort(user_list: list) -> list:
    """Функция сортировки пузырьком, сортирует вакансии по зарплате"""
    n = len(user_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if user_list[j] < user_list[j + 1]:
                user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
    return user_list


def bubble_sort_area(user_list: list) -> list:
    """Функция сортировки пузырьком, сортирует вакансии по региону"""
    n = len(user_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if user_list[j].vacancy.get("area") > user_list[j + 1].vacancy.get("area"):
                user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
    return user_list


def filter_by_salary_range(vacancies: list, min_salary: str = "0", max__salary: str = "0") -> list:
    """Функция фильтрует вакансии по заданному диапазону ЗП"""
    result_lisr = []
    logger.debug(min_salary)
    logger.debug(max__salary)
    for vacancy in vacancies:
        if int(min_salary) <= int(vacancy.vacancy.get("salary").get("from")) <= int(max__salary):
            result_lisr.append(vacancy)
    return result_lisr


# if __name__ == "__main__":
#     print(bubble_sort([3, 1, 2, 5, 4]))
