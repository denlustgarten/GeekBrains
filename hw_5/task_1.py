"""1. Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка."""

with open('test.txt', 'w') as f:
    content = True
    while content:
        content = input("Введите текст для записи в файл: ")
        f.write(content + '\n')