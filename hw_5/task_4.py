"""4.
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

from typing import List, Dict

eng_to_rus = {
    'Zero': 'Ноль',
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять',
    'Six': 'Шесть',
    'Seven': 'Семь',
    'Eight': 'Восемь',
    'Nine': 'Девять',
}


def read_file(filename: str) -> List[str]:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.readlines()
        return content
    except IOError as e:
        print(e)
        return []


def list_to_dict(content: List[str]) -> Dict[str, float]:
    content_to_dict = {name_digit[0]: int(name_digit[1]) for name_digit in [val.strip().split(' — ') for val in content]}
    return content_to_dict


def translate_eng_to_rus(digit_dict: Dict[str, float]) -> Dict[str, int]:
    translate_content = {eng_to_rus.get(name): val for name, val in digit_dict.items() if name in eng_to_rus}
    return translate_content


def write_file(filename: str, digits: Dict[str, int]) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        for name, dig in digits.items():
            f.write(f'{name} — {dig}\n')


if __name__ == '__main__':
    file_content = read_file('test_4.txt')
    digit_dict = list_to_dict(file_content)
    new_dict = translate_eng_to_rus(digit_dict)
    print(new_dict)
    write_file('test_4_2.txt', new_dict)
