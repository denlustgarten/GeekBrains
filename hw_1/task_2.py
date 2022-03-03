'''2. Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.'''

if __name__ == "__main__":
    time_in_second = int(input("Введите время в секундах:"))

    hours = time_in_second // 3600
    minutes = (time_in_second % 3600) // 60
    seconds = time_in_second % 60

    print(f'{hours:02}:{minutes:02}:{seconds:02}')
