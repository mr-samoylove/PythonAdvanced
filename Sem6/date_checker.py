from sys import argv


def calend(date: str):
    day, month, year = map(int, date.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        else:
            if 1 <= day <= 28 + leap_year(year):
                return True
    return False


def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


if __name__ == '__main__':
    if len(argv) == 1:
        print("Передайте аргумент (дата в формате dd.mm.yyyy) через командную строку")
    else:
        print(calend(argv[1]))

