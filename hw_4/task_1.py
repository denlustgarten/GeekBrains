"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для
конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv


try:
    production_in_hours = float(argv[1])
    rate_per_hour = float(argv[2])
    bonus = float(argv[3])
    wage = production_in_hours * rate_per_hour + bonus
    print(f'Заработная плата = {wage}')
except IndexError as e:
    print(f'Ошибка! Некорректное кол-во параметров при запуске скрипта: \n{e}')
except ValueError as e:
    print(f'Ошибка! Некорректное значение параметра при запуске скрипта: \n{e}')
