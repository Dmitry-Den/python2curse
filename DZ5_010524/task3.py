""" Напишите однострочный генератор словаря, который принимает на вход три 
списка одинаковой длины: имена str, ставка int, премия str с указанием 
процентов вида “10.25%”. В результате получаем словарь с именем в качестве 
ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка 
умноженная на процент премии """

names = input("Введите имена через пробел: ").split()
rates = list(map(int, input("Введите зп через пробел: ").split()))
awards = input("Введите премии в процентах через пробел: ").split()

result = {name: int(rate) * float(award.strip("%")) / 100 for name, rate, award in zip(names, rates, awards)}
print(result)

