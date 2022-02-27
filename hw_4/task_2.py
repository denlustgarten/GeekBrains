"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента."""

from random import randint


sequence = [randint(0, 100) for x in range(10)]
print(sequence)

sort_seq = [sequence[i + 1] for i in range(len(sequence) - 1) if sequence[i] < sequence[i + 1]]
print(sort_seq)
