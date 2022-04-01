"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
Matrix (двух матриц). Результатом сложения должна быть новая матрица."""

from copy import deepcopy
from itertools import zip_longest


class Matrix:
    def __init__(self, matrix_):
        self.matrix = deepcopy(matrix_)

    def __str__(self):
        result_str = ''
        for string in self.matrix:
            for val in string:
                result_str += f'{val:>4}'
            result_str += '\n'
        return result_str

    @property
    def matrix_size(self):
        return len(self.matrix), len(self.matrix[0])

    def __add__(self, other):
        if self.matrix_size == other.matrix_size:
            sum_matrix = []
            for line_m1, line_m2 in zip(self.matrix, other.matrix):
                new_line = [sum(nums) for nums in zip_longest(line_m1, line_m2)]
                sum_matrix.append(new_line)
            return Matrix(sum_matrix)
        else:
            print('Addition of matrices of different sizes!')
            return None


if __name__ == '__main__':
    matr_1 = Matrix([[2, 4], [1, 2]])
    matr_2 = Matrix([[3, 4], [6, 5]])
    matr_3 = Matrix([[1, 1], [1, 7]])
    matr_4 = Matrix([[33, 44], [32, 41], [14, 26]])

    print(f'matr_1:\n{matr_1}')
    print(f'matr_2:\n{matr_2}')
    print(f'matr_3:\n{matr_3}')
    print(f'matr_4:\n{matr_4}')

    sum_matr_1_2 = matr_1 + matr_2
    print(f'sum_matr_1_2:\n{sum_matr_1_2}')

    sum_matr_2_3 = matr_2 + matr_3
    print(f'sum_matr_2_3:\n{sum_matr_2_3}')

    sum_matr_1_2_3 = matr_1 + matr_2 + matr_3
    print(f'sum_matr_1_2_3:\n{sum_matr_1_2_3}')

    sum_matr_1_4 = matr_1 + matr_4
    print(f'sum_matr_1_4:\n{sum_matr_1_4}')

