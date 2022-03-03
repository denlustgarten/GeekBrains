'''3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.'''

if __name__ == "__main__":
    n = ""
    while not n.isdigit():
        n = input("Введите число:")

    result = 0
    for i in range(1, int(n) + 1):
        result += int(n * i)

    print(f'result = {result}')


