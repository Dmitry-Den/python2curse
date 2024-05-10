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

def group_rename_files(desired_name, num_digits, original_extension, final_extension, name_range=None):
    files = [f for f in os.listdir() if f.endswith(original_extension)]

    count = 1
    for file in files:
        if name_range:
            original_name = file[name_range[0]-1:name_range[1]] + desired_name
        else:
            original_name = desired_name

        new_name = f"{original_name}_{str(count).zfill(num_digits)}.{final_extension}"
        os.rename(file, new_name)
        count += 1

# Пример использования функции
group_rename_files("234", 3, ".txt", "txt", name_range=(3, 6))
