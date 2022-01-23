from src.circle import Circle
from src.rectangle import Rectagnle
from src.square import Square
from src.triangle import Triangle

if __name__ == "__main__":
    """ Создаём фигуры. Сумма площадей созданных фигур. """

    triangle = Triangle(13, 14, 15)  # Создаем треугольник
    print("Имя фигуры = {}, стороны: {}".format(triangle.get_name(), triangle.sides))
    print("Периметр {}а = {}".format(triangle.get_name(), triangle.perimeter))
    print("Площадь {}а = {}\n".format(triangle.get_name(), triangle.area))

    square = Square(10)  # Создаем квадрат
    print("Имя фигуры = {}, сторона: {}".format(square.get_name(), square.sides))
    print("Периметр {}а = {}".format(square.get_name(), square.perimeter))
    print("Площадь {}а = {}\n".format(square.get_name(), square.area))

    circle = Circle(10)  # Создаем круг
    print("Имя фигуры = {}, радиус: {}".format(circle.get_name(), circle.radius))
    print("Периметр {}а = {}".format(circle.get_name(), circle.perimeter))
    print("Площадь {}а = {}\n".format(circle.get_name(), circle.area))

    rectangle = Rectagnle(4, 5)  # Создаем прямоугольник
    print("Имя фигуры = {}, {}".format(rectangle.get_name(), rectangle.sides))
    print("Периметр {}а = {}".format(rectangle.get_name(), rectangle.perimeter))
    print("Площадь {}а = {}\n".format(rectangle.get_name(), rectangle.area))

    # Проверяем сумму площадей cозданных фигур
    print(f"Сумма площадей {triangle.get_name()} + {square.get_name()} = "
          f"{triangle.add_area(square)}")
    print(f"Сумма площадей {triangle.get_name()} + {circle.get_name()} = "
          f"{triangle.add_area(circle)}")
    print(f"Сумма площадей {triangle.get_name()} + {rectangle.get_name()} = "
          f"{triangle.add_area(rectangle)}")
    print(f"Сумма площадей {square.get_name()} + {rectangle.get_name()} = "
          f"{square.add_area(rectangle)}")
