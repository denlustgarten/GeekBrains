"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран."""

from typing import List
from random import randint


def write_file(filename: str) -> None:
    try:
        sequence = [str(randint(-80, 80)) for _ in range(randint(15, 20))]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(" ".join(sequence))
    except IOError as e:
        print(e)


def read_file(filename: str) -> List[int]:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            sequence = f.read()
        return [int(val) for val in sequence.split()]
    except IOError as e:
        print(e)
        return []


if __name__ == '__main__':
    write_file('test_5.txt')
    seq = read_file('test_5.txt')
    print(f'Последовательность: {seq}')
    seq_sum = sum(seq)
    print(f'Сумма чисел: {seq_sum}')
