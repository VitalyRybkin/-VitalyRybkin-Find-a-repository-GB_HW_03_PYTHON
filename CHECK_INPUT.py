def check_num_input(n):
    while True:
        try:
            return int(n)
        except ValueError:
            n = input('Ошибка ввода! Введите число или "Q" для выхода: ')
            if n == 'Q':
                exit()


