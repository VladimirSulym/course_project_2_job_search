import json
import logging
import os

from config import DATA_PATH, LOG_FORMAT, LOG_LEVEL

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(LOG_FORMAT)
logger.addHandler(console_handler)
logger.setLevel(LOG_LEVEL)

def get_len_base(file_name):
    path = os.path.join(DATA_PATH, file_name)
    try:
        with open(path, 'r') as f:
            return len(json.load(f))
    except FileNotFoundError:
        logger.error(f'Файл с базой вакансий не найден: {path}')
        return 0

def bubble_sort(user_list):
    n = len(user_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if user_list[j] < user_list[j + 1]:
                user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
    return user_list

def bubble_sort_area(user_list):
    n = len(user_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if user_list[j].vacancy.get('area') > user_list[j + 1].vacancy.get('area'):
                user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
    return user_list

if __name__ == '__main__':
    print(bubble_sort([3, 1, 2, 5, 4]))
