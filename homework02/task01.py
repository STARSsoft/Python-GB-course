"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.

"""


def coder(n):
    if n < 10: return str(n)
    elif n == 10: return "a"
    elif n == 11: return "b"
    elif n == 12: return "c"
    elif n == 13: return "d"
    elif n == 14: return "e"
    else: return "f"


num = int(input("Введите число: "))
hnum = abs(num)
answ = ""
while hnum > 0:
    answ = coder(hnum % 16)+answ
    hnum //= 16  # hnum=hnum//16
if num < 0:
    answ = "-" + answ
print("Ответ: " + answ + " Проверка: " + hex(num))
