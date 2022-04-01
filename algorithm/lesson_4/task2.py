import math
import timeit
import cProfile
import matplotlib.pyplot as plt

n = 1000
sieve = [i for i in range(n)]  # только для этой задачи, а не для выполнения ПЗ
HOLE = 0
sieve[1] = HOLE


def sieve(n):
    sieve_ = [i for i in range(n)]
    for i in range(2, n):
        if sieve_[i] != HOLE:
            j = i + i
            while j < n:
                sieve_[j] = HOLE
                j += i
    return [item for item in sieve_ if item != HOLE]


def prime(n):
    if n == 1:
        result_arr = [1, ]
    else:
        result_arr = [val for val in [1, 2]]
        for i in range(3, n):
            is_simple = 1
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    is_simple = 0
            if is_simple:
                result_arr.append(i)
    return result_arr


print(sieve(100))
print(prime(100))

time_sieve = []
time_prime = []
numb = [x for x in range(1, 1000, 100)]

for n in numb:
    time_ = timeit.timeit("sieve(n)", number=1000, globals=globals())
    print(f'sieve(): arr length: {n:>4}, time: {time_}')
    time_sieve.append(time_)
print()

for n in numb:
    time_ = timeit.timeit("prime(n)", number=1000, globals=globals())
    print(f'prime(): arr length: {n:>4}, time: {time_}')
    time_prime.append(time_)
print()

plt.plot(numb, time_sieve, color='green', marker='o', linewidth=2, markersize=6)
plt.plot(numb, time_prime, color='blue', marker='o', linewidth=2, markersize=6)
plt.plot(numb, [x * math.log2(x) / 4300 for x in numb], color='red', marker='o', linewidth=2, markersize=6)
plt.legend(['sieve', 'prime', 'n * log2(n)'])
plt.show()

cProfile.run('sieve(100000)')
cProfile.run('prime(100000)')

"""
sieve(): arr length:    1, time: 0.00015120001626200974
sieve(): arr length:  101, time: 0.0037619000067934394
sieve(): arr length:  201, time: 0.0076538999855984
sieve(): arr length:  301, time: 0.011860700004035607
sieve(): arr length:  401, time: 0.01649300000281073
sieve(): arr length:  501, time: 0.021650100010447204
sieve(): arr length:  601, time: 0.026079600007506087
sieve(): arr length:  701, time: 0.03146729999571107
sieve(): arr length:  801, time: 0.03590399998938665
sieve(): arr length:  901, time: 0.04157840000698343

prime(): arr length:    1, time: 2.4100008886307478e-05
prime(): arr length:  101, time: 0.011476300016511232
prime(): arr length:  201, time: 0.02659459999995306
prime(): arr length:  301, time: 0.044050500000594184
prime(): arr length:  401, time: 0.06428109999978915
prime(): arr length:  501, time: 0.08518150000600144
prime(): arr length:  601, time: 0.11077620001742616
prime(): arr length:  701, time: 0.13220540000475012
prime(): arr length:  801, time: 0.16259169997647405
prime(): arr length:  901, time: 0.19159090000903234


ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.001    0.001    0.088    0.088 <string>:1(<module>)
    1    0.072    0.072    0.087    0.087 task2.py:14(sieve)
    1    0.007    0.007    0.007    0.007 task2.py:15(<listcomp>)
    1    0.008    0.008    0.008    0.008 task2.py:22(<listcomp>)
    1    0.000    0.000    0.088    0.088 {built-in method builtins.exec}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


     109593 function calls in 1.691 seconds

Ordered by: standard name

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.000    0.000    1.691    1.691 <string>:1(<module>)
    1    1.663    1.663    1.691    1.691 task2.py:25(prime)
    1    0.000    0.000    0.000    0.000 task2.py:30(<listcomp>)
    1    0.000    0.000    1.691    1.691 {built-in method builtins.exec}
99997    0.027    0.000    0.027    0.000 {built-in method math.sqrt}
 9591    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
    1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Отчет cProfile показал, что функция sieve довольно хорошо оптимизирована и не имеет тонких мест.
В принципе функция prime тоже не имеет заметных проблем, но ее производительность существенно ниже 

Вывод: сложность алгоритма "решето Эратосфена" равна O(n), сложность алгоритма в функции 
prime можно отнести как к O(n), так и к О(n log2(n)). На графике я изобразил график y(n) =K * n * log(n).
К = 4300 подобран руками при number=1000 
Алгоритм Эратосфена является более оптимальным, чем алгоритм prime.
"""
