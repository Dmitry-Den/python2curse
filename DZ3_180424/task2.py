# Дан список повторяющихся элементов. Вернуть список с дублирующимися 
# элементами. В результирующем списке не должно быть дубликатов.

def find_duplicates_and_remove(input_list):
    duplicates = []
    unique_elements = []
    
    for element in input_list:
        if input_list.count(element) > 1 and element not in duplicates:
            duplicates.append(element)
    
    for element in input_list:
        if element not in duplicates:
            unique_elements.append(element)
    
    return duplicates, unique_elements

user_input = input("Введите список элементов через пробел: ").split()
duplicates, unique_elements = find_duplicates_and_remove(user_input)

print("Дублирующиеся элементы:", duplicates)
print("Оставшиеся элементы:", unique_elements)