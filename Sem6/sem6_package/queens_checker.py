import random


def check_coordinates(tuple_of_eight_coords: tuple) -> bool:
    if len(tuple_of_eight_coords) == 8 and all(len(pair) == 2 for pair in tuple_of_eight_coords):
        board = [[0] * 8 for _ in range(8)]
        for x, y in tuple_of_eight_coords:
            if board[x][y] == 1:  # если поле бьется или там уже стоит ферзь
                return False
            else:
                for i in range(8):
                    for j in range(8):
                        if i == x or j == y or x - y == i - j or x + y == i + j:  # помечаем все бьющиеся клетки
                            board[i][j] = 1
            # print_table(board)
        return True
    else:
        raise RuntimeError("Функция принимает кортеж из 8 пар чисел")


def print_table(table):
    for row in range(8):
        print(table[row])


def print_random_queens_boards(amount_of_boards: int):
    rows = list(range(8))
    cols = list(range(8))
    matches = 0
    while matches != amount_of_boards:
        random.shuffle(rows)
        random.shuffle(cols)
        board = tuple(zip(rows, cols))
        if check_coordinates(board):
            print(board)
            matches += 1


if __name__ == '__main__':
    # coords = ((0, 0), (1, 6), (2, 4), (3, 7), (4, 1), (5, 3), (6, 5), (7, 2))
    # print(check_coordinates(coords))
    print_random_queens_boards(4)
