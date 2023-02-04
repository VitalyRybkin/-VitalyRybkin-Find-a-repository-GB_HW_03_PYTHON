"""
Требуется вычислить, сколько раз встречается некоторое
число X в массиве A[1..N]. Пользователь в первой строке вводит
натуральное число N – количество элементов в массиве. В последующих
строках записаны N целых чисел Ai. Последняя строка содержит число X

5
1 2 3 4 5
3
-> 1

"""

from CHECK_INPUT import check_num_input
from random import randint

while True:
    try:
        N = input('Введите количество элементов в массиве или "Q": ')
        N = check_num_input(N)
        if N == 'Q':
            exit()
        N = int(N)
    except KeyboardInterrupt:
        pass

    X= input('Введите число для проверки или "Q": ')
    X = check_num_input(X)
    if X == 'Q':
        exit()
    X = int(X)

    my_list = [randint(1, 5) for _ in range(N)]
    counter = 0
    for _ in my_list:
        if _ == X:
            counter += 1

    print(my_list)
    print(counter)

