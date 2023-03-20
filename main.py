import random
from random import randint
def zadanie_1():
    print("Задание1")
    a = 5
    list = []
    for i in range(a):
        item = randint(1,99)
        list.append(item)
    n = int(input("введите число"))
    if n in list:
        print("Поздравляю, вы угадали число", *list)
    else:
        print("нет такого числа", *list)




from random import randint
def zadanie_2():
    print("Задание 2")
    b = 5
    list = []
    for i in range(b):
        item = randint(1,99)
        list.append(item)
    print(*filter(lambda x : list.count(x) > 1, list))

def zadanie_3():
    print("Задание 3")
    ned = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    d = int(input("сколько выходных?"))
    for i in ned:
        print("Рабочие", *ned[:-d])
        print("Выходные", *ned[-d:])
        break

from random import sample
def zadanie_4():
    print("Задание4")
    list =["Бурашников" , "Троицкая" , "Чернейкина"]
    list2 = ["Москвитина", "Рогозин" , "Лащев"]
    team = tuple(random.sample(list,2)+random.sample(list2,2))
    print(*list)
    print(*list2)
    print(*team)
    print(len(team))
    team = tuple(sorted(team))
    if "Иванов" in team:
         print(team).count("Иванов")
    else:
        print("нету")


zadanie_1(), zadanie_2(), zadanie_3(), zadanie_4()