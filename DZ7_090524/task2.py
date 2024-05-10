#Напишите функцию группового переименования файлов. Она должна:
#a. принимать параметр желаемое конечное имя файлов. При переименовании в конце 
# имени добавляется порядковый номер.
#b. принимать параметр количество цифр в порядковом номере.
#c. принимать параметр расширение исходного файла. Переименование должно работать
# только для этих файлов внутри каталога.
#d. принимать параметр расширение конечного файла.
#e. принимать диапазон сохраняемого оригинального имени. Например для диапазона 
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


import os

def group_rename_files(target_name, digits_count, original_extension, new_extension, name_range=None):
    files = [f for f in os.listdir() if f.endswith(original_extension)]

    if name_range:
        start, end = name_range
    else:
        start, end = 0, None

    counter = 1
    for file_name in files[start:end]:
        new_file_name = target_name + str(counter).zfill(digits_count) + new_extension
        os.rename(file_name, new_file_name)
        counter += 1

# Пример использования функции
group_rename_files("new_file", 3, ".txt", ".docx", name_range=(1, 4))