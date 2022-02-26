"""7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое
слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func()."""


def upper_first_char(words: str) -> str:
    new_str = ''
    for word in words.split():
            new_str += word[0].upper() + word[1:]
    return new_str


if __name__ == '__main__':
    print(upper_first_char('hello my name is denis'))
