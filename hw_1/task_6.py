'''Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке.
Далее запросите численность сотрудников фирмы, и определите прибыль
фирмы в расчёте на одного сотрудника.'''

if __name__ == "__main__":
    revenue = float(input("Введите значение выручки:"))
    costs = float(input("Введите значение издержек:"))

    if revenue > costs:
        print('Прибыль — выручка больше издержек')
        print(f'Рентабельность выручки = {revenue / costs}')
        employs_number = int(input("Введите количество сотрудников:"))
        print(f'Прибыль фирмы в расчёте на одного сотрудника = {(revenue - costs) / employs_number}')
    elif revenue < costs:
        print('Убыток — издержки больше выручки')
    else:
        print('В нуле — издержки равны выручке')
