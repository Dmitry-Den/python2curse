"""2. Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце
 имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать
 только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона
 [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется 
 желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет
для работы с файлами.""" 

import os

def generate_files(file_name, directory, num_files):
    for i in range(1, num_files + 1):
        with open(os.path.join(directory, f'{file_name}_{i}.txt'), 'w') as file:
            file.write(f'This is file {i}')