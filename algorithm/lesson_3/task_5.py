"""В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения."""

from random import randint

SIZE_ARR = 1000
MIN_ITEM = -10
MAX_ITEM = 10
matrix = [randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_ARR)]

print(matrix)

min_val = -1000
min_val_ind = -1
for ind, val in enumerate(matrix):
    if min_val < val < 0:
        min_val = val
        min_val_ind = ind

print(f'Максимальный отрицательный элемент: {min_val} \n'
      f'Индекс элемента в массиве (1-го встречающегося): {min_val_ind}')
