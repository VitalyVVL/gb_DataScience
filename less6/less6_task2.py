class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calculation_mass(self, weight =25, thickness = 5):
        return self._lenght*self._width*weight*thickness

road_1 = Road(7000, 20)
print(f'Масса асфальта необходимого для укладки: {road_1.calculation_mass(40,5)}')