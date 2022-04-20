"""1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком."""

from hashlib import sha256


def count_substring(word: str) -> int:
    hash_list = []

    for substring_len in range(1, len(word)):
        for piece in range(len(word) - substring_len + 1):
            sub_word = word[piece:piece + substring_len]
            sub_word_hash = sha256(sub_word.encode('utf-8')).hexdigest()
            if sub_word_hash not in hash_list:
                hash_list.append(sub_word_hash)

    return len(hash_list)


if __name__ == '__main__':
    print(count_substring('sova'))
    print(count_substring('papa'))
    print(count_substring('aaaaa'))
    print(count_substring('hello'))
