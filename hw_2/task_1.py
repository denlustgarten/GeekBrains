"""1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе."""

if __name__ == '__main__':
    my_list = [1, 2, 'hello', 3.14, False, [1, 2, 3], 'world']
    for val in my_list:
        print(type(val))
