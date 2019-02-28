import random
import sys


def create_lotto_list():
    list = [[], [], []]
    numbers = [i for i in range(1, 90)]
    for line in range(3):
        for _ in range(5):
            num = random.choice(numbers)
            numbers.remove(num)
            list[line].append(num)
        list[line].sort()
    return list


def print_lists(comp_list, user_list):
    print("---Компьютер---")
    for line in comp_list:
        print(line)
    print("-----Игрок-----")
    for line in user_list:
        print(line)


def user_interface(comp_list, user_list, barrel):
    print_lists(comp_list, user_list)
    print('Бочонок № ' + str(barrel))
    print('Зачеркнуть цифру? (y/n)')
    answer = input()
    while (answer != 'y') and (answer != 'n'):
        print('Ответьте y или n')
        answer = input()
    if answer == 'y':
        number_lines_with_barrel = 0
        for line in user_list:
            if barrel in line:
                number_lines_with_barrel += 1
        if number_lines_with_barrel == 0:
            print("Вы проиграли")
            sys.exit(0)
        else:
            for line in user_list:
                if barrel in line:
                    line[line.index(barrel)] = -1
    elif answer == 'n':
        for line in user_list:
            if barrel in line:
                print("Вы проиграли")
                sys.exit(0)


def comp_brain(comp_list, barrel):
    for line in comp_list:
        if barrel in line:
            line[line.index(barrel)] = -1


def win_chek(comp_list, user_list):
    comp_counter, user_counter = 0, 0
    for line in comp_list:
        comp_counter += line.count(-1)
    for line in user_list:
        user_counter += line.count(-1)
    if comp_counter == 15 and user_counter == 15:
        print("Ничья")
        sys.exit(0)
    elif comp_counter == 15:
        print("Компьютер выиграл!")
        sys.exit(0)
    elif user_counter == 15:
        print("Игрок выиграл!")
        sys.exit(0)


def main():
    complist = create_lotto_list()
    userlist = create_lotto_list()
    bag = [i for i in range(1, 90)]
    while bag:
        barrel = random.choice(bag)
        bag.remove(barrel)
        user_interface(complist, userlist, barrel)
        comp_brain(complist, barrel)
        win_chek(complist, userlist)
    print('Бочонки закончились')
    print('Сообщи разрабу, это ошибка')

if __name__ == '__main__':
    main()
