"""7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки, но каждое
слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func()."""


def upper_first_char(words: str) -> str:
    upper_words_arr = []
    for word in words.split():
        upper_words_arr.append(word[0].upper() + word[1:])
    return ' '.join(upper_words_arr)


if __name__ == '__main__':
    print(upper_first_char('hello my name is denis'))
