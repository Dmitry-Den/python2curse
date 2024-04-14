# Напишите программу, которая принимает две строки вида “a/b” - дробь
# с числителем и знаменателем. Программа должна возвращать сумму и 
# произведение* дробей. Для проверки своего кода используйте модуль fractions
from fractions import Fraction

def operate_fractions(fraction1, fraction2):
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))

    frac1 = Fraction(num1, denom1)
    frac2 = Fraction(num2, denom2)

    sum_frac = frac1 + frac2
    product_frac = frac1 * frac2

    return sum_frac, product_frac

# Ввод пользовательских данных
fraction1 = input("Введите первую дробь в формате a/b: ")
fraction2 = input("Введите вторую дробь в формате a/b: ")

# Вычисление суммы и произведения дробей
sum_result, product_result = operate_fractions(fraction1, fraction2)

# Вывод результатов
print(f"Сумма дробей: {sum_result}")
print(f"Произведение дробей: {product_result}")