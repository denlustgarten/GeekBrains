"""Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""


a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a > b:
    if b > c:
        print(f'{b} - среднее число')
    else:
        if a > c:
            print(f'{c} - среднее число')
        else:
            print(f'{a} - среднее число')
else:
    if a > c:
        print(f'{a} - среднее число')
    else:
        if b > c:
            print(f'{c} - среднее число')
        else:
            print(f'{b} - среднее число')
