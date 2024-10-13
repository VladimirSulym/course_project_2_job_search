class Vacancy:
    def __init__(self, data):
        self.vacancy = {
            "id": data.get("id"),
            "name": data.get("name"),
            "alternate_url": data.get("alternate_url"),
            "area": "",
            "salary": {
                "from": 0,
                "to": 0,
                "currency": None,
                "gross": None,
            },
            "snippet": data.get("snippet"),
            "schedule": "",
        }
        if data.get("salary"):
            if data.get("salary").get("from"):
                self.vacancy["salary"]["from"] = data.get("salary").get("from")
            else:
                self.vacancy["salary"]["from"] = 0
            if data.get("salary").get("to"):
                self.vacancy["salary"]["to"] = data.get("salary").get("to")
            else:
                self.vacancy["salary"]["to"] = 0
            self.vacancy["salary"]["currency"] = data.get("salary").get("currency")
            self.vacancy["salary"]["gross"] = data.get("salary").get("gross")
        if type(data.get("area")) == dict:
            self.vacancy["area"] = data.get("area").get("name")
        else:
            self.vacancy["area"] = data.get("area")
        if type(data.get("schedule")) == dict:
            self.vacancy["schedule"] = data.get("schedule").get("name")
        else:
            self.vacancy["schedule"] = data.get("schedule")

    def __str__(self):
        return (
            f'ID: {self.vacancy.get("id")}\n'
            f'Название: {self.vacancy.get("name")}\n'
            f'Регион: {self.vacancy.get("area")}\n'
            f"Зарплата от: {self.vacancy.get('salary').get('from')}, до: {self.vacancy.get('salary').get('to')} {self.vacancy.get('salary').get('currency')}\n"
            f"Описание:\n"
            f"Ссылка: {self.vacancy.get('alternate_url')}\n"
            f"Требования: {self.vacancy.get('snippet').get('requirement')}\n"
            f"Обязанности: {self.vacancy.get('snippet').get('responsibility')}\n"
        )

    def __lt__(self, other):
        return self.vacancy.get("salary").get("from") < other.vacancy.get("salary").get("from")

    def __gt__(self, other):
        return self.vacancy.get("salary").get("from") > other.vacancy.get("salary").get("from")


if __name__ == "__main__":
    vacancy = Vacancy(
        {
            "id": "108472084",
            "premium": False,
            "name": "Научный сотрудник / Молекулярный биолог",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "1", "name": "Москва", "url": "https://api.hh.ru/areas/1"},
            "salary": {"from": 150000, "to": None, "currency": "RUR", "gross": True},
            "type": {"id": "open", "name": "Открытая"},
            "address": {
                "city": "Москва",
                "street": "Трубецкая улица",
                "building": "8",
                "lat": 55.728317,
                "lng": 37.573815,
                "description": None,
                "raw": "Москва, Трубецкая улица, 8",
                "metro": {
                    "station_name": "Фрунзенская",
                    "line_name": "Сокольническая",
                    "station_id": "1.152",
                    "line_id": "1",
                    "lat": 55.727462,
                    "lng": 37.58022,
                },
                "metro_stations": [
                    {
                        "station_name": "Фрунзенская",
                        "line_name": "Сокольническая",
                        "station_id": "1.152",
                        "line_id": "1",
                        "lat": 55.727462,
                        "lng": 37.58022,
                    }
                ],
                "id": "16310690",
            },
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-10-10T15:14:21+0300",
            "created_at": "2024-10-10T15:14:21+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108472084",
            "show_logo_in_search": None,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/108472084?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/108472084",
            "relations": [],
            "employer": {
                "id": "5454844",
                "name": "Онкодиагностика Атлас",
                "url": "https://api.hh.ru/employers/5454844",
                "alternate_url": "https://hh.ru/employer/5454844",
                "logo_urls": {
                    "original": "https://img.hhcdn.ru/employer-logo-original/873514.png",
                    "240": "https://img.hhcdn.ru/employer-logo/3934932.png",
                    "90": "https://img.hhcdn.ru/employer-logo/3934931.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=5454844",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Опыт работы в молекулярно-биологической лаборатории от 5 лет. Глубокое понимание методов молекулярной <highlighttext>биологии</highlighttext>: от фореза до NGS. ",
                "responsibility": "Планирование, проведение и анализ результатов экспериментов. Разработка, оптимизация и валидация NGS-тестов. Тестирование сырья и готовой продукции. Ведение отчетной документации...",
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "79", "name": "Научный специалист, исследователь"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    )

    # print(vacancy.id)
    print(vacancy.vacancy)
    print(vacancy)
