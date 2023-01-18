import random


def winner(flag):
    if flag:
        print("Выиграл первый игрок")
    else:
        print("Выиграл второй игрок")


def igra(n, flag):
    m = 28

    if n <= m:
        m = n
    if n <= 0:
        return not flag
    print(f"Осталось {n} конфет")

    if flag:
        print(f"Ходит первый игрок")
    else:
        print("Ходит второй игрок")

    while (x := int(input(f"введите количество конфет от 1 до {m} "))) > m:
        print("Еще раз")

    #  чтобы выиграл игрок, последний взявший конфету, ему необходимо взять в свой первый ход n % (m +1) конфет,
    #  затем он должен брать x = 29 - x2 конфет, где x2 - конфеты, который взял соперник в предыдущий ход
    return igra(n - x, not flag)


flag = random.randint(0, 1)
winner(igra(100, flag))
