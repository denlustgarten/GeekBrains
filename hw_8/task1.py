"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""

import calendar
from datetime import datetime


class Data:
    def __init__(self, data_inp: str):
        # super().__init__()12-
        self.data_str = data_inp

    @property
    def data(self):
        return self.data_str

    @classmethod
    def conv_data(cls, data_obj):
        try:
            # day, month, year = cls.data(cls).split(sep='-')
            day, month, year = data_obj.data.split(sep='-')
            if not int(day) and int(month) and int(year):
                raise ValueError()
            return int(day), int(month), int(year)
        except ValueError as val_er:
            print(val_er)
            return None
        except Exception as ex:
            print(ex)
            return None

    @staticmethod
    def validate(day=None, month=None, year=None) -> list[bool, bool, bool]:
        check_y = year <= datetime.now().year
        check_m = 0 < month < 13
        check_d = False
        for week in calendar.monthcalendar(year, month):
            if day in week:
                check_d = True
                break

        return check_d, check_m, check_y


if __name__ == "__main__":
    data_input = input("Введите дату в формате «день-месяц-год»\n")
    data = Data(data_input)
    res = data.conv_data(data)
    if res is not None:
        day, month, year = res
        val_res = Data.validate(day, month, year)
        print(f'Результаты проверки на существование даты день-месяц-год:\n{val_res}')
    else:
        print('Ошибка ввода данных')
