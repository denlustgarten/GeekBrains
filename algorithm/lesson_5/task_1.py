"""Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
(т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год
для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и
ниже среднего."""

from collections import defaultdict

QUARTERS = 4

company_profit = defaultdict(list)

N = int(input("Введите кол-во компаний: "))
for i in range(N):
    company_name = input(f'Введите название {i + 1}-й компании: ')
    for j in range(QUARTERS):
        company_profit[company_name].append(int(input(f'Введите прибыль компании за {j + 1}-й квартал: ')))
    print()

# company_profit = {'first': [2, 3, 4, 5], 'second': [3, 1, 1, 1], 'third': [3, 1, 1, 23], 'fourth': [45, 45, 2, 1]}

average_profit = (sum(sum(val) for val in company_profit.values())) / len(company_profit)
print(f'Средняя прибыль: {average_profit}')

profitable_unprofitable = {'Прибыльные компании': [], 'Убыточные компании': [], 'Вышли в 0': []}

for name, val in company_profit.items():
    profit = sum(val)
    if profit > average_profit:
        profitable_unprofitable['Прибыльные компании'].append(name + f'({profit})')
    elif profit < average_profit:
        profitable_unprofitable['Убыточные компании'].append(name + f'({profit})')
    else:
        profitable_unprofitable['Вышли в 0'].append(name + f'({profit})')

for key, val in profitable_unprofitable.items():
    print(f'{key}: {", ".join(val)}')
