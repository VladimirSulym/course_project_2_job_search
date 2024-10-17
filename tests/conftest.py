import pytest

from src.hh_parser import HH
from src.saver import SaveDataInJsonFile
from src.vacancy import Vacancy


@pytest.fixture()
def hh_loader():
    return HH()


@pytest.fixture()
def vacancies_for_test():
    vacancies = []
    for i in [
        {
            "id": "107370917",
            "name": "Онколог-хирург, маммолог",
            "alternate_url": "https://hh.ru/vacancy/107370917",
            "area": "Санкт-Петербург",
            "salary": {"from": 300000, "to": 500000, "currency": "RUR", "gross": True},
            "snippet": {
                "requirement": "Опыт работы в должности онколога-хирурга, <highlighttext>маммолога</highlighttext> "
                "не менее 6 лет. Наличие действующего сертификата специалиста. Умение работать в "
                "команде, ответственность...",
                "responsibility": "Проведение диагностики и лечения заболеваний молочной железы, включая "
                "онкологические заболевания. Выполнение хирургических операций различной сложности. "
                "Ведение амбулаторного приема пациентов. ",
            },
            "schedule": "Полный день",
        },
        {
            "id": "107642936",
            "name": "ВРАЧ ОНКОЛОГ",
            "alternate_url": "https://hh.ru/vacancy/107642936",
            "area": "Москва",
            "salary": {"from": 250000, "to": 0, "currency": "RUR", "gross": False},
            "snippet": {
                "requirement": "высшее профильное образование. - наличие необходимых квалификационных сертификатов. "
                "- опыт работы с пациентами. - Опыт работы по специальности не менее 3-х лет. - ",
                "responsibility": "амбулаторный прием. - диагностика, лечение и профилактика заболеваний. - "
                "консультирование по лабораторной диагностике. - проведение лечебных манипуляций. "
                "- ведение медицинской документации.",
            },
            "schedule": "Полный день",
        },
        {
            "id": "108123109",
            "name": "Инструктор ЛФК",
            "alternate_url": "https://hh.ru/vacancy/108123109",
            "area": "Кемерово",
            "salary": {"from": 50000, "to": 0, "currency": "RUR", "gross": False},
            "snippet": {
                "requirement": 'Среднее профессиональное образование по специальности "Сестринское дело", '
                '"Лечебное дело", "Акушерское дело" или Высшее. Так же готовы рассмотреть '
                "без опыта, но...",
                "responsibility": "Реабилитация после операционных пациентов (травматология, ортопедия, "
                "<highlighttext>маммология</highlighttext>, урология, гинекология). "
                "Работа на высокотехнологичном реабилитационном оборудовании. "
                "Обучение! Быть немного психологом и любить...",
            },
            "schedule": "Сменный график",
        },
    ]:
        vacancy = Vacancy(i)
        vacancies.append(vacancy)
    return vacancies


@pytest.fixture()
def test_vacancy():
    return Vacancy(
        {
            "id": "93353083",
            "premium": False,
            "name": "Тестировщик комфорта квартир",
            "department": None,
            "has_test": False,
            "response_letter_required": False,
            "area": {"id": "26", "name": "Воронеж", "url": "https://api.hh.ru/areas/26"},
            "salary": {"from": 0, "to": 450000, "currency": "RUR", "gross": False},
            "type": {"id": "open", "name": "Открытая"},
            "address": None,
            "response_url": None,
            "sort_point_distance": None,
            "published_at": "2024-02-16T14:58:28+0300",
            "created_at": "2024-02-16T14:58:28+0300",
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93353083",
            "branding": {"type": "CONSTRUCTOR", "tariff": "BASIC"},
            "show_logo_in_search": True,
            "insider_interview": None,
            "url": "https://api.hh.ru/vacancies/93353083?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/93353083",
            "relations": [],
            "employer": {
                "id": "3499705",
                "name": "Специализированный застройщик BM GROUP",
                "url": "https://api.hh.ru/employers/3499705",
                "alternate_url": "https://hh.ru/employer/3499705",
                "logo_urls": {
                    "original": "https://hhcdn.ru/employer-logo-original/1214854.png",
                    "240": "https://hhcdn.ru/employer-logo/6479866.png",
                    "90": "https://hhcdn.ru/employer-logo/6479865.png",
                },
                "vacancies_url": "https://api.hh.ru/vacancies?employer_id=3499705",
                "accredited_it_employer": False,
                "trusted": True,
            },
            "snippet": {
                "requirement": "Занимать активную жизненную позицию, уметь активно танцевать и громко петь."
                " Обладать навыками коммуникации, чтобы налаживать добрососедские отношения. "
                "Обладать системным мышлением...",
                "responsibility": "Оценивать вид из окна: встречать рассветы на кухне, и провожать алые закаты "
                "в спальне. Оценивать инфраструктуру района: ежедневно ходить на...",
            },
            "contacts": None,
            "schedule": {"id": "flexible", "name": "Гибкий график"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "107", "name": "Руководитель проектов"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "noExperience", "name": "Нет опыта"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        }
    )


@pytest.fixture()
def test_saver():
    return SaveDataInJsonFile()


# @pytest.fixture()
# def product_iphone():
#     return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#
#
# @pytest.fixture()
# def category_smartphone():
#     return Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [Product("Iphone 15", "512GB, Gray space", 210000.0, 8)],
#     )
#
#
# @pytest.fixture()
# def products_for_test():
#     return [
#         {
#             "name": "Смартфоны",
#             "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных "
#             "функций для удобства жизни",
#             "products": [
#                 {
#                     "name": "Samsung Galaxy C23 Ultra",
#                     "description": "256GB, Серый цвет, 200MP камера",
#                     "price": 180000.0,
#                     "quantity": 5,
#                 },
#                 {"name": "Iphone 15", "description": "512GB, Gray space", "price": 210000.0, "quantity": 8},
#                 {"name": "Xiaomi Redmi Note 11", "description": "1024GB, Синий", "price": 31000.0, "quantity": 14},
#             ],
#         },
#         {
#             "name": "Телевизоры",
#             "description": "Современный телевизор, который позволяет наслаждаться просмотром, "
#             "станет вашим другом и помощником",
#             "products": [
#                 {"name": '55" QLED 4K', "description": "Фоновая подсветка", "price": 123000.0, "quantity": 7}
#             ],
#         },
#     ]
#
#
# @pytest.fixture()
# def product_for_new_product(product_iphone):
#     return product_iphone.new_product(
#         {
#             "name": "Samsung Galaxy S23 Ultra",
#             "description": "256GB, Серый цвет, 200MP камера",
#             "price": 190000.0,
#             "quantity": 5,
#         }
#     )
#
#
# @pytest.fixture()
# def product_lawn_grass():
#     return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
#
#
# @pytest.fixture()
# def product_smartphone():
#     return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
