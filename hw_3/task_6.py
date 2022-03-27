"""6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text."""


def upper_first_char(word: str) -> str:
    return word[0].upper() + word[1:]


if __name__ == '__main__':
    print(upper_first_char('hello'))
