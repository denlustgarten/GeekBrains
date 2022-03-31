import timeit
from typing import List
from random import randint, seed
import matplotlib.pyplot as plt

SIZE_ARR = 10
MIN_ITEM = 0
MAX_ITEM = 1000
FIND_NUM = 4
find_dig = 4


def sum_(nums):
    sum_val = 0
    for num in nums:
        sum_val += num

    return sum_val


time_arr = []
val_num = (10, 100, 1000, 5000, 10000, 30000, 60000, 100000, 300000, 600000, 1000000)
for val in val_num:
    num1 = [randint(MIN_ITEM, MAX_ITEM) for _ in range(val)]
    time_ = timeit.timeit("sum_(num1)", number=100, globals=globals())
    time_arr.append(time_)

plt.plot(val_num, time_arr, color='red', marker='o', linewidth=2, markersize=6)
plt.show()
