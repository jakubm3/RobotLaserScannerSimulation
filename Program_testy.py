import pytest
from PIL import Image
from Program import (Point, Line, LoadParameters,
                     OutOfRangeError, DrawLine, FindObstacle,
                     FindLineEndingPoints)


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


def test_drawline():
    width, height = 320, 240
    image = Image.new("RGB", (width, height), "white")
    start = Point(20, 70)
    end = Point(60, 50)
    line = Line(start, end)
    DrawLine(image, line)
    pixels = image.load()
    for point in line.LinePoints():
        assert pixels[point.x, point.y] == (255, 0, 0)


def test_drawline_out_of_bounds():
    width, height = 320, 240
    image = Image.new("RGB", (width, height), "white")
    start = Point(-10, 50)
    end = Point(110, 50)
    line = Line(start, end)
    DrawLine(image, line)
    pixels = image.load()
    for point in line.LinePoints():
        if 0 <= point.x <= width and 0 <= point.y <= height:
            assert pixels[point.x, point.y] == (255, 0, 0)


def test_find_obstacle_found():
    image = Image.new("RGB", (100, 100), "white")
    pixels = image.load()
    pixels[50, 50] = (0, 0, 0)
    start_point = Point(0, 0)
    end_point = Point(100, 100)
    line = Line(start_point, end_point)
    obstacle = FindObstacle(image, line)
    assert obstacle == Point(50, 50)


def test_find_obstacle_not_found():
    image = Image.new("RGB", (100, 100), "white")
    start_point = Point(0, 0)
    end_point = Point(100, 100)
    line = Line(start_point, end_point)
    obstacle = FindObstacle(image, line)
    assert obstacle is None


def test_find_line_ending_points_0_degrees():
    x1, y1 = 50, 50
    angle = 0
    x2, y2 = FindLineEndingPoints(x1, y1, angle)
    assert (x2, y2) == (110, 50)


def test_find_line_ending_points_90_degrees():
    x1, y1 = 50, 50
    angle = 90
    x2, y2 = FindLineEndingPoints(x1, y1, angle)
    assert (x2, y2) == (50, 110)


def test_find_line_ending_points_180_degrees():
    x1, y1 = 50, 50
    angle = 180
    x2, y2 = FindLineEndingPoints(x1, y1, angle)
    assert (x2, y2) == (-10, 50)


def test_find_line_ending_points_270_degrees():
    x1, y1 = 50, 50
    angle = 270
    x2, y2 = FindLineEndingPoints(x1, y1, angle)
    assert (x2, y2) == (50, -10)


def test_find_line_ending_points_45_degrees():
    x1, y1 = 50, 50
    angle = 45
    x2, y2 = FindLineEndingPoints(x1, y1, angle)
    assert (x2, y2) == (92, 92)


def test_find_line_ending_points_135_degrees():
    x1, y1 = 50, 50
    angle = 135
    x2, y2 = FindLineEndingPoints(x1, y1, angle)
    assert (x2, y2) == (8, 92)
