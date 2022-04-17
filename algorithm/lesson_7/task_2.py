"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from typing import List
from random import uniform

SIZE_ARR = 10
MIN_ITEM = 0
MAX_ITEM = 49


def merge_two_array(arr1: List, arr2: List) -> List:
    merge_arr = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merge_arr.append(arr1[i])
            i += 1
        else:
            merge_arr.append(arr2[j])
            j += 1

    if i < len(arr1):
        merge_arr.extend(arr1[i:])
    elif j < len(arr2):
        merge_arr.extend(arr2[j:])

    return merge_arr


def merge_sort(array: List) -> List:
    if len(array) == 1:
        return array
    middle = len(array) // 2
    left_array = merge_sort(array[:middle])
    right_array = merge_sort(array[middle:])
    return merge_two_array(left_array, right_array)


if __name__ == '__main__':
    matrix = [uniform(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_ARR)]
    print(matrix)
    print(merge_sort(matrix))
