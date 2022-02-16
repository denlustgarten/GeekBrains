''' 1. Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и
строки и сохраните в переменные, затем выведите на экран.'''

if __name__ == "__main__":
    a = 15
    b = 'hello world'
    c = 14.304
    d = True

    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')
    print(f'd = {d}')

    print(f'type_a = {type(a)}')
    print(f'type_b = {type(b)}')
    print(f'type_c = {type(c)}')
    print(f'type_d = {type(d)}')

    name, second_name, surname = input("Введите свое ФИО телефона:").split()
    print(f'{name} {second_name} {surname}')

    number = int(input("Введите ваш возраст:"))
    print(number)
