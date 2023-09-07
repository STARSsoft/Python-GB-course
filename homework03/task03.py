'''
3. Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.

'''
my_items = {
    "палатка": 3000,
    "спальник": 2000,
    "котелок": 800,
    "лопата": 1000,
    "веревка": 1200,
    "фонарик": 400,
    "нож": 200,
    "телефон": 125
}


def find_comb(items, max_w):
    sorted_items = sorted(items.items(), key=lambda x: x[1], reverse=True)
    
    def find_com_rec(cur_w, cur_comb, rem_items):
        if cur_w <= max_w:
            result.append(cur_comb)

        for i in range(len(rem_items)):
            new_comb = cur_comb + [rem_items[i]]
            new_w = cur_w + rem_items[i][1]
            new_rem = rem_items[i + 1:]
            find_com_rec(new_w, new_comb, new_rem)

    result = []
    find_com_rec(0, [], sorted_items)
    
    # удаляем подмножества
    final_result = []
    to_remove = set()
    for i in range(len(result)):
        is_subset = False
        for j in range(len(result)):
            if i == j:
                continue
            if set(result[i]).issubset(set(result[j])):
                is_subset = True
                to_remove.add(i)
                break
        if not is_subset:
            final_result.append(result[i])
    
    # удаляем подмножества из исходного списка
    final_result = [item for i, item in enumerate(result) if i not in to_remove]
    return final_result


combinators=find_comb(my_items,4000)
for c in combinators:
    print(c)



