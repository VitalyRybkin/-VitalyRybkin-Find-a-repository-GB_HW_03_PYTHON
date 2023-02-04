"""
Требуется найти в массиве A[1..N] самый близкий по
величине элемент к заданному числу X. Пользователь в первой строке
вводит натуральное число N – количество элементов в массиве. В
последующих строках записаны N целых чисел Ai. Последняя строка
содержит число X

5
1 2 3 4 5
6
-> 5
"""

from CHECK_INPUT import check_num_input
from random import randint

while True:
    N = input('Введите количество элементов в массиве или "Q": ')
    N = check_num_input(N)
    if N == 'Q':
        exit()
    N = int(N)

    X= input('Введите число для проверки или "Q": ')
    X = check_num_input(X)
    if X == 'Q':
        exit()
    X = int(X)

    my_list = [randint(1, 5) for _ in range(N)]
    min_diff, res = abs(X - my_list[0]), my_list[0]
    for _ in my_list:
        if min_diff > abs(_ - X):
            min_diff = abs(_ - X)
            res = _


    print(my_list)
    print(f'Самое близкое к {X} число {res}')