"""Напишите функцию, которая принимает на вход строку - абсолютный путь до 
файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, 
расширение файла."""

def split_path(file_path):
    import os
    path, filename = os.path.split(file_path)
    filename, ext = os.path.splitext(filename)
    return path, filename, ext

file_path = "/home/user/docs/example.txt"
result = split_path(file_path)
print(result)