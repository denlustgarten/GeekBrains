"""6. Реализовать два небольших скрипта:
    итератор, генерирующий целые числа, начиная с указанного;
    итератор, повторяющий элементы некоторого списка, определённого заранее.
    Подсказка: используйте функцию count() и cycle() модуля itertools.
    Обратите внимание, что создаваемый цикл не должен быть бесконечным.
    Предусмотрите условие его завершения.
    #### Например, в первом задании выводим целые числа, начиная с 3.
    При достижении числа 10 — завершаем цикл. Вторым пунктом необходимо
    предусмотреть условие, при котором повторение элементов списка прекратится.
"""

from itertools import count, cycle


def int_gen(start_: int, stop_: int):
    for num in count(start_):
        yield num
        if num == stop_:
            break


def repeat_iter(arr, stop_: int):
    for num in cycle(arr):
        yield num
        if arr.index(num) == stop_:
            break


# generator 1
start = 3
stop = 10
int_generator = int_gen(start, stop)
print(list(int_generator))

# generator 1
sequence = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
rep_iter = repeat_iter(sequence, stop_=10)
print(list(rep_iter))
