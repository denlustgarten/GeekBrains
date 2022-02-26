"""2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как
 именованные аргументы. Осуществить вывод данных о пользователе одной строкой."""


def user_info(name_: str, surname_: str, birth_day_: int,
              city_: str, email_: str, t_number_: str) -> str:
    return f' Имя: {name_}\n Фамилия: {surname_}\n Год рождения: {birth_day_}\n ' \
           f'Город проживания: {city_}\n Email: {email_}\n Номер телефона: {t_number_}'


if __name__ == '__main__':
    try:
        name = input("Введите имя: ")
        surname = input("Введите фамилия: ")
        birth_day = int(input("Введите год рождения: "))
        city = input("Введите город проживания: ")
        email = input("Введите email: ")
        t_number = input("Введите номер телефона: ")

        print(user_info(name_=name, surname_=surname, birth_day_=birth_day,
                        city_=city, email_=email, t_number_=t_number))
    except ValueError as e:
        print('Input error: incorrect arguments ')
