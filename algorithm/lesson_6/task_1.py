"""8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры."""
import sys
from random import randint

SIZE_ARR = 10
MIN_ITEM = 0
MAX_ITEM = 1000
FIND_NUM = 4
find_dig = 4


def my_size(data, sum_mem=0):
    sum_mem += sys.getsizeof(data)
    if hasattr(data, '__iter__'):
        if hasattr(data, 'items'):
            for key, value in data.items():
                my_size(key, sum_mem)
                my_size(value, sum_mem)
        elif not isinstance(data, str):
            for item in data:
                my_size(item, sum_mem)
    return sum_mem


def memory_expended(func):
    def wrapper(*args, **kwargs):
        sum_memory = 0
        func_var_return = None
        func_return = func(*args, **kwargs)
        if isinstance(func_return, tuple):
            var_arr = func_return[0]
            func_var_return = func_return[1:]
        else:
            var_arr = func_return

        for name, var in var_arr.items():
            var_size = my_size(var)
            print(f'Переменная типа {type(var)} с именем "{name}" заняла {var_size} байт памяти')
            sum_memory += my_size(var)

        print(f'Функция :"{func.__name__}" заняла {sum_memory} байт памяти.')
        return tuple(func_var_return)

    return wrapper


@memory_expended
def dig_count_1(sequence, find_dig):
    count = 0
    for num in sequence:
        dig_arr = list(str(num))
        count += dig_arr.count(str(find_dig))
    return locals(), count


@memory_expended
def dig_count_2(sequence, find_dig):
    count = 0
    for item in sequence:
        val = abs(item)
        while val != 0:
            dig = val % 10
            dig //= 10
            if dig == find_dig:
                count += 1
    return locals(), count


@memory_expended
def dig_count_3(sequence, find_dig):
    seq_in_str = ''.join([str(item) for item in sequence])
    count = seq_in_str.count(str(find_dig))
    return locals(), count


if __name__ == '__main__':
    seq = [randint(MIN_ITEM, MAX_ITEM) for _ in range(1000)]

    print(dig_count_1(seq, 4))
    print(dig_count_2(seq, 4))
    print(dig_count_3(seq, 4))

""" 
Python interpreter: 3.9
OC: Ubuntu 21.10, 64-bit

Переменная типа <class 'list'> с именем "sequence" заняла 8856 байт памяти
Переменная типа <class 'int'> с именем "find_dig" заняла 28 байт памяти
Переменная типа <class 'int'> с именем "count" заняла 28 байт памяти
Переменная типа <class 'int'> с именем "num" заняла 28 байт памяти
Переменная типа <class 'list'> с именем "dig_arr" заняла 72 байт памяти
Функция :"dig_count_1" заняла 9012 байт памяти.

Переменная типа <class 'list'> с именем "sequence" заняла 8856 байт памяти
Переменная типа <class 'int'> с именем "find_dig" заняла 28 байт памяти
Переменная типа <class 'int'> с именем "count" заняла 28 байт памяти
Переменная типа <class 'int'> с именем "item" заняла 28 байт памяти
Переменная типа <class 'int'> с именем "val" заняла 24 байт памяти
Переменная типа <class 'int'> с именем "dig" заняла 28 байт памяти
Функция :"dig_count_2" заняла 8992 байт памяти.

Переменная типа <class 'list'> с именем "sequence" заняла 8856 байт памяти
Переменная типа <class 'int'> с именем "find_dig" заняла 28 байт памяти
Переменная типа <class 'str'> с именем "seq_in_str" заняла 2934 байт памяти
Переменная типа <class 'int'> с именем "count" заняла 28 байт памяти
Функция :"dig_count_3" заняла 11846 байт памяти.

Выводы: первая и вторая функции заняли примерно одинаковый объём памяти и меньший чем функция с конкатенацией строк.
Данные результаты приближённо можно считать корректными, за исключение некоторых моментов. 
Если брать в расчёт, что значения от -5 до 255 уже хранятся в памяти, то, например dig и count во второй функции 
действительно занимают 28 байт в случаи маленького массива. В моем случаи функции насчитали 313 четверок, 
следовательно, помимо 255 дефолтных ячеек было выделено памяти еще на 313-255 = 58 интовых значений, что в решении не 
учитывается. 
И, конечно же, то что я испортил функции параметром locals() это ужасно, но пока альтернативного решения не нашёл, 
возможно, посмотрев разбор дз найду ответ. Наверное, в будущем имеет смысл изучить замер памяти с помощью трассировок.
"""
