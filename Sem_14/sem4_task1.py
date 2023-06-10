# Напишите функцию для транспонирования матрицы.

def transposition(matrix: tuple) -> tuple:
    """
    функцию для транспонирования матрицы.
    :param matrix: tuple
    :return: tuple

    >>> print(transposition(((1, 2, 3), (4, 5, 6), (7, 8, 9))))
    ((1, 4, 7), (2, 5, 8), (3, 6, 9))
    >>> print(transposition(((1, 1, 1), (2, 2, 2), (-3, -3, -3))))
    ((1, 2, -3), (1, 2, -3), (1, 2, -3))
    >>> print(transposition(((1.2, 2.2, 3.2), (4.1, 5, 6), (7, 8, 9))))
    ((1.2, 4.1, 7), (2.2, 5, 8), (3.2, 6, 9))
    >>> print(transposition((('a', 'b', 'c'), (2, 2, 2), (-3, -3, -3))))
    (('a', 2, -3), ('b', 2, -3), ('c', 2, -3))
    """
    return tuple(zip(*matrix))


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
