"""2. Посчитать четные и нечетные цифры введенного натурального числа. Например,
если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."""


def count_digit(x: int, n_chet: int, n_nechet: int) -> (int, int):  # noqa
    if x > 0:
        dig = x % 10
        if not dig % 2:
            n_chet += 1
        else:
            n_nechet += 1
        return count_digit(x // 10, n_chet, n_nechet)
    else:
        return n_chet, n_nechet


x = int(input("Введите натуральное число: "))
n_ch, n_nech = count_digit(x, 0, 0)
print(f'Кол-во четных цифр: {n_ch} \nКол-во нечетных цифр: {n_nech}')
