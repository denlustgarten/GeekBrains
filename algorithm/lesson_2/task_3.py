"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и
вывести на экран. Например, если введено число 3486, надо вывести 6843."""


def reverse(old_num: int, new_num: int) -> int:
    if old_num > 0:
        dig = old_num % 10
        new_num *= 10
        new_num += dig
        return reverse(old_num // 10, new_num)
    else:
        return new_num


x = int(input("Введите натуральное число: "))
new_x = reverse(x, 0)
print(f'Первоначальное число: {x} \nПеревернутое число: {new_x}')
