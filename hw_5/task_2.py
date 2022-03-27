"""2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке."""

with open('test_2.txt', 'r') as f:
    content = f.readlines()
    print(f'Всего строк в документе: {len(content)}')
    for ind_str, val in enumerate(content, start=1):
        print(f'{ind_str} строка: {len(val.split())} слов')
