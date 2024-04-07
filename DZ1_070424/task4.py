#Задача 4. Программа загадывает число от 0 до 1000. Необходимо угадать число
# за 10 попыток. Программа должна подсказывать “больше” или “меньше” после 
# каждой попытки. Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
# from random import randint.

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num_to_guess = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num_to_guess = randint(LOWER_LIMIT, UPPER_LIMIT)
attempts = 10

print("Программа загадала число от", LOWER_LIMIT, "до", UPPER_LIMIT)
while attempts > 0:
    guess = int(input("Угадайте число: "))
    if guess < num_to_guess:
        print("Больше")
    elif guess > num_to_guess:
        print("Меньше")
    else:
        print("Поздравляем! Вы угадали число", num_to_guess)
        break
    attempts -= 1

if attempts == 0:
    print("Вы исчерпали все попытки. Загаданное число было", num_to_guess)