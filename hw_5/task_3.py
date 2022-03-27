"""3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину
их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч,
вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников."""
from typing import List, Dict
from statistics import mean


def read_file(filename: str) -> List[str]:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            employers = f.readlines()
        return employers
    except IOError as e:
        print(e)
        return []


def list_to_dict(employers: List[str]) -> Dict[str, float]:
    emp_dict = {person[0]: float(person[1]) for person in [val.strip().split() for val in employers]}
    return emp_dict


if __name__ == '__main__':
    emp_to_list = read_file('test_3.txt')
    emp_to_dict = list_to_dict(emp_to_list)
    salary_less_20 = [name for name, sal in emp_to_dict.items() if sal < 20000]
    print(f'Сотрудники c ЗП меньше 20к: {", ".join(salary_less_20)}')

    if emp_to_dict:
        average_salary = mean(sal for sal in emp_to_dict.values())
        print(f'Средняя зарплата = {average_salary:.2f}')
    else:
        print('Файл либо не существует либо он пуст!')

