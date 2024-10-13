import json
import logging
import os
from abc import ABC, abstractmethod

from config import DATA_PATH, LOG_FORMAT, LOG_LEVEL

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(LOG_FORMAT)
logger.addHandler(console_handler)
logger.setLevel(LOG_LEVEL)


class FileWork(ABC):
    @abstractmethod
    def get_data(self, path: str) -> dict:
        pass

    @abstractmethod
    def save_data(self, data):
        pass

    @abstractmethod
    def delete_data(self, id):
        pass


class SaveDataInJsonFile(FileWork):
    file_name = ''

    def __init__(self, file_name='base_vacancies.json'):
        SaveDataInJsonFile.file_name = file_name

    def get_data(self, path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f'Файл с базой вакансий не найден: {path}')
            return []

    def save_data(self, data):
        """Функция получает словарь с вакансией, проверяет его с существующей локальной базой и заполняет
        базу всеми отсутствующими вакансиями"""
        data_for_comparison = self.get_data(os.path.join(DATA_PATH, SaveDataInJsonFile.file_name))
        result_data_for_save = []
        logger.debug(f'Длина файла {len(data_for_comparison)}')
        if data_for_comparison:
            result_data_for_save.extend(data_for_comparison)
            flag = True
            for i in data_for_comparison:
                if i.get('id') == data.get('id'):
                    flag = False
            if flag:
                result_data_for_save.append(data)
        else:
            result_data_for_save.append(data)
        logger.debug(f'Длина файла {len(result_data_for_save)}')
        with open(os.path.join(DATA_PATH, SaveDataInJsonFile.file_name), 'w') as f:
            json.dump(result_data_for_save, f, ensure_ascii=False, indent=4)
            logger.info("Файл сохранен")

    def save_dataset(self, data):
        """Функция получает список словарей с вакансиями, проверяет его с существующей локальной базой и заполняет
        базу всеми отсутствующими вакансиями"""
        data_for_comparison = self.get_data(os.path.join(DATA_PATH, SaveDataInJsonFile.file_name))
        result_data_for_save = []
        logger.debug(f'Длина файла {len(data_for_comparison)}')
        logger.debug(f'data = {data[0]}')
        if data_for_comparison:
            result_data_for_save.extend(data_for_comparison)
            for i in data:
                flag = True
                for j in data_for_comparison:
                    if i.vacancy.get('id') == j.get('id'):
                        flag = False
                if flag:
                    result_data_for_save.append(i.vacancy)
        elif data:
            for i in data:
                result_data_for_save.append(i.vacancy)
        logger.debug(f'Длина файла {len(result_data_for_save)}')
        with open(os.path.join(DATA_PATH, SaveDataInJsonFile.file_name), 'w') as f:
            json.dump(result_data_for_save, f, ensure_ascii=False, indent=4)
            logger.info("Файл сохранен")
            print(f'Локальная база обновлена и содержит {len(result_data_for_save)} вакансий')

    def delete_data(self, list_delete_id):
        """Функция удаляет из локальной базу вакансию с заданным ID"""
        list_delete_id = list_delete_id.split(',')
        list_delete_id = [i.strip() for i in list_delete_id]
        print(list_delete_id)
        for delete_id in list_delete_id:
            data_for_delete = self.get_data(os.path.join(DATA_PATH, SaveDataInJsonFile.file_name))
            result_data_for_save = []
            logger.debug(f'Длина файла {len(data_for_delete)}')
            if data_for_delete:
                for i in data_for_delete:
                    if i.get('id') != str(delete_id):
                        result_data_for_save.append(i)
            if data_for_delete == result_data_for_save:
                print(f'Вакансия с ID {delete_id} не найдена')
            logger.debug(f'Длина файла {len(result_data_for_save)}')
            with open(os.path.join(DATA_PATH, SaveDataInJsonFile.file_name), 'w') as f:
                json.dump(result_data_for_save, f, ensure_ascii=False, indent=4)
                logger.info("Файл сохранен")


if __name__ == '__main__':
    test = SaveDataInJsonFile('temp121.json')
    print(test.get_data())
