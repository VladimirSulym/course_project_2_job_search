import json
import os
from abc import ABC, abstractmethod

from config import DATA_PATH

class FileWork (ABC):
    @abstractmethod
    def get_data(self, file_path):
        pass

    @abstractmethod
    def save_data(self, data):
        pass

    # @abstractmethod
    # def delete_data(self):
    #     pass

class SaveDataInJsonFile(FileWork):

    file_name = ''

    def __init__(self, file_name='base_vacancies.json'):
        # self.file_path = ''
        # self.data = []
        SaveDataInJsonFile.file_name = file_name

    def get_data(self, file_path):
        path = os.path.join(DATA_PATH, file_path)
        with open(path, 'r') as f:
            return json.load(f)

    def save_data(self, data):
        with open(os.path.join(DATA_PATH, SaveDataInJsonFile.file_name), 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    test = SaveDataInJsonFile('temp121.json')
    print(test.get_data())