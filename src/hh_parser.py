import logging
from abc import ABC, abstractmethod

import requests

from config import LOG_FORMAT, LOG_LEVEL

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(LOG_FORMAT)
logger.addHandler(console_handler)
logger.setLevel(LOG_LEVEL)


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        self.vacancies_cont = 0

    def load_vacancies(self, keyword):
        """Функция получает на вход слово для поиска на сайте hh и список словарей с вакансиями"""
        self.params["text"] = keyword
        pages_count = 20
        while self.params.get("page") < pages_count:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            logger.debug(f"Статус код - {response.status_code}")
            logger.debug(f"Количество найденных вакансий {response.json()['found']}")
            self.vacancies_cont = response.json()["found"]
            if response.json()["pages"] < pages_count:
                logger.debug(f"Кол-во страниц {response.json()['pages']} - меньше 20")
                pages_count = response.json()["pages"]
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
        return self.vacancies


# if __name__ == '__main__':
#     test = HH()
#     test1 = test.load_vacancies('микробиолог')
#     print(test1[0].get('id'))
#     print(test1[1].get('id'))
#     print(test1[100].get('id'))
#     print(test1[101].get('id'))
#     print(test.vacancies_cont)
