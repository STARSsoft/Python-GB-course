'''
 Напишите следующие функции:
- Нахождение корней квадратного уравнения
- Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
- Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
- Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

'''
import csv
import random
import json
from pathlib import Path
from typing import Callable


def gen_cvs(path_):

    with open(f'{path_}.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for _ in range(50):
            a = random.randint(-2, 2)
            b = random.randint(-10, 2)
            c = random.randint(-10, 10)
            writer.writerow([a, b, c])


def decor_cvs_sol(func: Callable):
    
    def wrapper(path_):
        sols = []
        with open(f'{path_}.csv', "r", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                a, b, c = map(int, row)
                sols.append(func(a, b, c))
        return sols
    return wrapper

def json_save_sols (save_path):
    def deco (func:Callable):  
        def wrapper(path_):
            i=0
            sols = dict()
            with open(f'{path_}.csv', "r", newline="") as f:
                reader = csv.reader(f)
                for row in reader:
                    a, b, c = map(int, row)
                    sols[i]=f" param: {a=} {b=} {c=} solution: {func(a, b, c)}"
                    i+=1
            with open(f'{save_path}.json', 'w') as json_file:
                json.dump(sols, json_file, indent=4)        
        return wrapper
    return deco

def quadr_sol(a, b, c):
    
    if a == 0 and b == 0 and c == 0:
        return "Any"

    if a == 0 and b != 0 and c == 0:
        return 0.0
    
    if a == 0 and b == 0 and c != 0:
        return None
    
    if a == 0 and b != 0 and c != 0:
        sol = float(-c/b)
        return f"{sol:.2f}"
    
    dscr = float(b**2-4*a*c)

    if dscr < 0:
        return None
    if dscr == 0:
        sol = float(-b/(2*a))
        return f"{sol:.2f}"
    else:
        sol1 = float((-b+dscr**0.5)/(2*a))
        sol2 = float((-b-dscr**0.5)/(2*a))
        return (f"{sol1:.2f}", f"{sol2:.2f}")


if __name__ == "__main__":
    
    my_path = Path().cwd() / "homework09"/"my_cvs" # указываем путь для cvs файла с которым будем работать
    gen_cvs(my_path) # генерируеи  csv файл.

    cvs_sols=decor_cvs_sol(quadr_sol) # создаем объект, который решает заданное уравнение(квадратное) из csv файла
    print(cvs_sols(Path().cwd() / "homework09"/"my_cvs")) # передаем объекту путь к csv файлу, печатаем решения

    save_json=json_save_sols(Path().cwd() / "homework09"/"my_json")(quadr_sol) # создаем объект, который будет сохранять решения в json по указанному пути
    save_json(my_path) # передаем объекту путь к сvs файлу, получаем файл с решениями

  
