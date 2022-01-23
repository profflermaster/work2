from src.figure import Figure


class Square(Figure):
    """ Класс Квадрат. Конструктор принимает длину стороны квадрата. """

    _name = 'Квадрат'

    def __init__(self, side):
        self.__side = side

    @property
    def sides(self):
        """ Метод возвращает значение длины стороны квадрата. """

        return self.__side

    @property
    def perimeter(self):
        """ Метод вычисляет периметр квадрата по формуле P = 4*a, где a - длина стороны квадрата. """

        return self.__side * 4

    @property
    def area(self):
        """ Метод вычисляет площадь квадрата по формуле S = a * a. """

        return self.__side ** 2


if __name__ == "__main__":
    square = Square(10)
    print("Имя фигуры: {}, сторона: {}".format(square.get_name(), square.sides))
    print("Периметр {}а = {}".format(square.get_name(), square.perimeter))
    print("Площадь {}а = {}".format(square.get_name(), square.area))
