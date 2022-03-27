"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат
вычисления произведения всех элементов списка."""


from functools import reduce

sequence = [num for num in range(100, 1001) if num % 2 == 0]
result = reduce(lambda x, y: x * y, sequence)
print(result)
