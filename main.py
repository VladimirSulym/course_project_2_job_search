import logging

from config import LOG_FORMAT, LOG_LEVEL
from src.hh_parser import HH
from src.saver import SaveDataInJsonFile

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(LOG_FORMAT)
logger.addHandler(console_handler)
logger.setLevel(LOG_LEVEL)

def main():
    """Функция, запускающая само приложение выдающая основное меню"""
    print(
        "1. Загрузка данных с HH\n"
        "0. Выход"
    )
    main_menu = input("Введите пункт меню => ")
    # условный оператор, который согласно выбору пользователя запускает функции чтения файлов и получения из них
    # информации
    match main_menu:
        case "1":
            hh_parser = HH()
            search_bar_user = input('Введите строку поиска => ')
            data_load_with_hh = hh_parser.load_vacancies(search_bar_user)
            print(f'По запросу найдено {hh_parser.vacancies_cont} вакансий')
            print(f'Скачено {len(data_load_with_hh)} вакансии')
            save_data = SaveDataInJsonFile()
            save_data.save_data(data_load_with_hh)
        case "2":
            pass
        case "3":
            pass
        case _:
            pass

if __name__ == '__main__':
    main()