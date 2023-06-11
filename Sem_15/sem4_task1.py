import argparse
import logging
from itertools import zip_longest


def transposition(matrix: tuple) -> tuple:
    FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" в строке {lineno:03d} функция "{funcName}()" ' \
             'секунд записала сообщение: {msg} '
    logging.basicConfig(format=FORMAT, style='{', filename='transposition_logs.txt', filemode='a', encoding='utf-8',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)
    if len(matrix) == 0:
        logger.warning("Матрица пустая")
    elif len(set((len(row) for row in matrix))) != 1:
        logger.warning("Длины строк в матрице не равны, идет заполнение пустых полей с помощью None")
    else:
        logger.info("Транспонирую")
    return tuple(zip_longest(*matrix))


if __name__ == '__main__':
    # matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    # print('old matrix: ', matrix)
    # print('new matrix: ', transposition(matrix))
    #
    # matrix = tuple()
    # print('old matrix: ', matrix)
    # print('new matrix: ', transposition(matrix))
    #
    # matrix = ((1, 2, 3), (4, 5, 6), (7,))
    # print('old matrix: ', matrix)
    # print('new matrix: ', transposition(matrix))

    arg_parser = argparse.ArgumentParser(description='Matrix transposition. Example of call: '
                                                     'python .\sem4_task1.py -a 1 2 3 -b 4 5 6')
    for ch in range(ord('a'), ord('h')):
        arg_parser.add_argument(f'-{chr(ch)}', metavar=chr(ch), type=str, nargs="+",
                                help=f'Введите строку номер {ch - ord("a") + 1} через пробел')
    args = arg_parser.parse_args()
    matrix = tuple(filter(None, (args.__getattribute__(chr(ch)) for ch in range(ord('a'), ord('h')))))
    print('old matrix: ', matrix)
    print('new matrix: ', transposition(matrix))
