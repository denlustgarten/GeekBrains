"""
3. Создайте собственный класс-исключение, который должен проверять
содержимое списка на наличие только чисел. Проверить работу исключения на реальном примере.
Запрашивать у пользователя данные и заполнять список необходимо только числами.
Класс-исключение должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
пока пользователь сам не остановит работу скрипта, введя, например, команду «stop».
При этом скрипт завершается, сформированный список с числами выводится на экран.
Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
Вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и
отобразить соответствующее сообщение.
При этом работа скрипта не должна завершаться.
"""


class MyListException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


def my_append_dec(append_func):
    def magic(*args):
        conv_args = []
        for arg in args:
            for obj in arg:
                if not obj.isnumeric():
                    raise MyListException('Appending obj must be integer or float')
                conv_args.append(int(obj))
        return append_func(*conv_args)

    return magic


class MyList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.append = my_append_dec(self.append)


if __name__ == "__main__":
    lst = MyList([])
    while True:
        try:
            data = input("Введите число\n")
            if data == 'q':
                break
            for sym in data.strip().split():
                lst.append(sym)
        except MyListException as my_ex:
            print(my_ex)
            break
        print(lst)
    print(lst)
