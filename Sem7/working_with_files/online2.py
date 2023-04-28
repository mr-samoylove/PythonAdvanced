# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.
import random
from random import randint, choices

VOWELS = 'аеиоуяюёэы'
CONSONANTS = ''.join([chr(ch) for ch in range(ord("а"), ord("я") + 1) if chr(ch) not in VOWELS])


def make_random_name(amount_of_names: int):
    count = 0
    all_names = []
    while count != amount_of_names:
        word_len = randint(4, 7)
        word = random.choices(VOWELS + CONSONANTS, k=word_len)
        if any(ch in VOWELS for ch in word):
            all_names.append(''.join(word).capitalize() + '\n')
            count += 1
    with open('names.txt', 'a', encoding='utf-8') as f:
        f.writelines(all_names)


make_random_name(10)



