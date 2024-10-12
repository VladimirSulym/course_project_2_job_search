

class Vacancy:
    id: str
    name: str
    area: str
    salary: {}
    snippet: {}
    schedule: str

    def __init__(self, id, name, area, salary, snippet, schedule):
        self.id = id
        self.name = name
        self.area = area
        if salary:
            if salary.get('from'):
                self.salary['from'] = salary['from']
            else:
                self.salary['from'] = 0
            if salary.get('to'):
                self.salary['to'] = salary['to']
            else:
                self.salary['to'] = 0
            self.salary['currency'] = salary['currency']
            self.salary['gross'] = salary['gross']
        self.snippet = snippet
        self.schedule = schedule.get('name')


if __name__ == '__main__':
    vacancy = Vacancy({
        "id": "108472084",
        "premium": false,
        "name": "Научный сотрудник / Молекулярный биолог",
        "department": null,
        "has_test": false,
        "response_letter_required": false,
        "area": {
            "id": "1",
            "name": "Москва",
            "url": "https://api.hh.ru/areas/1"
        },
        "salary": {
            "from": 150000,
            "to": null,
            "currency": "RUR",
            "gross": true
        },
        "type": {
            "id": "open",
            "name": "Открытая"
        },
        "address": {
            "city": "Москва",
            "street": "Трубецкая улица",
            "building": "8",
            "lat": 55.728317,
            "lng": 37.573815,
            "description": null,
            "raw": "Москва, Трубецкая улица, 8",
            "metro": {
                "station_name": "Фрунзенская",
                "line_name": "Сокольническая",
                "station_id": "1.152",
                "line_id": "1",
                "lat": 55.727462,
                "lng": 37.58022
            },
            "metro_stations": [
                {
                    "station_name": "Фрунзенская",
                    "line_name": "Сокольническая",
                    "station_id": "1.152",
                    "line_id": "1",
                    "lat": 55.727462,
                    "lng": 37.58022
                }
            ],
            "id": "16310690"
        },
        "response_url": null,
        "sort_point_distance": null,
        "published_at": "2024-10-10T15:14:21+0300",
        "created_at": "2024-10-10T15:14:21+0300",
        "archived": false,
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108472084",
        "show_logo_in_search": null,
        "insider_interview": null,
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
                "90": "https://img.hhcdn.ru/employer-logo/3934931.png"
            },
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=5454844",
            "accredited_it_employer": false,
            "trusted": true
        },
        "snippet": {
            "requirement": "Опыт работы в молекулярно-биологической лаборатории от 5 лет. Глубокое понимание методов молекулярной <highlighttext>биологии</highlighttext>: от фореза до NGS. ",
            "responsibility": "Планирование, проведение и анализ результатов экспериментов. Разработка, оптимизация и валидация NGS-тестов. Тестирование сырья и готовой продукции. Ведение отчетной документации..."
        },
        "contacts": null,
        "schedule": {
            "id": "fullDay",
            "name": "Полный день"
        },
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": false,
        "professional_roles": [
            {
                "id": "79",
                "name": "Научный специалист, исследователь"
            }
        ],
        "accept_incomplete_resumes": false,
        "experience": {
            "id": "between1And3",
            "name": "От 1 года до 3 лет"
        },
        "employment": {
            "id": "full",
            "name": "Полная занятость"
        },
        "adv_response_url": null,
        "is_adv_vacancy": false,
        "adv_context": null
    })

    print(vacancy.id)