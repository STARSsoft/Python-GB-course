'''
✔ Три друга взяли вещи в поход. 
Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей.

'''
my_dict = {"Вася": ("палатка", "нож", "спальник"),
           "Петя": ("фонарь", "веревка", "телефон", "спальник"),
           "Коля": ("палатка", "фонарь", "телефон", "котелок", "спальник")}

# общие вещи, которые есть у всех
common_items = set(next(iter(my_dict.values())))
for name in my_dict.keys():
    common_items = common_items & set(my_dict[name])
print("Вещи у всех:", common_items)

all_items = set()
for items in my_dict.values():
    all_items.update(set(items))

# уникальные вещи

unique_items = set()
for item in all_items:
    count = 0
    for name in my_dict:
        if item in my_dict[name]:
            count += 1
            cur_friend = name
    if count == 1:
        unique_items.add((item, cur_friend))
print("Уникальные вещи и друзья, которые их взяли:", unique_items)

# Какие вещи есть у всех друзей кроме одного
missing_item = set()
for item in all_items:
    count = 0
    for name in my_dict:
        if item not in my_dict[name]:
            count += 1
            cur_friend = name
    if count == 1:
        missing_item.add((item, cur_friend))
print("Вещи есть у всех, кроме одного: ", missing_item)
