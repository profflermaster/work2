from src.figure import Figure


class Rectagnle(Figure):
    """ Класс Прямоугольник. Конструктор принимает длину и ширину прямоугольника. """

    _name = 'Прямоугольник'

    def __init__(self, side1, side2):
        self.__side1 = side1
        self.__side2 = side2

    @property
    def sides(self):
        """ Метод возвращает значение длин сторон прямоугольника. """

        return self.__side1, self.__side2

    @property
    def perimeter(self):
        """ Метод вычисляет периметр прямоугольника по формуле P = 2(a+b), где a - длина, b - ширина """

        return 2 * (self.__side1 + self.__side2)

    @property
    def area(self):
        """ Метод вычисляет площадь прямоугольника по формуле S = a * b, где a - длина, b - ширина """

        return self.__side1 * self.__side2


if __name__ == "__main__":
    rectangle = Rectagnle(3, 4)
    print("Имя фигуры = {}, стороны: {}".format(rectangle.get_name(), rectangle.sides))
    print("Периметр {}а = {}".format(rectangle.get_name(), rectangle.perimeter))
    print("Площадь {}а = {}".format(rectangle.get_name(), rectangle.area))
