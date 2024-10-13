import logging
import os

from config import LOG_FORMAT, LOG_LEVEL, DATA_PATH
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

def menu_1(vacancies,main_menu):
    value_menu = ''
    how_much_show = 10
    while value_menu != '0':
        if main_menu == '1':
            print(f'МЕНЮ РАБОТЫ С БАЗОЙ ПОЛУЧЕННОЙ С HH.RU')
        elif main_menu == '2':
            print(f'МЕНЮ РАБОТЫ С ЛОКАЛЬНОЙ БАЗОЙ ДАННЫХ')
        print(f'1. Выбрать кол-во вакансий выводимых на экран. Установлено {how_much_show}\n'
              f'2. Отсортировать по ЗП по убыванию\n'
              f'3. Отсортировать по региону по алфавиту\n'
              f'4. Показать ВСЕ\n'
              f'5. ТОП N вакансий по ЗП\n'
              f'6. Поиск вакансии по ключевым словам')
        if main_menu == '2':
            print(f'7. Удаление вакансии из локальной базы')
        print(f'0. Выход в главное меню\n')
        value_menu = input('Введите пункт меню => ')
        match value_menu:
            case '1':
                how_much_show = int(input('Введите кол-во вакансий выводимых на экран => '))
            case '2':
                data_from_sort = bubble_sort(vacancies)
                temp_show = how_much_show
                if len(data_from_sort) < temp_show:
                    temp_show = len(data_from_sort)
                for i in range(temp_show):
                    print(data_from_sort[i])
                print(f'>>> Получено результатов {len(data_from_sort)} / показано на экран {temp_show}')
            case '3':
                data_from_sort = bubble_sort_area(vacancies)
                temp_show = how_much_show
                if len(data_from_sort) < temp_show:
                    temp_show = len(data_from_sort)
                for i in range(temp_show):
                    print(data_from_sort[i])
                print(f'>>> Получено результатов {len(data_from_sort)} / показано на экран {temp_show}')
            case '4':
                for i in vacancies:
                    print(i)
            case '5':
                data_from_sort = bubble_sort(vacancies)
                temp_show = int(input('Введите N => '))
                if len(data_from_sort) < temp_show:
                    temp_show = len(data_from_sort)
                for i in range(temp_show):
                    print(data_from_sort[i])
            case '6':
                # print(vacancies[0])
                result_for_show: list = vacancies_search(vacancies, input('введите ключевое слово => '))
                temp_show = how_much_show
                if len(result_for_show) < temp_show:
                    temp_show = len(result_for_show)
                for i in range(temp_show):
                    print(result_for_show[i])
                print(f'>>> Получено результатов {len(result_for_show)} / показано на экран {temp_show}')
            case '7':
                if main_menu == '2':
                    pass

            case '0':
                pass
            case _:
                print('Нет такого пункта, повторите ввод')


def main():
    """Функция, запускающая само приложение выдающая основное меню"""
    main_menu = ''
    save_data = SaveDataInJsonFile()
    while main_menu != '0':
        print(f'\nГЛАВНОЕ МЕНЮ\n'
              f'1. Загрузка данных с HH.ru\n'
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
                vacancies_for_processing = []
                for i in data_load_with_hh:
                    # save_data.save_data(Vacancy(i).vacancy)
                    vacancy = Vacancy(i)
                    vacancies_for_processing.append(vacancy)
                # save_data.save_data(data_load_with_hh)
                save_data.save_dataset(vacancies_for_processing)
                # save_data.delete_data(108130637)
                menu_1(vacancies_for_processing, main_menu)
            case "2":
                data_load_with_local_base = save_data.get_data(os.path.join(DATA_PATH, save_data.file_name))
                # print(data_load_with_local_base)
                vacancies_for_processing = []
                for i in data_load_with_local_base:
                    # save_data.save_data(Vacancy(i).vacancy)
                    vacancy = Vacancy(i)
                    # vacancies_for_save.append(vacancy.vacancy)
                    vacancies_for_processing.append(vacancy)
                print(f'В локальной базе доступно {len(vacancies_for_processing)} вакансий')
                # print(f'1. Удалить вакансию по ID')
                save_data.delete_data('108346287, 107960123, 108485427, 23423  ,  234234')
                menu_1(vacancies_for_processing, main_menu)
            case "3":
                pass
            case "0":
                pass
            case _:
                print('Нет такого пункта, повторите ввод')

if __name__ == '__main__':
    main()