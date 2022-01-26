""" Тесты на класс Rectangle. """

import pytest

from src.rectangle import Rectangle
from src.figure import Figure


def test_rectangle_create_instance(create_rectangle):
    """ Проверяем, что объект создается и является экземпляром классов 'Rectangle', 'Figure'. """

    assert isinstance(create_rectangle, (Rectangle, Figure))


def test_rectangle_has_attr_name(create_rectangle):
    """ Проверяем, что у фигуры есть имя и это имя 'Прямоугольник'. """

    assert create_rectangle.get_name() == 'Прямоугольник'


def test_rectangle_has_attr_area(create_rectangle):
    """ Проверяем, что у прямоугольника есть атрибут 'area' - площадь. """

    assert create_rectangle.area


def test_rectangle_has_attr_perimeter(create_rectangle):
    """ Проверяем, что у прямоугольника есть атрибут 'perimeter' - периметр. """

    assert create_rectangle.perimeter


def test_rectangle_has_sides(create_rectangle):
    """ Проверяем, что у прямоугольника есть стороны после создания объекта. """

    assert create_rectangle.sides == (3, 4)


def test_rectangle_add_area_square(create_rectangle, create_square, create_circle, create_triangle):
    """ Проверяем, что к площади прямоугольника можно прибавить площадь другой геометрической фигуры
    ('Trinangle, 'Square', 'Circle', 'Rectangle'). """

    rectangle2 = Rectangle(5, 6)
    assert create_rectangle.add_area(rectangle2) == create_rectangle.area + rectangle2.area
    assert create_rectangle.add_area(create_square) == create_rectangle.area + create_square.area
    assert create_rectangle.add_area(create_circle) == create_rectangle.area + create_circle.area
    assert create_rectangle.add_area(create_triangle) == create_rectangle.area + create_triangle.area


def test_rectangle_add_area_negative(create_rectangle):
    """ Проверяем, что нельзя складывать площади не геометрических фигур. """

    class Car:
        pass

    with pytest.raises(ValueError):
        create_rectangle.add_area(Car())

