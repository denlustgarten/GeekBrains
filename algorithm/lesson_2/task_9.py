"""9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр."""


def max_sum_digit(max_dig_num: int, max_dig_sum: int) -> (int, int):
    num = int(input("Введите число: "))
    if num:
        current_num = num
        sum_dig = 0
        while num:
            dig = num % 10
            num //= 10
            sum_dig += dig

        if sum_dig > max_dig_sum:
            max_dig_sum = sum_dig
            max_dig_num = current_num

        return max_sum_digit(max_dig_num, max_dig_sum)
    else:
        return max_dig_num, max_dig_sum


print('Программа находит число с наибольшей суммой цифр. Для завершения программы введите 0')
max_digit_num, max_digit_sum = max_sum_digit(0, 0)
print(f'Число с максимальной суммой цифр: {max_digit_num} \nСумма цифр этого числа: {max_digit_sum}')
