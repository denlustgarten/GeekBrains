"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""


class MyException(ZeroDivisionError):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


try:
    num1, num2 = [float(sym) for sym in input('Enter 2 numbers\n').strip().split()]
    if num2 == 0.0:
        raise MyException('Whoops. Division by zero. ¯\\_(ツ)_/¯')
    else:
        print(num1 / num2)
except MyException as my_ex:
    print(my_ex)
except Exception as ex:
    print(ex)
