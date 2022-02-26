"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def div(num_1: float, num_2: float) -> float:
    try:
        return num_1 / num_2
    except ZeroDivisionError as e:
        print(f'div exception: {e}')


if __name__ == '__main__':
    try:
        a, b = [float(x) for x in input('Введите делимое и делитель: ').split()]
        print(div(a, b))
    except ValueError as e:
        print('Input error: incorrect arguments ')
