# 3. Добавьте в пакет, созданный на семинаре шахматный модуль. 
#Внутри него напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8
# можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана 
#расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг 
# друга. Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - 
# координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют 
# - ложь.
# 4. Напишите функцию в шахматный модуль. Используйте генератор случайных 
# чисел для случайной расстановки ферзей в задаче выше. Проверяйте различный 
# случайные варианты и выведите 4 успешных расстановки.

import random

def check_queens(arrangement):
    for i in range(len(arrangement)):
        for j in range(i+1, len(arrangement)):
            if arrangement[i][0] == arrangement[j][0] or arrangement[i][1] == arrangement[j][1] or abs(arrangement[i][0] - arrangement[j][0]) == abs(arrangement[i][1] - arrangement[j][1]):
                return False
    return True

def generate_random_arrangement():
    queens = []
    for _ in range(8):
        queens.append((random.randint(1, 8), random.randint(1, 8)))
    return queens

successful_arrangements = 0
while successful_arrangements < 4:
    random_arrangement = generate_random_arrangement()
    if check_queens(random_arrangement):
        print("Successful arrangement:", random_arrangement)
        successful_arrangements += 1
