"""
5. Реализовать класс Stationery (канцелярская принадлежность).

    определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
    создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
    в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
    создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""

import os

"""установка модуля для рисования: pip install image2ascii"""


class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')  # логичнее просто pass, чтобы был интерфейсный класс


class Pen(Stationery):
    def __init__(self):
        super().__init__(title='pen')

    def draw(self):
        # say('Pen text', colors=['green', 'blue'], size=(100, 5), font='slick')
        # os.system("image2ascii pen.png --color --quality 9")
        print("Рисуем ручку!")
        os.system("image2ascii pen.png --width 40 --quality 5  --color --color-balance 12")


class Pencil(Stationery):
    def __init__(self):
        super().__init__(title='pencil')

    def draw(self):
        print("Рисуем карандаш!")
        os.system("image2ascii pencil.png --width 40 --quality 5  --color --color-balance 12")


class Handle(Stationery):
    def __init__(self):
        super().__init__(title='handle')

    def draw(self):
        print("Рисуем маркер!")
        os.system("image2ascii handle.png --width 40 --quality 5  --negative --color ")


if __name__ == '__main__':
    pen = Pen()
    pencil = Pencil()
    handle = Handle()

    pen.draw()
    print('\n\n\n')
    pencil.draw()
    print('\n\n\n')
    handle.draw()
