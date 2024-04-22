#Напишите функцию для транспонирования матрицы

def transpose_matrix():
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Введите элемент [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)

    transposed_matrix = [[matrix[j][i] for j in range(rows)] for i in range(cols)]

    print("Исходная матрица:")
    for row in matrix:
        print(row)

    print("Транспонированная матрица:")
    for row in transposed_matrix:
        print(row)

transpose_matrix()