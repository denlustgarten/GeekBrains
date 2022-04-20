"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают
за приём оргтехники на склад и передачу в определённое подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру (например, словарь).
6. Продолжить работу над вторым (FIXME 4м?) заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
"""

from random import randint
import traceback
import sys

from task6 import check_method_args, try_except_decorator


class OfficeEquipment:
    def __init__(self, serial_number, wifi_name_='', wifi_pass=None):
        self._serial_number = serial_number
        self.wifi_name_ = wifi_name_
        self._wifi_pass = wifi_pass

    def set_wifi_name(self, wifi_name):
        self.wifi_name = wifi_name

    def set_wifi_pass(self, wifi_pass):
        self._wifi_pass = wifi_pass

    @property
    def wifi_name(self):
        return self.wifi_name_

    @property
    def serial_number(self):
        return self._serial_number

    def __str__(self):
        return f'{self.__class__.__name__}_id: {self.serial_number}'

    def __repr__(self):
        return f'{self.__class__.__name__}_id: {self.serial_number}'

    def __eq__(self, other):
        return self.serial_number == other.serial_number

    def __hash__(self):
        return hash(self.serial_number)


class Printer(OfficeEquipment):
    def __init__(self, serial_number):
        super(Printer, self).__init__(serial_number)
        self.__toner_lvl = 0
        self.list_formates = {'A1': (594, 841),
                              'A2': (420, 594),
                              'A3': (297, 420),
                              'A4': (210, 297),
                              'A5': (148, 210)}

    def update_toner_lvl(self, lvl):
        self.__toner_lvl = lvl

    @property
    def toner_lvl(self):
        return self.__toner_lvl


class Scaner(OfficeEquipment):
    def __init__(self, serial_number):
        super(Scaner, self).__init__(serial_number)
        self.qlvl = 5
        self.__color_mode = True

    def set_scan_quality(self, qlvl):
        if type(qlvl) == int and 0 < qlvl < 11:
            self.qlvl = qlvl

    def set_color_mode(self, mode: bool):
        self.__color_mode = mode

    @property
    def color_mode(self):
        return self.__color_mode


class Copier(OfficeEquipment):
    def __init__(self, serial_number):
        super(Copier, self).__init__(serial_number)
        self.__modes = {
            1: 'strange_mode1',
            2: 'strange_mode2',
            3: 'strange_mode3',
        }
        self.__strange_copier_mode = self.__modes[1]

    @try_except_decorator
    def set_strange_mode(self, mode):
        if mode in self.__modes.keys():
            self.__strange_copier_mode = self.__modes[mode]

    @property
    def current_mode(self):
        return self.__strange_copier_mode


class OfficeEquipmentStorage:
    def __init__(self):
        self.__storage = {'printer': 0,
                          'scaner': 0,
                          'copier': 0}
        self.__authorized_devices = {'printer': [],
                                     'scaner': [],
                                     'copier': []}

    @property
    def storage(self):
        return self.__storage

    @property
    def authorized_devices(self):
        return self.__authorized_devices

    @check_method_args(str, int)
    # @try_except_decorator
    # @check_method_args(str, int)
    def add_equip(self, equip_name: str, num: int) -> bool:
        """
        :param equip_name: str
        :param num: int
        :return: True if success / False if not success
        """
        if equip_name in self.__storage.keys():
            self.__storage[equip_name] += num
            return True
        else:
            print('No such equipment. Use create_new_equip() for adding new position')
            return False

    def remove_equip(self, equip_name: str, num: int) -> bool:
        """
        :param equip_name: str
        :param num: int
        :return: bool
        """
        if equip_name in self.__storage.keys():
            if num <= self.__storage[equip_name]:
                self.__storage[equip_name] -= num
                return True
            else:
                print('There is no such quantity of devices')
                return False
        else:
            print('No such equipment. Use create_new_equip() for adding new position')
            return False

    @try_except_decorator
    def create_new_equip(self, equip: OfficeEquipment):
        """
        :param equip: OfficeEquipment
        :return: None
        """
        if equip not in self.__storage.keys():
            self.__storage[equip] = 0
        else:
            print(f'{equip} already in storage list')

    @try_except_decorator
    def add_autorized_device(self, devices: list[OfficeEquipment]):
        """
        :param devices: list[OfficeEquipment]
        :return None
        """
        devices = devices if isinstance(devices, list) else [devices]
        device_type = type(devices[0]).__name__.lower()
        for device in devices:
            if device_type in self.__authorized_devices.keys():
                self.__authorized_devices[device_type].append(device)
                self.__storage[device_type] += 1
            else:
                print('No such device type. Use create_new_dev_type().')

    # @check_method_args(OfficeEquipment)
    @try_except_decorator
    def create_new_dev_type(self, obj):
        """
        :param obj: OfficeEquipment
        :return: True if success / False if not success
        """
        device_type = obj.__name__.lower()
        if device_type in self.__authorized_devices.keys():
            print(f'{device_type} already in the list')
            return False
        else:
            self.__authorized_devices[device_type] = []
            self.__storage[device_type] = 0
            return True

    @try_except_decorator
    def remove_autorized_device_type(self, obj):
        """
        :param obj: class object
        :return: None
        """
        device_type: OfficeEquipment = obj.__name__.lower()
        try:
            self.__authorized_devices.pop(device_type)
            self.storage.pop(device_type)
        except KeyError:
            print(f'Exception: {traceback.format_exc()}')
        except Exception:
            print(f'Exception: {traceback.format_exc()}')

    @check_method_args(OfficeEquipment)
    # @try_except_decorator
    def remove_autorized_device(self, device):
        device_type = type(device).__name__.lower()
        self.__authorized_devices[device_type].remove(device)
        self.__storage[device_type] -= 1

    @classmethod
    def transfer(cls, stor1, stor2, product_dict: dict):
        """
        :param stor1:
        :param stor2:
        :param product_dict: {'printer': <int>,
                              'scaner': <int>,
                              ...}
        :return:
        """
        for product, num in product_dict.items():
            if stor1.__storage[product] >= num:
                stor2.add_equip(product, num)
                stor1.remove_equip(product, num)
            else:
                print(f'There is no such quantity of devices: {product}')

    @classmethod
    @try_except_decorator
    # @check_method_args(str)
    def gen_id(cls, dev_type=''):
        id_str = [chr(randint(46, 122)) for i in range(16)]
        return dev_type.join(id_str)


class TestDevice(OfficeEquipment):
    def __init__(self, serial_number):
        super(TestDevice, self).__init__(serial_number)


if __name__ == '__main__':
    storage = OfficeEquipmentStorage()
    gen_id = OfficeEquipmentStorage.gen_id
    printers = [Printer(gen_id()) for i in range(randint(1, 5))]
    scaners = [Scaner(gen_id()) for i in range(randint(1, 5))]
    copier = [Copier(gen_id()) for i in range(randint(1, 5))]

    storage.add_autorized_device(printers)
    storage.add_autorized_device(scaners)
    storage.add_autorized_device(copier)

    for device_type, device in storage.authorized_devices.items():
        print(f'{device_type}: {device}')

    print(storage.storage)

    print('Попробуем добавить неизвестный девайс')
    test_device = TestDevice(gen_id())
    storage.add_autorized_device(test_device)
    print('Добавим новый тип')
    storage.create_new_dev_type(TestDevice)
    print('Снова попробуем добавить')
    storage.add_autorized_device(test_device)
    print(f'{storage.storage = }')
    print('Теперь удалим устройство')
    storage.remove_autorized_device(test_device)
    print(f'{storage.storage = }')
    print('И удалим сам тип')
    storage.remove_autorized_device_type(TestDevice)
    print(f'{storage.storage = }')

    print('Попробуем добавить неавторизованных устройств на склад')
    print(storage.storage)
    storage.add_equip('printer', 10)
    print(storage.storage)
    print('Попробуем удалить неавторизованных устройств на склад')
    storage.remove_equip('scaner', 1)
    print(storage.storage)
    print('Попробуем удалить больше неавторизованных устройств на склад')
    storage.remove_equip('scaner', 100)
    print(storage.storage)

    print('Проверим работу контроля параметров')
    storage.add_equip('scaner', 'scaner')
    storage.add_equip()

    print('Теперь проверим передачу устройств между складами')
    storage2 = OfficeEquipmentStorage()
    print('До передачи изделий:')
    print(f'{storage.storage = }\n{storage2.storage = }')

    OfficeEquipmentStorage.transfer(storage, storage2, {'printer':5})
    print('После передачи изделий')
    print(f'{storage.storage = }\n{storage2.storage = }')

    print('Попробуем передать больше, чем есть')
    OfficeEquipmentStorage.transfer(storage2, storage, {'scaner': 5})
    print(f'{storage.storage = }\n{storage2.storage = }')