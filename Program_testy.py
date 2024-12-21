import pytest
from PIL import Image
from Program import Point, Line, LoadParameters, OutOfRangeError, DrawLine


def test_point_integer():
    point = Point(1, 2)
    assert point.x == 1
    assert point.y == 2


def test_point_not_integer():
    with pytest.raises(TypeError):
        Point('a', 3.5)


def test_line_points():
    point1 = Point(1, 1)
    point2 = Point(5, 5)
    line = Line(point1, point2)
    assert line.start == point1
    assert line.end == point2


def test_line_points_not_Point():
    with pytest.raises(TypeError):
        Line(1, "a")


def test_line_bresenham():
    point1 = Point(1, 1)
    point2 = Point(5, 3)
    line = Line(point1, point2)
    line_points = line.LinePoints()
    assert line_points == [Point(1, 1), Point(2, 1), Point(3, 2),
                           Point(4, 2), Point(5, 3)]


def test_line_bresenham_horizontal():
    point1 = Point(1, 1)
    point2 = Point(5, 1)
    line = Line(point1, point2)
    line_points = line.LinePoints()
    assert line_points == [Point(1, 1), Point(2, 1), Point(3, 1),
                           Point(4, 1), Point(5, 1)]


def test_line_bresenham_vertical():
    point1 = Point(1, 1)
    point2 = Point(1, 5)
    line = Line(point1, point2)
    line_points = line.LinePoints()
    assert line_points == [Point(1, 1), Point(1, 2), Point(1, 3),
                           Point(1, 4), Point(1, 5)]


def test_line_bresenham_shallow():
    point1 = Point(1, 1)
    point2 = Point(7, 3)
    line = Line(point1, point2)
    line_points = line.LinePoints()
    assert line_points == [Point(1, 1), Point(2, 1), Point(3, 2), Point(4, 2),
                           Point(5, 2), Point(6, 3), Point(7, 3)]


def test_line_bresenham_reverse():
    point1 = Point(5, 5)
    point2 = Point(1, 1)
    line = Line(point1, point2)
    line_points = line.LinePoints()
    assert line_points == [Point(5, 5), Point(4, 4), Point(3, 3),
                           Point(2, 2), Point(1, 1)]


def test_line_bresenham_vertical_reverse():
    point1 = Point(1, 5)
    point2 = Point(1, 1)
    line = Line(point1, point2)
    line_points = line.LinePoints()
    assert line_points == [Point(1, 5), Point(1, 4), Point(1, 3),
                           Point(1, 2), Point(1, 1)]


def test_line_bresenham_single_point():
    point1 = Point(1, 1)
    point2 = Point(1, 1)
    line = Line(point1, point2)
    line_points = line.LinePoints()
    assert line_points == [Point(1, 1)]


def test_line_bresenham_horizontal_negative():
    point1 = Point(5, 1)
    point2 = Point(1, 1)
    line = Line(point1, point2)
    line_points = line.LinePoints()
    assert line_points == [Point(5, 1), Point(4, 1), Point(3, 1),
                           Point(2, 1), Point(1, 1)]


def test_load_parameters():
    result = LoadParameters("Pliki testowe/poprawne_dane.txt")
    assert result[1] == 60
    assert result[0].x == 30
    assert result[0].y == 50


def test_load_parameters_filenotfound():
    with pytest.raises(FileNotFoundError):
        LoadParameters("nieistnieje.txt")


def test_load_parameters_strings():
    with pytest.raises(ValueError):
        LoadParameters("Pliki testowe/string_dane.txt")


def test_load_parameters_out_of_range():
    with pytest.raises(OutOfRangeError):
        LoadParameters("Pliki testowe/poza_dane.txt")


def test_load_parameters_not_enough_data():
    with pytest.raises(ValueError):
        LoadParameters("Pliki testowe/brak_danych.txt")


def test_load_image_wrong_extension():
    with pytest.raises(ValueError):
        LoadParameters("Pliki testowe/wrong_extension.jpg")


def test_load_parameters_wrong_extension():
    with pytest.raises(ValueError):
        LoadParameters("Pliki testowe/wrong_extension.txt")
