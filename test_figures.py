import pytest

from figures import Square, Rectangle, Circle


def test_calculate_right_perimetr_square():
    input_data = "Square TopRight 1 1 Side 1"
    test_square = Square(input_data.split())
    assert test_square.calculate_perimeter() == 4


def test_calculate_wrong_square():
    with pytest.raises(ValueError, match="The side of square should be > 0"):
        input_l = "Square TopRight 1 1 Side 0"
        Square(input_l.split())


def test_calculate_wrong_rectangle():
    with pytest.raises(ValueError):
        input_l = "Rectangle TopRight 1 1 BottomLeft 1 2"
        Rectangle(input_l.split())


def test_calculate_wrong_circle():
    with pytest.raises(ValueError):
        input_l = "Circle Center 1 1 Radius 0"
        Circle(input_l.split())
