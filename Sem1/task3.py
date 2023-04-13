# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print("Загадано число от 0 до 1000")

up = UPPER_LIMIT
down = LOWER_LIMIT
for i in range(1, 11):
    mid = (up + down) // 2
    print(f"Попытка {i}. Это число {mid}?")
    if num == mid:
        print("Да, число угадано")
        break
    elif num > mid:
        print("\tНет, Загаданное число больше")
        down = mid + 1
    else:
        print("\tНет, Загаданное число меньше")
        up = mid - 1