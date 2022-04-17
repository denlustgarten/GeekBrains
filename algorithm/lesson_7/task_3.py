"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""

from typing import List
from random import randint, uniform

SIZE_ARR = 7
MIN_ITEM = -100
MAX_ITEM = 100


def get_median(array: List) -> int:
    for i in range(len(array)):
        greater_count = 0
        less_count = 0
        equal_count = -1  # исключаем равенство с собой
        for j in range(len(array)):
            if array[j] > array[i]:
                greater_count += 1
            elif array[j] < array[i]:
                less_count += 1
            else:
                equal_count += 1
        if abs(greater_count - less_count) <= equal_count:
            return array[i]


if __name__ == '__main__':
    matrix = [randint(MIN_ITEM, MAX_ITEM) for _ in range(2 * SIZE_ARR + 1)]
    # matrix = [uniform(MIN_ITEM, MAX_ITEM) for _ in range(2 * SIZE_ARR + 1)]
    print(matrix)
    print(sorted(matrix))  # для проверки

    print(f'Медиана в массиве: {get_median(matrix)}')
