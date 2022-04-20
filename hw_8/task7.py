"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real_part: float, imag_part: float = 0.0):
        self.real = real_part
        self.imag = imag_part

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + other.real * self.imag)

    def __truediv__(self, other):
        # тип complex округляет до 17 знаков до запятой и 16 после, делаем аналогично,
        # чтобы можно было сравнить результаты
        return Complex(
            round((self.real * other.real + self.imag * other.imag) / (other.real ** 2 + other.imag ** 2), 17),
            round((other.real * self.imag - self.real * other.imag) / (other.real ** 2 + other.imag ** 2), 16))

    def __str__(self):
        return f'{self.real} + {self.imag}i' if self.imag > 0 else f'{self.real} - {abs(self.imag)}i'

    def __repr__(self):
        return f'{self.real} + {self.imag}i' if self.imag > 0 else f'{self.real} - {abs(self.imag)}i'


if __name__ == "__main__":
    x1 = Complex(1.3423, 42.5425)
    y1 = Complex(324.234, 234.23542)
    print(x1)
    print(y1)
    print(f'{x1 + y1 = }')
    print(f'{x1 - y1 = }')
    print(f'{x1 * y1 = }')
    print(f'{x1 / y1 = }')

    x2 = complex(x1.real, x1.imag)
    y2 = complex(y1.real, y1.imag)
    print(x2)

    print('Сравним результаты со втроенным типом complex:')
    print(f'{x1 == x2 = },\n{y1 == y2 = }')
    print(f'{x1 + y1 == x2 + y2 = }')
    print(f'{x1 - y1 == x2 - y2  = }')
    print(f'{x1 * y1 == x2 * y2  = }')
    print(f'{x1 / y1 == x2 / y2  = }')
