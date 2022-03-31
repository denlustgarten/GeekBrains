"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""

# Вывод по работе в самом низу

import timeit
import cProfile
import sys
import matplotlib.pyplot as plt
from random import randint, seed

sys.setrecursionlimit(5000)

SIZE_ARR = 10
MIN_ITEM = 0
MAX_ITEM = 1000
FIND_NUM = 4
find_dig = 4


def dig_count_0(sequence, find_dig, left_border=0, count=0):
    if left_border != len(sequence):
        num = abs(sequence[left_border])
        while num > 0:
            dig = num % 10
            num //= 10
            if dig == find_dig:
                count += 1
        return dig_count_0(sequence, find_dig, left_border + 1, count)
    else:
        return count


def dig_count_1(sequence, find_dig):
    count = 0
    for num in sequence:
        dig_arr = list(str(num))
        # print(dig_arr)
        count += dig_arr.count(str(find_dig))
    return count


def dig_count_2(sequence, find_dig):
    count = 0
    for item in sequence:
        val = abs(item)
        while val != 0:
            dig = val % 10
            val //= 10
            if dig == find_dig:
                count += 1
    return count


def dig_count_3(sequence, find_dig):
    seq_in_str = ''.join([str(item) for item in sequence])
    count = seq_in_str.count(str(find_dig))
    return count


def test_func(func0, func1, func2, func3, min_, max_, size, find_dig):
    seq = [randint(min_, max_) for _ in range(size)]
    # print(seq)
    result_0 = func0(seq, find_dig)
    result_1 = func1(seq, find_dig)
    result_2 = func2(seq, find_dig)
    result_3 = func3(seq, find_dig)
    if result_0 == result_1 == result_2 == result_3:
        print(f'Functions is correct!\n'
              f'Result_1 = {result_0}, Result_1 = {result_1}, Result_2 = {result_2}, Result_3 = {result_3}')
    else:
        print(f'ERROR: Functions is not correct! \n'
              f'Result_0 = {result_0}, Result_1 = {result_1}, Result_2 = {result_2}, Result_3 = {result_3}')


if __name__ == '__main__':
    test_func(dig_count_0, dig_count_1, dig_count_2, dig_count_3, -1000, 1000, 1000, 5)

    time_func_0 = []
    time_func_1 = []
    time_func_2 = []
    time_func_3 = []
    # val_num = (10, 100, 1000, 5000, 10000, 30000, 60000, 100000)
    val_num = (10, 100, 300, 600, 1000, 2000)
    find_digit = 4

    '''
    Рекурсивная функция забивает стек и кладет программу при большой длине массива, поэтому я сделал небольшой костыль.
    Если смотреть график для больших значений, нужно раскомментировать 1-й val_num (c этими данными рекурсивную функция
    не замеряю)
   '''
    if max(val_num) <= 2000:
        for val in val_num:
            seed(1)
            seq0 = [randint(MIN_ITEM, MAX_ITEM) for _ in range(val)]
            time_ = timeit.timeit("dig_count_0(seq0, find_digit,0 , 0)", number=1000, globals=globals())
            print(f'dig_count_0(): arr length: {len(seq0):>6}, time: {time_} ')
            time_func_0.append(time_)
        print()

    for val in val_num:
        seed(1)
        seq1 = [randint(MIN_ITEM, MAX_ITEM) for _ in range(val)]
        time_ = timeit.timeit("dig_count_1(seq1, find_digit)", number=1000, globals=globals())
        print(f'dig_count_1(): arr length: {len(seq1):>6}, time: {time_} ')
        time_func_1.append(time_)
    print()

    for val in val_num:
        seed(1)
        seq2 = [randint(MIN_ITEM, MAX_ITEM) for _ in range(val)]
        time_ = timeit.timeit("dig_count_2(seq2, find_digit)", number=1000, globals=globals())
        print(f'dig_count_2(): arr length: {len(seq2):>6}, time: {time_} ')
        time_func_2.append(time_)

    print()
    for val in val_num:
        seed(1)
        seq3 = [randint(MIN_ITEM, MAX_ITEM) for _ in range(val)]
        time_ = timeit.timeit("dig_count_3(seq3, find_digit)", number=1000, globals=globals())
        print(f'dig_count_3(): arr length: {len(seq3):>6}, time: {time_} ')
        time_func_3.append(time_)

    if not time_func_0:
        plt.plot(0, 0, color='black', marker='o', linewidth=2, markersize=6)
    else:
        plt.plot(val_num, time_func_0, color='black', marker='o', linewidth=2, markersize=6)
    plt.plot(val_num, time_func_1, color='red', marker='o', linewidth=2, markersize=6)
    plt.plot(val_num, time_func_2, color='green', marker='o', linewidth=2, markersize=6)
    plt.plot(val_num, time_func_3, color='blue', marker='o', linewidth=2, markersize=6)
    plt.legend(['dig_count_0: recursion', 'dig_count_1: used list.count()',
                'dig_count_2: circle', 'dig_count_3: to string'])
    plt.show()

    sequence = [randint(MIN_ITEM, MAX_ITEM) for _ in range(1_000_000)]
    cProfile.run('dig_count_0(seq, 5)')
    cProfile.run('dig_count_1(seq, 5)')
    cProfile.run('dig_count_2(seq, 5)')
    cProfile.run('dig_count_3(seq, 5)')





'''
Результаты измерений
val_num = (10, 100, 300, 600, 1000, 2000)

dig_count_0(): arr length:     10, time: 0.0010352999961469322
dig_count_0(): arr length:    100, time: 0.010227799997664988
dig_count_0(): arr length:    300, time: 0.0331302999984473
dig_count_0(): arr length:    600, time: 0.06706069997744635
dig_count_0(): arr length:   1000, time: 0.11020819999976084
dig_count_0(): arr length:   2000, time: 0.23321480001322925

dig_count_1(): arr length:     10, time: 0.0011827000125776976
dig_count_1(): arr length:    100, time: 0.010239999974146485
dig_count_1(): arr length:    300, time: 0.029338199994526803
dig_count_1(): arr length:    600, time: 0.05874300000141375
dig_count_1(): arr length:   1000, time: 0.09920349999447353
dig_count_1(): arr length:   2000, time: 0.19273430001339875

dig_count_2(): arr length:     10, time: 0.0009379000111948699
dig_count_2(): arr length:    100, time: 0.008744899998418987
dig_count_2(): arr length:    300, time: 0.026878100004978478
dig_count_2(): arr length:    600, time: 0.05376720000640489
dig_count_2(): arr length:   1000, time: 0.09254069998860359
dig_count_2(): arr length:   2000, time: 0.1806254999828525

dig_count_3(): arr length:     10, time: 0.00037789999623782933
dig_count_3(): arr length:    100, time: 0.002498999994713813
dig_count_3(): arr length:    300, time: 0.007080799987306818
dig_count_3(): arr length:    600, time: 0.013618299999507144
dig_count_3(): arr length:   1000, time: 0.02344359998824075
dig_count_3(): arr length:   2000, time: 0.046457899996312335

val_num = (10, 100, 1000, 5000, 10000, 30000, 60000, 100000)

dig_count_1(): arr length:     10, time: 0.0010405000066384673
dig_count_1(): arr length:    100, time: 0.009619399992516264
dig_count_1(): arr length:   1000, time: 0.0957201000128407
dig_count_1(): arr length:   5000, time: 0.49393789999885485
dig_count_1(): arr length:  10000, time: 0.975001799990423
dig_count_1(): arr length:  30000, time: 2.908905499993125
dig_count_1(): arr length:  60000, time: 5.78197939999518
dig_count_1(): arr length: 100000, time: 9.838061700022081

dig_count_2(): arr length:     10, time: 0.0011366000107955188
dig_count_2(): arr length:    100, time: 0.009074400004465133
dig_count_2(): arr length:   1000, time: 0.09132760000647977
dig_count_2(): arr length:   5000, time: 0.4972748000000138
dig_count_2(): arr length:  10000, time: 0.8893571000080556
dig_count_2(): arr length:  30000, time: 2.6251586000144016
dig_count_2(): arr length:  60000, time: 5.363291600020602
dig_count_2(): arr length: 100000, time: 9.367739200009964

dig_count_3(): arr length:     10, time: 0.00035930000012740493
dig_count_3(): arr length:    100, time: 0.002361199993174523
dig_count_3(): arr length:   1000, time: 0.024648699996760115
dig_count_3(): arr length:   5000, time: 0.10869049999746494
dig_count_3(): arr length:  10000, time: 0.24806850001914427
dig_count_3(): arr length:  30000, time: 0.8159502999915276
dig_count_3(): arr length:  60000, time: 1.51072339998791
dig_count_3(): arr length: 100000, time: 2.7356395999959204
'''

'''
Отчет cProfile для функций: 
Запуски на массиве размером 1_000_000 кроме рекурсии

1) dig_count_0() (больше 2500 стек переполняется)
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.005    0.005 <string>:1(<module>)
   2501/1    0.005    0.000    0.005    0.005 task1.py:16(dig_count_0)
     2500    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
     2501    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

2) dig_count_1()
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.268    1.268 <string>:1(<module>)
        1    1.091    1.091    1.268    1.268 task1.py:29(dig_count_1)
        1    0.000    0.000    1.268    1.268 {built-in method builtins.exec}
  1000000    0.177    0.000    0.177    0.000 {method 'count' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

3) dig_count_2()
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.726    0.726 <string>:1(<module>)
        1    0.662    0.662    0.726    0.726 task1.py:38(dig_count_2)
  1000000    0.064    0.000    0.064    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.726    0.726 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

4) dig_count_3()
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.277    0.277 <string>:1(<module>)
        1    0.017    0.017    0.277    0.277 task1.py:50(dig_count_3)
        1    0.245    0.245    0.245    0.245 task1.py:51(<listcomp>)
        1    0.000    0.000    0.277    0.277 {built-in method builtins.exec}
        1    0.004    0.004    0.004    0.004 {method 'count' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.012    0.012    0.012    0.012 {method 'join' of 'str' objects}


Вывод: проведя замеры производительности 4 алгоритмов, выполняющих одну и ту же задачу, можно сделать следующие выводы:
    1) Все алгоритмы имеют сложность O(n). 
    2) Рекурсивный алгоритм для данной задачи подходит очень плохо и показывает худшие результаты.
    3) Алгоритм подсчета конкретной цифры в последовательности, методом преобразования ее в строку, является самым 
       быстрым (если брать не общую формулу сложности а реальные временные значения)
    4) Перед решением задач необходимо хотя бы формально оценить сложность алгоритма, после чего приступать к его
       реализации


'''
