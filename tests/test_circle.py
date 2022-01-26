"""Тесты на класс Circle."""
import pytest

from src.circle import Circle
from src.figure import Figure


def test_circle_create_instance(create_circle):
    """ Проверяем, что объект создается и является экземпляром классов 'Circle', 'Figure'. """

    assert isinstance(create_circle, (Circle, Figure))


def test_circle_has_attr_name(create_circle):
    """ Проверяем, что у фигуры есть имя и это имя 'Круг'. """

    assert create_circle.get_name() == 'Круг'


def test_circle_has_attr_area(create_circle):
    """ Проверяем, что у круга есть атрибут 'area' - площадь. """

    assert create_circle.area


def test_circle_has_attr_perimeter(create_circle):
    """ Проверяем, что у круга есть атрибут 'perimeter' - периметр. """

    assert create_circle.perimeter


def test_circle_has_sides(create_circle):
    """ Проверяем, что у круга есть радиус после создания объекта. """

    assert create_circle.radius == 7


def test_circle_add_area_negative(create_circle):
    """ Проверяем, что нельзя складывать площади не геометрических фигур. """

    class Car:
        pass

    with pytest.raises(ValueError):
        create_circle.add_area(Car())
