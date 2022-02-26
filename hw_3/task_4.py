"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
При решении задания нужно обойтись без встроенной функции возведения числа в степень."""


def pow_1(x: float, y: int) -> float:
    return x ** y


def pow_2(x: float, y: int) -> float:
    result = 1
    if y < 0:
        for i in range(abs(y)):
            result /= x
    else:
        for i in range(y):
            result *= x
    return result


if __name__ == '__main__':
    try:
        a = float(input("Введите основание: "))
        b = int(input("Введите степень: "))
        print(pow_1(a, b))
        print(pow_2(a, b))
    except ValueError:
        print('Input error: incorrect arguments')
