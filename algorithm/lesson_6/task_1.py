import sys


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
    def wrapper():
        sum_memory = 0
        *func_return, var_arr = func()

        for var in var_arr.values():
            sum_memory += my_size(var)

        print(f'Function:"{func.__name__}", size={sum_memory}')
        return func_return
    return wrapper


@memory_expended
def test():
    a = 1
    b = 1000
    c = [0, 5, 6, 3, 5, 4, 5, 6, 3, 5]
    print(sys.getsizeof(c))
    return locals()


test()

# result_memory = 0
# for var in varibles.values():
#     spam = sys.getsizeof(var)
#     print(spam)
#     result_memory += spam
