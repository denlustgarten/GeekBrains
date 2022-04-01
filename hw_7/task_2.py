""" Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно."""

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def calculate_cloth(self):
        pass


class Coat(Clothes):
    def __init__(self, size_):
        self.__size = size_

    def calculate_cloth(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, growth_):
        self.__growth = growth_

    def calculate_cloth(self):
        return 2 * self.__growth + 0.3
