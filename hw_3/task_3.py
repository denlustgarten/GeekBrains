"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов."""


def my_func(a_: float, b_: float, c_: float) -> float:
    my_list = sorted([a_, b_, c_])
    return sum(my_list[-2:])


if __name__ == '__main__':
    try:
        a, b, c = [float(x) for x in input("Введите через пробел 3 числа: ").split()]
        print(my_func(a, b, c))
    except ValueError:
        print('Input error: incorrect arguments')
