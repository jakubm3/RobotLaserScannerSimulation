import pytest
from PIL import Image
import numpy as np
from Errors import WrongExtensionError, OutOfRangeError
from DataLoad import (LoadImageWithArray, LoadParameters)
from Functions import (Point, Line, DrawLine, FindObstacle,
                       FindLineEndingPoints)


def test_point_integer():
    point = Point(1, 2)
    assert point.x == 1
    assert point.y == 2


def test_point_equality():
    point1 = Point(1, 1)
    point2 = Point(1, 1)
    point3 = Point(2, 2)
    assert point1 == point2
    assert point1 != point3


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


def test_line_bresenham_diagonal():
    point1 = Point(0, 0)
    point2 = Point(3, 3)
    line = Line(point1, point2)
    line_points = line.LinePoints()
    assert line_points == [Point(0, 0), Point(1, 1),
                           Point(2, 2), Point(3, 3)]


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


def test_load_parameters_wrong_extension():
    with pytest.raises(ValueError):
        LoadParameters("Pliki testowe/wrong_extension.txt")


def test_load_image_valid(tmp_path):
    test_image = Image.new('RGB', (320, 240), color='white')
    image_path = tmp_path / "test.png"
    test_image.save(image_path)

    image, array = LoadImageWithArray(str(image_path))
    assert isinstance(image, Image.Image)
    assert isinstance(array, np.ndarray)
    assert array.shape == (240, 320, 3)


def test_load_image_wrong_extension():
    with pytest.raises(ValueError):
        LoadParameters("Pliki testowe/wrong_extension.jpg")


def test_load_image_nonexistent():
    with pytest.raises(FileNotFoundError):
        LoadImageWithArray("nonexistent.png")


def test_drawline():
    width, height = 320, 240
    image = Image.new("RGB", (width, height), "white")
    image_array = np.array(image)
    start = Point(20, 70)
    end = Point(60, 50)
    line = Line(start, end)
    line_points = line.LinePoints()
    DrawLine(image_array, line_points)
    updated_image = Image.fromarray(image_array)
    pixels = updated_image.load()
    for point in line_points:
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
    ending_point = FindLineEndingPoints(x1, y1, angle)
    x2, y2 = ending_point.x, ending_point.y
    assert Point(x2, y2) == Point(110, 50)


def test_find_line_ending_points_90_degrees():
    x1, y1 = 50, 50
    angle = 90
    ending_point = FindLineEndingPoints(x1, y1, angle)
    x2, y2 = ending_point.x, ending_point.y
    assert Point(x2, y2) == Point(50, -10)


def test_find_line_ending_points_180_degrees():
    x1, y1 = 50, 50
    angle = 180
    ending_point = FindLineEndingPoints(x1, y1, angle)
    x2, y2 = ending_point.x, ending_point.y
    assert Point(x2, y2) == Point(-10, 49)


def test_find_line_ending_points_270_degrees():
    x1, y1 = 50, 50
    angle = 270
    ending_point = FindLineEndingPoints(x1, y1, angle)
    x2, y2 = ending_point.x, ending_point.y
    assert Point(x2, y2) == Point(49, 110)


def test_find_line_ending_points_45_degrees():
    x1, y1 = 50, 50
    angle = 45
    ending_point = FindLineEndingPoints(x1, y1, angle)
    x2, y2 = ending_point.x, ending_point.y
    assert Point(x2, y2) == Point(92, 7)


def test_find_line_ending_points_135_degrees():
    x1, y1 = 50, 50
    angle = 135
    ending_point = FindLineEndingPoints(x1, y1, angle)
    x2, y2 = ending_point.x, ending_point.y
    assert Point(x2, y2) == Point(7, 7)


def test_find_line_ending_points_angle_greater_than_360():
    x1, y1 = 50, 50
    angle = 450
    ending_point = FindLineEndingPoints(x1, y1, angle)
    x2, y2 = ending_point.x, ending_point.y
    assert Point(x2, y2) == Point(50, -10)
