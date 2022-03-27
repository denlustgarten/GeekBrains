"""Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
"""


class Car:
    def __init__(self, speed: float, color: str, name: str, is_police = False):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police = is_police

    def go(self):
        print(f'Машина {self._name} поехала!')

    def stop(self):
        print(f'Машина {self._name} остановилась!')

    def turn(self, direction: str):
        if direction == 'left':
            print(f'Машина {self._name} повернула влево!')
        elif direction == 'right':
            print(f'Машина {self._name} повернула вправо!')
        else:
            print('Машина {self._name} непонятно что сделала!')

    def show_speed(self):
        return self._speed

    def get_name(self):
        return self._name


class TownCar(Car):
    def show_speed(self):
        if self._speed > 60:
            print(f'Превышение скорости!')
        return self._speed


class SportCar(Car):
    def __init__(self, speed: float, color: str, name: str, acceleration_to_100: float,
                 horsepower: int):
        super().__init__(speed, color, name)
        self.__acceleration_to_100 = acceleration_to_100
        self.__horsepower = horsepower

    def get___acceleration_to_100(self):
        return self.__acceleration_to_100

    def get_horsepower(self):
        return self.__horsepower


class WorkCar(Car):
    def __init__(self, speed: float, color: str, name: str):
        super().__init__(speed, color, name)
        self.__sos_gps = False

    def show_speed(self):
        if self._speed > 60:
            print(f'Превышение скорости!')
        return self._speed

    def sos_request(self):
        self.__sos_gps = True
        print('Отправлен сигнал о помощи!')


class PoliceCar(Car):
    def __init__(self, speed: float, color: str, name: str, token_number: str):
        super().__init__(speed, color, name, is_police=True)
        self.__token_number = token_number
        self.__siren = False

    def siren_on(self):
        self.__siren = True
        print('Сирена включена!')

    def siren_off(self):
        self.__siren = True
        print('Сирена выключена!')

    def get_token_number(self):
        return self.__token_number


if __name__ == '__main__':
    ozon_car = WorkCar(speed=70, color='black', name='ozon_car')
    ozon_car.go()
    print(f'Скорость машины {ozon_car.get_name()}: {ozon_car.show_speed()}')
    ozon_car.turn('left')
    ozon_car.stop()
    ozon_car.sos_request()

    print()
    porshe = SportCar(speed=130, color='black', name='porshe', acceleration_to_100=6, horsepower=512)
    porshe.go()
    print(f'Скорость машины {porshe.get_name()}: {porshe.show_speed()}')
    porshe.turn('hz')
    porshe.stop()
    print(f'Разгон машины {porshe.get_name()} до 100 км/ч - {porshe.get___acceleration_to_100()} с.')
    print(f'Машина {porshe.get_name()} имеет мощность двигателя {porshe.get_horsepower()} л.с.')

    print()
    police = PoliceCar(speed=130, color='blue', name='police', token_number='SFT234V2')
    police.go()
    print(f'Скорость машины {police.get_name()}: {police.show_speed()}')
    police.turn('right')
    police.stop()
    print(f'Машины {police.get_name()} имеет номер - {police.get_token_number()}')
    police.siren_on()
    police.siren_off()
