"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
"""

from typing import List
from random import randint

SIZE_ARR = 10
MIN_ITEM = -100
MAX_ITEM = 99

"""
Оптимизация:
1) внешний цикл динамический. Нет смысла каждый раз проходить до конца массива
2) Добавлена проверка на отсортированность на каждом n-ом шаге 
"""


def bubble_sort(array: List) -> None:
    n = 1
    while n < len(array):
        is_sort = 1
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                is_sort = 0
        if is_sort:
            return
        n += 1
        print(array)


if __name__ == '__main__':
    matrix = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_ARR)]
    print(matrix)

    bubble_sort(matrix)
    print(matrix)
