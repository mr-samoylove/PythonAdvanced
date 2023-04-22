# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fib_generator():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b


fib_seq = fib_generator()

for _ in range(10):
    print(next(fib_seq))
