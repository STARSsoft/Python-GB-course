"""
Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

"""
import fractions

def my_nod(a, b):
    """
    Быстрый алгоритм Евклида для нахождения НОД

    """
    a, b = abs(a), abs(b)
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a


def my_sum(first_fraction, second_fraction):
    a, b = map(int, first_fraction.split("/"))
    c, d = map(int, second_fraction.split("/"))
    num = a*d+c*b
    dem = d*b
    nod = my_nod(num, dem)
    num = num//nod
    dem = dem//nod
    if dem == 1:
        return f"{num}"
    return f"{num}/{dem}"


def my_mult(first_fraction, second_fraction):
    a, b = map(int, first_fraction.split("/"))
    c, d = map(int, second_fraction.split("/"))
    num = a*c
    dem = b*d
    nod = my_nod(num, dem)
    num = num//nod
    dem = dem//nod
    if dem == 1:
        return f"{num}"
    return f"{num}/{dem}"


ff = input("Введите первую дробь: ")
sf = input("Введите вторую дробь: ")

f1 = fractions.Fraction(ff)
f2 = fractions.Fraction(sf)

print(f" Cумма дробей равна: {my_sum(ff,sf)} Проверка: {f1+f2} ")
print(f" Произведение дробей равно: {my_mult(ff,sf)} Проверка: {f1*f2} ")
