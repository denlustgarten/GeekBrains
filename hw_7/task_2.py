""" Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно."""

from abc import ABC, abstractmethod
import random


class Cloth(ABC):
    @abstractmethod
    def calculate_cloth(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __hash__(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass


class Coat(Cloth):
    def __init__(self, size_, name='coat'):
        self.__size = size_
        self.__name = name

    @property
    def calculate_cloth(self):
        return self.__size / 6.5 + 0.5

    def __str__(self):
        return f'Cloth type: Coat\nname: {self.__name}\nsize: {self.__size}\n'

    def __repr__(self):
        return f'Cloth type: Coat\nname: {self.__name}\nsize: {self.__size}'

    def __hash__(self):
        return hash(self.__name + str(self.__size))

    def __eq__(self, other):
        return self.__name == other.__name and type(self) == type(other)


class Costume(Cloth):
    def __init__(self, growth_, name='costume'):
        self.__growth = growth_
        self.__name = name

    @property
    def calculate_cloth(self):
        return 2 * self.__growth + 0.3

    def __str__(self):
        return f'Cloth type: Costume\nname: {self.__name}\nsize: {self.__growth}\n'

    def __repr__(self):
        return f'Cloth type: Costume\nname: {self.__name}\nsize: {self.__growth}'

    def __hash__(self):
        return hash(self.__name + str(self.__growth))

    def __eq__(self, other):
        return self.__name == other.__name and type(self) == type(other)


class ClothFactory:
    def __init__(self):
        self.__cloth_dict = {}

    def add_cloth(self, cloth_obj: Cloth, num=1):
        if cloth_obj not in self.__cloth_dict.keys():
            self.__cloth_dict[cloth_obj] = num
        else:
            self.__cloth_dict[cloth_obj] += num

    @property
    def total_fabric_consumption(self):
        total_cons = 0
        for key, val in self.__cloth_dict.items():
            total_cons += key.calculate_cloth * val
        return total_cons

    def get_cloth_dict(self):
        return self.__cloth_dict


def gen_cloth():
    if random.random() > 0.5:
        return Costume(growth_=random.randint(130, 200) / 100)
    else:
        return Coat(size_=random.randint(30, 60))


if __name__ == '__main__':

    factory = ClothFactory()
    for i in range(5):
        factory.add_cloth(gen_cloth())

    print(factory.get_cloth_dict())
    print(f'{factory.total_fabric_consumption = }')
