import csv
import functools
import json
import math
from random import randint

CSV_FILENAME = "roots.csv"
JSON_FILENAME = "params_and_solutions.json"


def make_csv_file_with_random_square_roots(min_value_of_root=-1000, max_value_of_root=1000):
    with open(CSV_FILENAME, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for _ in range(randint(100, 1001)):
            writer.writerow((randint(min_value_of_root, max_value_of_root),
                             randint(min_value_of_root, max_value_of_root),
                             randint(min_value_of_root, max_value_of_root)))


def decorator_to_solve_all_equations_from_csv(func):
    """Решает все уравнения из файла CSV_FILENAME, заданного глобальной переменной.
    Действие: построчно читает int параметры [a, b, c] из csv и поочередно вызывает func(a, b, c)
    Возвращает кортеж решений"""

    @functools.wraps(func)
    def wrapper():
        with open(CSV_FILENAME, 'r', encoding='utf-8') as f:
            return tuple(func(*map(int, line)) for line in csv.reader(f))

    return wrapper


def decorator_to_save_solutions_to_json(func):
    """Читает параметры уравнения из файла CSV_FILENAME, заданного глобальной переменной,
    а также читает решения, переданные функцией func.
    Ожидает, что функция func вернет iterable из решений.
    Сохраняет параметры и решения в JSON_FILENAME"""

    @functools.wraps(func)
    def wrapper():
        with (open(JSON_FILENAME, 'w', encoding='utf-8', newline='') as json_file,
              open(CSV_FILENAME, 'r', encoding='utf-8') as csv_file):
            json.dump([{'a': example[0][0],
                        'b': example[0][1],
                        'c': example[0][2],
                        'solutions': example[1]}
                       for example in zip(csv.reader(csv_file), func())],
                      json_file, indent=3)
        return "finished decorator_to_save_solutions_to_json"

    return wrapper


@decorator_to_save_solutions_to_json
@decorator_to_solve_all_equations_from_csv
def find_roots(a, b, c):
    if a == 0:
        return -c / b

    discriminant = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(discriminant))

    if discriminant > 0:
        return (((-b + sqrt_val) / (2 * a),
                 (-b - sqrt_val) / (2 * a)))
    elif discriminant == 0:
        return -b / (2 * a)
    else:
        return None


if __name__ == '__main__':
    find_roots()
