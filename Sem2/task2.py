# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from math import gcd
from fractions import Fraction

a1, a2 = map(int, input("Введите первую дробь в виде a/b: ").split('/'))
b1, b2 = map(int, input("Введите вторую дробь в виде a/b: ").split('/'))

lcm = (a2 * b2) // gcd(a2, b2)
print(f"Сумма кастомной функции равна: {a1 * (lcm // a2) + b1 * (lcm // b2)}/{lcm}")

fr1, fr2 = Fraction(a1, a2), Fraction(b1, b2)
print(f"Сумма встроенной функции равна: {fr1 + fr2}")

up = a1 * b1
down = a2 * b2
g = gcd(up, down)
print(f"Произведение кастомной функции равно: {up // g}/{down // g}")
print(f"Произведение встроенной функции равно: {fr1 * fr2}")