import pytest

from sem4_task1 import transposition


def test_all_integers_positive():
    assert transposition(((1, 2, 3), (4, 5, 6), (7, 8, 9))) == ((1, 4, 7), (2, 5, 8), (3, 6, 9)), \
        "test_all_integers_positive transposition failed"


def test_with_negative_integers():
    assert transposition(((1, 1, 1), (2, 2, 2), (-3, -3, -3))) == ((1, 2, -3), (1, 2, -3), (1, 2, -3)), \
        "test_with_negative_integers transposition failed"


def test_with_floats():
    assert transposition(((1.2, 2.2, 3.2), (4.1, 5, 6), (7, 8, 9))) == ((1.2, 4.1, 7), (2.2, 5, 8), (3.2, 6, 9)), \
        "test_with_floats transposition failed"


def test_with_letters():
    assert transposition((('a', 'b', 'c'), (2, 2, 2), (-3, -3, -3))) == (('a', 2, -3), ('b', 2, -3), ('c', 2, -3)), \
        "test_with_letters transposition failed"


if __name__ == '__main__':
    pytest.main()
