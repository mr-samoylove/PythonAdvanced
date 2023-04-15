# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
import itertools

MAX_WEIGHT = 6
things = dict(hammer=5, tent=10, rope=3, food=1, camera=2)

for i in range(1, len(things) + 1):
    for comb in itertools.combinations(things.items(), i):
        if sum(x[1] for x in comb) <= MAX_WEIGHT:
            print('combination:', *comb, sep=' ')

