""" Тесты на класс Square. """

import pytest

from src.square import Square
from src.figure import Figure


def test_square_create_instance(create_square):
    """ Проверяем, что объект создается и является экземпляром классов 'Square', 'Figure'. """

    assert isinstance(create_square, (Square, Figure))


def test_square_has_attr_name(create_square):
    """ Проверяем, что у фигуры есть имя и это имя 'Квадрат'. """

    assert create_square.get_name() == 'Квадрат'


def test_square_has_attr_area(create_square):
    """ Проверяем, что у квадрата есть атрибут 'area' - площадь. """

    assert create_square.area


def test_square_has_attr_perimeter(create_square):
    """ Проверяем, что у квадрата есть атрибут 'perimeter' - периметр. """

    assert create_square.perimeter


def test_square_has_sides(create_square):
    """ Проверяем, что у квадрата есть стороны после создания объекта. """

    assert create_square.sides == 4


def test_square_add_area_square(create_square, create_triangle, create_circle, create_rectangle):
    """ Проверяем, что к площади квадрата можно прибавить площадь другой геометрической фигуры
    ('Square', 'Trinangle', 'Circle', 'Rectangle'). """

    square2 = Square(20)
    assert create_square.add_area(square2) == create_square.area + square2.area
    assert create_square.add_area(create_triangle) == create_square.area + create_triangle.area
    assert create_square.add_area(create_circle) == create_square.area + create_circle.area
    assert create_square.add_area(create_rectangle) == create_square.area + create_rectangle.area


def test_square_add_area_negative(create_square):
    """ Проверяем, что нельзя складывать площади не геометрических фигур. """

    class Animal:
        pass

    with pytest.raises(ValueError):
        create_square.add_area(Animal())
