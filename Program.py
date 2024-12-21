import os


class Point:
    def __init__(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Coordinates must be integers")
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        if not isinstance(start, Point) or not isinstance(end, Point):
            raise TypeError("Line must be defined by two points")
        self.start = start
        self.end = end
        self.points = []

    def LinePoints(self):
        distance_x = abs(self.end.x - self.start.x)
        distance_y = abs(self.end.y - self.start.y)
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        step_x = 1 if x1 < x2 else -1
        step_y = 1 if y1 < y2 else -1

        if distance_x == 0:
            for y in range(y1, y2+step_y, step_y):
                self.points.append((x1, y))
            return self.points

        inverted_axes = distance_y > distance_x
        if inverted_axes:
            distance_x, distance_y = distance_y, distance_x
        error = 2 * distance_y - distance_x
        y0 = y1

        for x in range(x1, x2+step_x, step_x):
            if inverted_axes:
                self.points.append((y0, x))
            else:
                self.points.append((x, y0))
            if error > 0:
                y0 += step_y
                error -= 2 * distance_x
            error += 2 * distance_y
        return self.points


def LoadImage(image_path):
    pass


def LoadParameters(file_path):
    with open(file_path, "r") as handle:
        x, y, angle = handle.readline().split()
        x, y, angle = int(x), int(y), int(angle)
    return x, y, angle


def DrawLine(image, line):
    pass


def FindObstacle(image, line):
    pass


def FindLineEndingPoints(x1, y1, angle):
    pass


print(LoadParameters("nazwy.txt"))