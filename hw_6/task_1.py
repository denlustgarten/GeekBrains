"""1. Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный метод."""

from colorama import Fore, Style
from time import sleep


class TrafficLight:

    def __init__(self):
        self.__color = ''

    def running(self, green_delay: int, cycles_number: int):
        for i in range(cycles_number):
            self.__color = 'RED'
            print(Fore.RED + self.__color)
            sleep(7)
            self.__color = 'YELLOW'
            print(Fore.YELLOW + self.__color)
            sleep(2)
            self.__color = 'GREEN'
            print(Fore.GREEN + self.__color)
            sleep(green_delay)


traffic_lights = TrafficLight()
traffic_lights.running(green_delay=4, cycles_number=5)
print(Style.RESET_ALL)
