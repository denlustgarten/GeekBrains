""" Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться
только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого)
деление клеток, соответственно."""

from random import randint


class Cell:
    def __init__(self, core_num: int):
        self.__core_num = core_num

    def __add__(self, other):
        return Cell(self.__core_num + other.__core_num)

    def __sub__(self, other):
        res = self.__core_num - other.__core_num
        if res > 0:
            self.__core_num = res
        else:
            print("Cell number of first obj must be greater (obj_1.cell_num > obj_2.cell_num)")

    def __mul__(self, other):
        return Cell(self.__core_num * other.__core_num)

    def __truediv__(self, other):
        return Cell(self.__core_num // other.__core_num)

    def make_order(self, core_in_line):
        if core_in_line <= 0:
            raise ValueError(f'Cores_in_line must be above zero, but {core_in_line} was given')
        return f'{"*" * core_in_line}\n' * (
                self.__core_num // core_in_line) + f'{"*" * (self.__core_num % core_in_line)}\n'

    def __str__(self):
        return str(self.__core_num)


def test(num_of_rep=3):
    try:
        # Create random num of cell with random cores num
        cells = [Cell(randint(1, 25)) for i in range(randint(10, 20))]
        rep_counter: int

        for rep_counter in range(num_of_rep):
            # Choose two random cells
            cell_1_idx, cell_2_idx = randint(0, len(cells) - 1), randint(0, len(cells) - 1)
            cell_1, cell_2 = cells[cell_1_idx], cells[cell_2_idx]

            print(f'Start values for cells:\n{cell_1}, {cell_2}')
            print(f'add(): {cell_1 + cell_2}')
            cell_1 - cell_2
            print(f'sub(): {cell_1}')
            print(f'mul(): {cell_1 * cell_2}')
            print(f'div(): {cell_1 / cell_2}')

            sym_in_line = randint(0, 10)
            print(f'{sym_in_line} cores in a line:\n{cell_2.make_order(sym_in_line)}')
    except Exception as ex:
        print(f'My_ex: {ex}')


if __name__ == '__main__':
    test(10)
