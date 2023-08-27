# Решить задачи, которые не успели решить на семинаре.
# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def formatter(a, b):
    c = a*b
    if (c < 10):
        return f"{b} x {a} =  {c}"
    elif (a < 10):
        return f"{b} x {a} = {c}"
    else:
        return f"{b} x {a}= {c}"


print("\n \t \t ТАБЛИЦА УМНОЖЕНИЯ \n")

for a in range(2, 11):
    for b in range(2, 6):
        print(formatter(a, b), end="\t")
    print()
print()
for a in range(2, 11):
    for b in range(6, 10):
        print(formatter(a, b), end="\t")
    print()
print()
