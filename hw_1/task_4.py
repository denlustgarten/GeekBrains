'''4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.'''

if __name__ == "__main__":
    n = ""
    while not n.isdigit():
        n = input("Введите число:")

    maximum = -1
    n = int(n)

    while n > 0:
        digit = n % 10
        if digit > maximum:
            maximum = digit
        n = n // 10
    print(f'max_digit = {maximum}')
