"""2. Реализовать класс Road (дорога).
определить атрибуты: length (длина), width (ширина);
значения атрибутов должны передаваться при создании экземпляра класса;
атрибуты сделать защищёнными;
определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
проверить работу метода."""


class Road:
    def __init__(self, length: float, width: float):
        self._length = length
        self._width = width

    def mass_calculation(self, mass_per_sq_metr_1sm: float, depth: float):
        return self._length * self._length * mass_per_sq_metr_1sm * depth


lenina_road = Road(length=120, width=3000)
result_mass = lenina_road.mass_calculation(mass_per_sq_metr_1sm=34, depth=23)
print(f'Масса асфальта = {result_mass/1000} т.')
