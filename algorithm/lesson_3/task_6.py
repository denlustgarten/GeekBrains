"""В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным
элементами. Сами минимальный и максимальный элементы в сумму не включать."""

from random import randint

SIZE_ARR = 10
MIN_ITEM = -10
MAX_ITEM = 10
matrix = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_ARR)]

print(matrix)

min_val = (matrix[0], 0)
max_val = (matrix[0], 0)

for ind, val in enumerate(matrix[1:], start=1):
    if val < min_val[0]:
        min_val = (val, ind)
    elif val > max_val[0]:
        max_val = (val, ind)

sum_in_range = 0
if min_val[1] < max_val[1]:
    for val in matrix[min_val[1] + 1:max_val[1]]:
        sum_in_range += val
else:
    for val in matrix[max_val[1] + 1:min_val[1]]:
        sum_in_range += val

print(f'Сумма элементов, находящихся между первым минимальным и первым максимальным: {sum_in_range}')
