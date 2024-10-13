import logging
import os
import re

from config import LOG_FORMAT, LOG_LEVEL, DATA_PATH
from src.hh_parser import HH
from src.saver import SaveDataInJsonFile
from src.search import vacancies_search
from src.utils import get_len_base, bubble_sort, bubble_sort_area, filter_by_salary_range
from src.vacancy import Vacancy

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(LOG_FORMAT)
logger.addHandler(console_handler)
logger.setLevel(LOG_LEVEL)


def menu_1(save_data: SaveDataInJsonFile, main_menu: str, data_load_with_base: list) -> None:
    value_menu = ""
    how_much_show = 10
    vacancies = []
    for i in data_load_with_base:
        vacancy = Vacancy(i)
        vacancies.append(vacancy)
    if main_menu == "1":
        save_data.save_dataset(vacancies)
    while value_menu != "0":
        if main_menu == "1":
            print(f"МЕНЮ РАБОТЫ С БАЗОЙ ПОЛУЧЕННОЙ С HH.RU")
        elif main_menu == "2":
            print(f"МЕНЮ РАБОТЫ С ЛОКАЛЬНОЙ БАЗОЙ ДАННЫХ")
            print(f"В локальной базе доступно {len(vacancies)} вакансий")
        print(
            f"1. Выбрать кол-во вакансий выводимых на экран. Установлено {how_much_show}\n"
            f"2. Отсортировать все по ЗП по убыванию\n"
            f"3. Отсортировать все по региону по алфавиту\n"
            f"4. Показать ВСЕ\n"
            f"5. ТОП N вакансий по ЗП\n"
            f"6. Поиск вакансии по ключевым словам\n"
            f"7. Показать вакансии в диапазона зарплат от - до"
        )
        if main_menu == "2":
            print(f"8. Удаление вакансии из локальной базы по ID")
        print(f"0. Выход в главное меню\n")
        value_menu = input("Введите пункт меню => ")
        match value_menu:
            case "1":
                how_much_show = int(input("Введите кол-во вакансий выводимых на экран => "))
            case "2":
                data_from_sort = bubble_sort(vacancies)
                temp_show = how_much_show
                if len(data_from_sort) < temp_show:
                    temp_show = len(data_from_sort)
                for i in range(temp_show):
                    print(data_from_sort[i])
                print(f">>> Получено результатов {len(data_from_sort)} / показано на экран {temp_show}\n")
            case "3":
                data_from_sort = bubble_sort_area(vacancies)
                temp_show = how_much_show
                if len(data_from_sort) < temp_show:
                    temp_show = len(data_from_sort)
                for i in range(temp_show):
                    print(data_from_sort[i])
                print(f">>> Получено результатов {len(data_from_sort)} / показано на экран {temp_show}\n")
            case "4":
                for i in vacancies:
                    print(i)
            case "5":
                data_from_sort = bubble_sort(vacancies)
                temp_show = int(input("Введите N => "))
                if len(data_from_sort) < temp_show:
                    temp_show = len(data_from_sort)
                for i in range(temp_show):
                    print(data_from_sort[i])
            case "6":
                result_for_show: list = vacancies_search(vacancies, input("введите ключевое слово => "))
                temp_show = how_much_show
                if len(result_for_show) < temp_show:
                    temp_show = len(result_for_show)
                for i in range(temp_show):
                    print(result_for_show[i])
                print(f">>> Получено результатов {len(result_for_show)} / показано на экран {temp_show}\n")
            case "7":
                salary_range = input("Введите диапазон зарплат от - до => ")
                search_int_list = re.findall(r"\d+\W\d+\W\d+|\d+", salary_range, flags=re.IGNORECASE | re.DOTALL)
                logger.info(search_int_list)
                try:
                    if int(search_int_list[0]) > int(search_int_list[1]):
                        search_int_list[0], search_int_list[1] = search_int_list[1], search_int_list[0]
                    result_for_show: list = filter_by_salary_range(vacancies, search_int_list[0], search_int_list[1])
                    temp_show = how_much_show
                    if len(result_for_show) < temp_show:
                        temp_show = len(result_for_show)
                    for i in range(temp_show):
                        print(result_for_show[i])
                    print(f">>> Получено результатов {len(result_for_show)} / показано на экран {temp_show}\n")
                except IndexError:
                    print(
                        "\nОШИБКА! Введены не верные данны!\n" "Необходимо указать диапазон ЗП двумя числами от и до\n"
                    )
            case "8":
                if main_menu == "2":
                    save_data.delete_data(
                        input("Введите ID для удаления (ввести можно несколько ID через запятую) => ")
                    )
                    data_load_with_base = save_data.get_data(os.path.join(DATA_PATH, save_data.file_name))
                    vacancies = []
                    for i in data_load_with_base:
                        vacancy = Vacancy(i)
                        vacancies.append(vacancy)
            case "0":
                pass
            case _:
                print("Нет такого пункта, повторите ввод")


def main() -> None:
    """Функция, запускающая само приложение выдающая основное меню"""
    main_menu = ""
    save_data = SaveDataInJsonFile()
    while main_menu != "0":
        print(
            f"\nГЛАВНОЕ МЕНЮ\n"
            f"1. Загрузка данных с HH.ru\n"
            f"2. Работа с локальной базой. В локальной базе {get_len_base(save_data.file_name)} вакансий\n"
            f"0. Выход"
        )
        main_menu = input("Введите пункт меню => ")
        # условный оператор, который согласно выбору пользователя запускает функции чтения файлов и получения из них
        # информации
        match main_menu:
            case "1":
                hh_parser = HH()
                search_bar_user = input("Введите строку поиска => ")
                data_load_with_hh = hh_parser.load_vacancies(search_bar_user)
                print(f"По запросу найдено {hh_parser.vacancies_cont} вакансий")
                print(f"Скачено {len(data_load_with_hh)} вакансии")
                menu_1(save_data, main_menu, data_load_with_hh)
            case "2":
                data_load_with_local_base = save_data.get_data(os.path.join(DATA_PATH, save_data.file_name))
                menu_1(save_data, main_menu, data_load_with_local_base)
            case "0":
                pass
            case _:
                print("Нет такого пункта, повторите ввод")


if __name__ == "__main__":
    main()
