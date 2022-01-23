import math

from src.figure import Figure


class Triangle(Figure):
    """ Класс Треугольник. Конструктор принимает длины 3х сторон треугольника. Если треугольник создать
    нельзя, возвращаетя 'None'. """

    _name = 'Треугольник'

    def __init__(self, side1, side2, side3):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    @staticmethod
    def __new__(cls, *args):
        """ Метод проверяет является ли создаваемая фигура треугольником по формуле: сумма длин 2х
        строн должна быть больше третьей. Если условие не выполняется, объект не создается,
        возвращается 'None'. """

        # Проверяем условие существования тругольника
        if not ((args[0] + args[1] > args[2]) and (args[0] + args[2] > args[1])
                and (args[1] + args[2] > args[0])):
            print("Создаваемая фигура не являтся треугольником")
            return None
        # Возврящаем объект
        return super(Triangle, cls).__new__(cls)

    @property
    def sides(self):
        """ Метод возвращает значение сторон треугольника. """

        return self.__side1, self.__side2, self.__side3

    @property
    def area(self):
        """ Метод вычисляет площадь треугольника по формуле Герона.
        Сначала необходимо подсчитать разность полупериметра и каждой его стороны. Потом найти
        произведение полученных чисел, умножить результат на полупериметр и найти корень из
        полученного числа.
        S = √ p * (p − a) * (p − b) * (p − c), где a, b, c — стороны, p — полупериметр,
        который можно найти по формуле: p = (a + b + c) / 2. """

        halfperimeter = self.perimeter / 2
        return math.sqrt(
            halfperimeter * (halfperimeter - self.__side1) * (halfperimeter - self.__side2) *
            (halfperimeter - self.__side3))

    @property
    def perimeter(self):
        """ Метод вычисляет периметр треугольника по формуле S = a + b + c. """

        return self.__side1 + self.__side2 + self.__side3


if __name__ == "__main__":
    triangle = Triangle(13, 14, 15)
    print("Имя фигуры: {}, стороны: {}".format(triangle.get_name(), triangle.sides))
    print("Периметр {}а = {}".format(triangle.get_name(), triangle.perimeter))
    print("Площадь {}а = {}".format(triangle.get_name(), triangle.area))
