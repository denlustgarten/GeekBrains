"""7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков)."""

from typing import List, Dict
from copy import deepcopy
from statistics import mean

import json


def read_file(filename: str) -> Dict[str, List]:
    try:
        firms_info = {}
        with open(filename, 'r', encoding='utf-8') as f:
            while True:
                content = f.readline().split()
                print(content)
                if content:
                    firms_info[content[0]] = content[1:]
                else:
                    break
        return firms_info
    except IOError as e:
        print(e)
        return {}


def profit_calculation(firms_info: Dict[str, List]) -> Dict[str, List]:
    for name, val in firms_info.items():
        firms_info[name].append(int(val[1]) - int(val[2]))
    return firms_info


def income_statement(firms_info_with_profit: Dict[str, List]):
    new_dict = {}
    for name, val in firms_info_with_profit.items():
        new_dict[name] = val[-1]
    average_profit = {"average_profit": mean([val[-1] for val in firms_info_with_profit.values() if val[-1] > 0])}
    return [new_dict, average_profit]


def dump_to_file(result_cont: List, filename):
    with open(filename, 'w', encoding='utf-8') as file_obj:
        json.dump(result_cont, file_obj)


if __name__ == '__main__':
    f_info = read_file('test_7.txt')
    f_info_with_prof = profit_calculation(deepcopy(f_info))
    result_content = income_statement(deepcopy(f_info_with_prof))
    dump_to_file(result_content, 'test_7_out.test')
