import logging

from numpy.ma.core import count

from config import LOG_FORMAT, LOG_LEVEL
from src.hh_parser import HH
from src.saver import SaveDataInJsonFile
from src.search import vacancies_search
from src.utils import get_len_base, bubble_sort, bubble_sort_area
from src.vacancy import Vacancy

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(LOG_FORMAT)
logger.addHandler(console_handler)
logger.setLevel(LOG_LEVEL)

def menu_1(vacancies):
    value_menu = ''
    how_much_show = 10
    while value_menu != '0':
        print(f'1. Выбрать кол-во вакансий выводимых на экран. Установлено {how_much_show}\n'
              f'2. Отсортировать по ЗП по убыванию\n'
              f'3. Отсортировать по региону по алфавиту\n'
              f'4. Показать ВСЕ\n'
              f'5. ТОП N вакансий по ЗП\n'
              f'6. Поиск вакансии по ключевым словам\n'
              f'0. Выход в главное меню')
        value_menu = input('Введите пункт меню => ')
        match value_menu:
            case '1':
                how_much_show = int(input('Введите кол-во вакансий выводимых на экран => '))
            case '2':
                data_from_sort = bubble_sort(vacancies)
                for i in range(how_much_show):
                    print(data_from_sort[i])
            case '3':
                data_from_sort = bubble_sort_area(vacancies)
                for i in range(how_much_show):
                    print(data_from_sort[i])
            case '4':
                for i in vacancies:
                    print(i)
            case '5':
                n = int(input('Введите N => '))
                data_from_sort = bubble_sort(vacancies)
                for i in range(n):
                    print(data_from_sort[i])
            case '6':
                print(vacancies)
                vacancies_search(vacancies, 'биолог')
            case '0':
                pass
            case _:
                print('Нет такого пункта, повторите ввод')


def main():
    """Функция, запускающая само приложение выдающая основное меню"""
    main_menu = ''
    save_data = SaveDataInJsonFile()
    while main_menu != '0':
        print(f'1. Загрузка данных с HH.ru\n'
              f'2. Работа с локальной базой. В локальной базе {get_len_base(save_data.file_name)} вакансий\n'
              f'0. Выход'
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
                vacancies_for_save = []
                vacancies_for_processing = []
                for i in data_load_with_hh:
                    # save_data.save_data(Vacancy(i).vacancy)
                    vacancy = Vacancy(i)
                    vacancies_for_save.append(vacancy.vacancy)
                    vacancies_for_processing.append(vacancy)
                # save_data.save_data(data_load_with_hh)
                save_data.save_dataset(vacancies_for_save)
                # save_data.delete_data(108130637)
                menu_1(vacancies_for_processing)
            case "2":
                print(f'1. Удалить вакансию по ID')
            case "3":
                pass
            case "0":
                pass
            case _:
                print('Нет такого пункта, повторите ввод')

if __name__ == '__main__':
    main()