import pytest
from figures import Square, Rectangle, Circle


def test_calculate_wrong_square():
    with pytest.raises(ValueError):
        Square(1, 1, 0)


def test_calculate_wrong_rectangle():
    with pytest.raises(ValueError):
        Rectangle(1, 1, 1, 2)


def test_calculate_wrong_circle():
    with pytest.raises(ValueError):
        Circle(1, 1, 0)
