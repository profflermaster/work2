import pytest

from src.figure import Figure
from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


@pytest.fixture
def create_circle():
    circle = Circle(7)
    yield circle
    del circle


@pytest.fixture
def create_figure():
    return Figure()


@pytest.fixture
def create_rectangle():
    rectangle = Rectangle(3, 4)
    yield rectangle
    del rectangle


@pytest.fixture
def create_square():
    square = Square(4)
    yield square
    del square


@pytest.fixture
def create_triangle():
    triangle = Triangle(13, 14, 15)
    yield triangle
    del triangle