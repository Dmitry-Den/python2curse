def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
        
        if a != b and a != c and b != c:
            print("Треугольник разносторонний")
        elif a == b == c:
            print("Треугольник равносторонний")
        else:
            print("Треугольник равнобедренный")
    else:
        print("Треугольник с такими сторонами не существует")

# Ввод сторон треугольника
a = float(input("Введите длину стороны a: "))
b = float(input("Введите длину стороны b: "))
c = float(input("Введите длину стороны c: "))

check_triangle(a, b, c)