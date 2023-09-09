'''
2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''

def my_func_kwargs(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        if hashable(value):
            my_dict[value] = key
        else:
            my_dict[str(value)] = key
    return my_dict

def hashable(my_param):
    try:
        hash(my_param)
        return True
    except TypeError:
        return False


my_dict = {"int": 5, "float": 6.7, "string": "kot", "list": [
    1, 3], "tuple": (1, 2), "set": {1, 2, 3}, "dict": {"1": "kot", "2": 9.9}}

print(my_func_kwargs(**my_dict))
