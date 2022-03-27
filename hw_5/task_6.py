"""6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный
предмет и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить
и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран."""

from typing import List, Dict


def read_file(filename: str) -> List[str]:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.readlines()
            # print(content)
        return content
    except IOError as e:
        print(e)
        return []


def convert_to_dict(content: List[str]) -> Dict[str, int]:
    temp = [val.strip().split(':') for val in content]
    lesson_hours_dict = {val[0]: val[1] for val in temp}
    for key, val in lesson_hours_dict.items():
        format_val = ''
        for char in val:
            if char.isdigit():
                format_val += char
            else:
                format_val += ' '
        lesson_hours_dict[key] = sum([int(x) for x in format_val.split()])
    return lesson_hours_dict


if __name__ == '__main__':
    lesson_hours = read_file('test_6.txt')
    result_dict = convert_to_dict(lesson_hours)
    for key, value in result_dict.items():
        print(f'{key}: {value}')
