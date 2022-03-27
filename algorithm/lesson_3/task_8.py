"""Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать
ее в последнюю ячейку строки. В конце следует вывести полученную матрицу."""

matrix = []

for i in range(5):
    sum_str = 0
    matrix.append([int(val) for val in input(f'Введите 3 значения {i + 1}-й строки через пробел: ').split()])
    for val in matrix[i]:
        sum_str += val

    matrix[i].append(sum_str)

for item in matrix:
    for val in item:
        print(f'{val:>5}', end='')
    print()
