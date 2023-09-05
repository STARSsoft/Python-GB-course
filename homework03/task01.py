'''
1. Дан список повторяющихся элементов. Вернуть список
с дублирующимися элементами. В результирующем списке
не должно быть дубликатов.

'''
my_list=[1,2,2,3,"5",5,6,"kot","kot"]
print("Было: " + str(my_list))
my_set=set()
for  item in my_list:
    if my_list.count(item)!=1: my_set.add(item)
my_list=(list(my_set))
print("Стало: " +  str(my_list))
