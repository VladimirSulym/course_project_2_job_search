import os
import re

from config import DATA_PATH
from src.saver import SaveDataInJsonFile
from src.vacancy import Vacancy


def vacancies_search(dicts_vacancies: list, search_str: str) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращать список словарей, у которых есть данные в записях совпадающие с данной строкой. Функция осуществляет
    поиск по всем полям и возвращает максимально подходящие варианты ответа в зависимости от степени совпадения данных
    """
    if dicts_vacancies and search_str:
        search_str_list = re.findall(
            r"[^\d\W][a-zA-Zа-яА-Я\s]+[^\W\d]|[a-zA-Zа-яА-Я]", search_str, flags=re.IGNORECASE | re.DOTALL
        )
        search_int_list = re.findall(r"\d+\W\d+\W\d+|\d+", search_str, flags=re.IGNORECASE | re.DOTALL)
        print(search_str_list)
        print(search_int_list)
        result = []
        for dict_trans in dicts_vacancies:
            for key, value in dict_trans.items():
                if search_int_list:
                    for i in search_int_list:
                        print('i int = ', i)
                        if str(value).strip().find(i) != -1:
                            result.append(dict_trans)
                if search_str_list:
                    for i in search_str_list:
                        print('i str = ', i)
                        if str(value).strip().find(i) != -1:
                            result.append(dict_trans)
        # result_filter = []
        # flag_set = set()
        # flag_rank = 2
        # for i in result:
        #     temp = tuple(i.items())
        #     if result.count(i) == flag_rank:
        #         if temp not in flag_set:
        #             flag_set.add(temp)
        #             result_filter.append(i)
        #     elif result.count(i) > flag_rank:
        #         flag_rank = result.count(i)
        #         flag_set.add(temp)
        #         result_filter = [i]
        # if result_filter:
        #     return result_filter
        # else:
        return result
    elif dicts_vacancies and (search_str is None or search_str == ""):
        return dicts_vacancies
    else:
        return []


if __name__ == '__main__':
    save_data = SaveDataInJsonFile()
    data_for_filter = save_data.get_data(os.path.join(DATA_PATH, "base_vacancies.json"))
    list_for_search = []
    for i in range(50):
        list_for_search.append(data_for_filter[i])
    print(list_for_search)
    print(vacancies_search(list_for_search, 'дисциплинированность'))
    # vacancies_for_processing =[]
    # for i in data_for_filter:
        # save_data.save_data(Vacancy(i).vacancy)
        # vacancy = Vacancy(i)
        # vacancies_for_save.append(vacancy.vacancy)
        # vacancies_for_processing.append(vacancy)
    # print(vacancies_for_processing)
    # transaction_search(data_for_filter,"Euro")
    #
    # for i in transaction_search(convert_csv_to_list(os.path.join(DATA_PATH, "transactions.csv")), '')[:]:
    #     print(i)
