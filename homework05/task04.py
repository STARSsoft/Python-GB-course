'''
Создайте функцию-генератор. 
Функция генерирует N простых чисел, начиная с числа 2.
Для проверки числа на простоту используйте правило: «число является простым, если делится 
нацело только на единицу и на себя».
'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def my_gen(n):
    i=0
    numb=2
    while (i<n):
        if is_prime(numb): 
            yield numb
            i+=1
        numb+=1

n=10           
for i in my_gen(n):
    print (i, end=" ")
