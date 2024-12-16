import pytest
from Program import Point


def test_point_integer():
    point = Point(1, 2)
    assert point.x == 1
    assert point.y == 2


def test_point_not_integer():
    with pytest.raises(TypeError):
        Point('a', 3.5)
