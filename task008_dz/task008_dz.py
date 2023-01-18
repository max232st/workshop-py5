# Создайте программу для игры в "Крестики-нолики".

lst = list(range(1, 10))


def board(lst):
    print("___________________")
    for i in range(3):
        print("| ", lst[0 + i * 3], " | ", lst[1 + i * 3], " | ", lst[2 + i * 3], " | ")
        print("|_____|_____|_____|")


def player_input(pl_mark):
    valid = False
    while not valid:
        pl_input = input("В какой клетке поставим " + pl_mark + "? ")
        try:
            pl_input = int(pl_input)
        except:
            print("Ошибка ввода!")
            continue
        if pl_input >= 1 and pl_input <= 9:
            if str(lst[pl_input - 1]) not in "XO":
                lst[pl_input - 1] = pl_mark
                valid = True
            else:
                print("Эта клетка занята!")
        else:
            print("Ошибка ввода!")


def check(lst):
    win_line = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )
    for i in win_line:
        if lst[i[0]] == lst[i[1]] == lst[i[2]]:
            return lst[i[0]]
    return False


def main(lst):
    i = 0
    win = False
    while not win:
        board(lst)
        if i % 2 == 0:
            player_input("X")
        else:
            player_input("O")
        i += 1
        if i > 4:
            marker = check(lst)
            if marker:
                print()
                print(marker, "выиграл!!!")
                win = True
                break
        if i == 9:
            print("Ничья!")
            break
    board(lst)


main(lst)
