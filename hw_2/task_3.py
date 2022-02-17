"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict."""

month_dict = {
    '12, 1, 2': 'Зима',
    '3, 4, 5': 'Весна',
    '6, 7, 8': 'Лето',
    '9, 10, 11': 'Осень',
}

if __name__ == '__main__':
    month_number = input()
    for keys in month_dict.keys():
        print(keys.split(', '))
        if month_number in keys.split(', '):
            print(month_dict[keys])
            break
        # els    #     print('This month does not exist.')
        #     break

