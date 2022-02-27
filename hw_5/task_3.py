"""3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину
их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников."""
from typing import List, Tuple
from statistics import mean


def read_file(filename: str) -> List[str]:
    employers = []
    with open(filename, 'r', encoding='utf-8') as f:
        employers = f.readlines()
    return employers


if __name__ == '__main__':
    employers = read_file('test_3.txt')
    employers = [val.strip().split() for val in employers]
    print(employers)
    salary_less_20 = [val[0] for val in employers if int(val[1]) < 20000]
    print(f'{salary_less_20 = }')
    average_salary = mean([employers[0] for val in salary_less_20 ])
