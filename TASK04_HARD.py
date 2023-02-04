"""
Задача HARD необязательная Имеется список чисел.
Создайте список, в который попадают числа, описывающие максимальную возрастающую последовательность.
Порядок элементов менять нельзя.
Одно число - это не последовательность.

Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
[1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
[1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]
"""
import random
import copy

while True:
    choose_list = {
        1: [1, 5, 2, 3, 4, 6, 1, 7],
        2: [1, 5, 2, 3, 4, 1, 7, 8 ,15 ,1],
        3: [1, 5, 3, 4, 1, 7, 8 ,15 ,1 ],
        4: [random.randint(1, 10) for i in range(15)],
    }

    n = input('Введите номер списка или "Q": ')
    if n == 'Q':
        exit()
    n = int(n)
    inspect_list = choose_list[n]

    counter = max_len = 0
    res = []
    check_list = []
    print(inspect_list)
    for i in range(len(inspect_list)):
        for j in range(i, len(inspect_list) + 1):
            counter = 0
            check_list = inspect_list[i:j + 1]
            if max(check_list) - min(check_list) == len(set(check_list)) - 1:
                counter = len(set(check_list)) - 1
                if counter > max_len:
                    check_list.sort()
                    max_len = counter
                    res = check_list[0::len(check_list)-1]

    print('Первая наибольшая возрастающая последовательность в списке: ', res)

