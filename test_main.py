import pytest
from main import calculate
import io


def test_calculate_square(capsys, monkeypatch):
    input_data = "Square TopRight 1 1 Side 1"
    monkeypatch.setattr('sys.stdin', io.StringIO(input_data))
    calculate()
    captured = capsys.readouterr()
    expected_output = f"Please enter your data here:Square Perimeter 4 Area 1\n"
    assert captured.out == expected_output


def test_calculate_wrong_square(capsys, monkeypatch):
    input_data = "Square TopRight 1 1 Side 0"
    monkeypatch.setattr('sys.stdin', io.StringIO(input_data))
    with pytest.raises(ValueError):
        calculate()


def test_calculate_rectangle(capsys, monkeypatch):
    input_data = "Rectangle TopRight 1 1 BottomLeft 2 2"
    monkeypatch.setattr('sys.stdin', io.StringIO(input_data))
    calculate()
    captured = capsys.readouterr()
    expected_output = f"Please enter your data here:Rectangle Perimeter 4 Area 1\n"
    assert captured.out == expected_output


def test_calculate_circle(capsys, monkeypatch):
    input_data = "Circle Center 1 1 Radius 2"
    monkeypatch.setattr('sys.stdin', io.StringIO(input_data))
    calculate()
    captured = capsys.readouterr()
    expected_output = f"Please enter your data here:Circle Perimeter 12.57 Area 12.57\n"
    assert captured.out == expected_output


def test_unknown_shape(capsys, monkeypatch):
    input_data = "Triangle Point 1 5 5 Point2 8 8 Point 3 10 2"
    monkeypatch.setattr('sys.stdin', io.StringIO(input_data))
    with pytest.raises(ValueError) as excinfo:
        calculate()
        assert 'Unknown shape type Triangle' in str(excinfo.value)




