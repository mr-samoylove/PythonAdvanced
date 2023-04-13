# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def hex_custom(n):
    digits = "0123456789abcdef"
    mod = n % 16
    rest = n // 16
    if not rest:
        return digits[mod]
    return hex_custom(rest) + digits[mod]


n = int(input("Введите число: "))

print(hex_custom(n))
print(hex(n))
