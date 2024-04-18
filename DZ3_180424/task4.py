# Создайте словарь со списком вещей для похода в качестве ключа и их массой
# в качестве значения. Определите какие вещи влезут в рюкзак передав его 
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
def fill_backpack(items, max_weight):
    # Функция для определения возможных вариантов комплектации рюкзака
    def fill_backpack_recursive(remaining_items, current_weight, current_items):
        if not remaining_items or current_weight >= max_weight:
            return [current_items] if current_weight <= max_weight else []
        
        item, weight = remaining_items[0]
        
        # Рекурсивно исследуем два случая: включение текущего предмета и его исключение
        with_item = fill_backpack_recursive(remaining_items[1:], current_weight + weight, current_items + [item])
        without_item = fill_backpack_recursive(remaining_items[1:], current_weight, current_items)
        
        return with_item + without_item
    
    items_list = list(items.items())
    backpack_options = fill_backpack_recursive(items_list, 0, [])
    
    return backpack_options

# Запросим у пользователя словарь с вещами и их массой
items = {}
while True:
    item_name = input("Введите название вещи (или 'стоп' для завершения): ")
    if item_name.lower() == 'стоп':
        break
    item_weight = float(input("Введите массу вещи в кг: "))
    items[item_name] = item_weight

# Запросим у пользователя максимальную грузоподъемность рюкзака
max_weight = float(input("Введите максимальную грузоподъемность рюкзака: "))

# Найдем все возможные варианты комплектации рюкзака
backpack_options = fill_backpack(items, max_weight)

print("Возможные варианты комплектации рюкзака:")
for option in backpack_options:
    print(option)