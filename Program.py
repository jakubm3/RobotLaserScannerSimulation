from PIL import Image, ImageDraw
import numpy as np
import math


class WrongExtensionError(ValueError):
    def __init__(self, message="Wrong file extension"):
        super().__init__(message)


class OutOfRangeError(ValueError):
    def __init__(self, message="Data out of range"):
        super().__init__(message)


class Point:
    def __init__(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Coordinates must be integers")
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


class Line:
    def __init__(self, start: Point, end: Point):
        if not isinstance(start, Point) or not isinstance(end, Point):
            raise TypeError("Line must be defined by two points")
        self.start = start
        self.end = end
        self.points = []

    def LinePoints(self):
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y

        distance_x = abs(x2 - x1)
        distance_y = abs(y2 - y1)

        steep = distance_y > distance_x

        if steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
            distance_x, distance_y = distance_y, distance_x

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        error = distance_x // 2
        y0 = y1
        step_y = 1 if y1 < y2 else -1

        for x in range(x1, x2 + 1):
            if steep:
                self.points.append(Point(y0, x))
            else:
                self.points.append(Point(x, y0))

            error -= distance_y
            if error < 0:
                y0 += step_y
                error += distance_x
        return self.points


def LoadImage(image_path):
    if not image_path.endswith(".png"):
        raise WrongExtensionError("Wrong file extension")
    return Image.open(image_path)


def LoadParameters(file_path):
    if not file_path.endswith(".txt"):
        raise WrongExtensionError("Wrong file extension")
    with open(file_path, "r") as handle:
        values = tuple(handle.readline().split())
        if len(values) != 3:
            raise ValueError("Not enough data")
        if (
            int(values[0]) < 0 or int(values[0]) > 320 or
            int(values[1]) < 0 or int(values[1]) > 240 or
            int(values[2]) < 0 or int(values[2]) > 360
        ):
            raise OutOfRangeError("Data has to be within the range")
        starting_point = Point(int(values[0]), int(values[1]))
        angle = values[2]
    return starting_point, int(angle)


def DrawLine(image, line):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    for point in line.LinePoints():
        if point.x in range(0, width+1) and point.y in range(0, height+1):
            draw.point((point.x, point.y), fill="red")


def FindObstacle(image, line):
    image_array = np.array(image)
    height, width, _ = image_array.shape
    for point in line.LinePoints():
        if 0 <= point.x < width and 0 <= point.y < height:
            if np.all(image_array[point.y, point.x][:3] == [0, 0, 0]):
                return point
    return None


def FindLineEndingPoints(x1, y1, angle, length=60):
    angle = int(angle)
    if angle > 360:
        round_angles = angle // 360
        angle -= 360 * round_angles
    elif angle < 0:
        raise ValueError("Angle has to be positive")
    angle_rad = math.radians(angle)
    x2 = x1 + length * math.cos(angle_rad)
    y2 = y1 - length * math.sin(angle_rad)
    return Point(round(x2), round(y2))


def CalculateDistance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)
