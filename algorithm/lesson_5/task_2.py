"""Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа. Например,
пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]."""
from collections import deque, ChainMap
from typing import Deque, List
from functools import reduce

hex_to_dec = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
}

dec_to_hex = {
    0: '0',
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F',
}

my_map = ChainMap(hex_to_dec, dec_to_hex)


def add(num_1: Deque, num_2: Deque) -> Deque:
    old_remain = 0
    num_3 = deque()

    while num_1 and num_2:
        tetrad_1 = num_1.pop()
        tetrad_2 = num_2.pop()

        sum_1_2 = my_map.get(tetrad_1) + my_map.get(tetrad_2) + old_remain
        tetrad_3 = sum_1_2 % 16

        num_3.extendleft(my_map.get(tetrad_3))
        old_remain = sum_1_2 // 16

    if num_1:
        while num_1:
            sum_1_2 = my_map.get(num_1.pop()) + old_remain
            num_3.extendleft(my_map.get(sum_1_2 % 16))
            old_remain = sum_1_2 // 16
    else:
        while num_2:
            sum_1_2 = my_map.get(num_2.pop()) + old_remain
            num_3.extendleft(my_map.get(sum_1_2 % 16))
            old_remain = sum_1_2 // 16

    if old_remain:
        num_3.extendleft(my_map.get(old_remain))
    return num_3


def mult(num_1: List, num_2: List) -> Deque:
    deque_arr = []
    k = 0
    remain = 0
    for val_2 in num_2[::-1]:
        temp = deque(['0' for _ in range(k)])
        for val_1 in num_1[::-1]:
            mul = my_map.get(val_2) * my_map.get(val_1) + remain
            temp.extendleft(my_map.get(mul % 16))
            remain = mul // 16
        if remain:
            temp.extendleft(my_map.get(remain))
        deque_arr.append(temp)
        remain = 0
        k += 1

    result = reduce(add, deque_arr)
    return result


if __name__ == '__main__':
    """Я не стал заморачиваться на счет форматированного вывода, думаю для данной задачи это не играет роли.
    Еще уверен, что можно написать функцию суммы более оптимизировано, но пока хватило фантазии только на такое)"""

    number_1 = deque(input("Введите первое число суммы: "))
    number_2 = deque(input("Введите второе число суммы: "))
    print('Результат сложения: ', *add(number_1, number_2), end='\n\n')

    number_1 = list(input("Введите первое число произведения: "))
    number_2 = list(input("Введите второе число произведения: "))
    print('Результат умножения: ', *mult(number_1, number_2))
