"""3. Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров."""


class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {'wage': wage,
                        'bonus': bonus,
                        }


class Position(Worker):
    def get_full_name(self):
        return f'{self._surname} {self._name}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


worker_1 = Position('Denis', 'Lustgarten', 'verification engineer', 70000, 15000)
print(f'Полное имя: {worker_1.get_full_name()}')
print(f'Доход: {worker_1.get_total_income()} руб.')

worker_2 = Position('Ivan', 'Smirnov', 'programmer', 80000, 10000)
print(f'Полное имя: {worker_2.get_full_name()}')
print(f'Доход: {worker_2.get_total_income()} руб.')