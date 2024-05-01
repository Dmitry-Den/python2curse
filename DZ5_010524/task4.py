"""Создайте функцию генератор чисел Фибоначчи"""

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Пример использования функции-генератора для вывода первых 50 чисел Фибоначчи
fib_gen = fibonacci_generator()
for _ in range(50):
    print(next(fib_gen))
