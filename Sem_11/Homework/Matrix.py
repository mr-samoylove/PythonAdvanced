import numpy


class Matrix:
    def __init__(self, iterable_of_iterables):
        """
        init
        :param iterable_of_iterables: Например, список списков или кортеж кортежей
        """
        self.matrix = iterable_of_iterables

    def __eq__(self, other):
        return all((left == right for left, right in zip(self.matrix, other.matrix)))

    def __add__(self, other):
        """
        Без использования numpy, сложение вручную
        :param other:
        :return: new Matrix
        """
        if not self.__check_size_compatibility(other):
            raise RuntimeError("Складывать можно только матрицы одной размерности")
        else:
            new_iterable = list()
            for left, right in zip(self.matrix, other.matrix):
                new_iterable.append(list(x1 + x2 for x1, x2 in zip(left, right)))
            return Matrix(new_iterable)

    def __mul__(self, other):
        """
        Используется numpy. Зачем изобретать свое уможение матриц, если все уже написано?
        :param other:
        :return: new Matrix
        """
        return Matrix(numpy.matmul(self.matrix, other.matrix).tolist())

    def __check_size_compatibility(self, other):
        if len(self.matrix) != len(other.matrix):
            return False
        for left, right in zip(self.matrix, other.matrix):
            if len(left) != len(right):
                return False
        return True

    def __str__(self):
        return str(self.matrix)


if __name__ == '__main__':
    m1 = Matrix(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    m2 = Matrix(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
    m3 = Matrix(((10, 10, 10), (10, 10, 10), (10, 10, 10)))
    print(m1 == m2)
    print(m1 == m3)
    print(m2 == m3)

    print(f'Matrix 1: {m1}')
    print(f'Matrix 2: {m2}')
    print(f'Matrix 1 + Matrix 2: {m1 + m2}')
    print(f'Matrix 1 * Matrix 2: {m1 * m2}')
