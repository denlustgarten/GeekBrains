"""Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив
надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля), т.к.
именно в этих позициях первого массива стоят четные числа."""

from random import randint

SIZE_ARR = 10
MIN_ITEM = -10
MAX_ITEM = 10
matrix = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_ARR)]

print(matrix)

index_arr = []
for index, val in enumerate(matrix):
    if val % 2 == 0:
        index_arr.append(index)

print(f'Индексы четных элементов массива: {index_arr}')
