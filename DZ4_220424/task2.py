"""Напишите функцию принимающую на вход только ключевые параметры и 
возвращающую словарь, где ключ — значение переданного аргумента, а значение — 
имя аргумента. Если ключ не хешируем, используйте его строковое представление."""

def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if isinstance(key, (int, float, str, tuple)):
            key_str = str(key)
        else:
            key_str = key
        result[key_str] = value

    return result

# Пример использования функции
result_dict = create_dict(a=1, b='hello', c=(1, 2), d=3.14)
print(result_dict)