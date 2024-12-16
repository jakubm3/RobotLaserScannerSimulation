class Point:
    def __init__(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Coordinates must be integers")
        self.x = x
        self.y = y


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.points = []

    def LinePoints(self):
        swapped_axes = False
        distance_x = self.end.x - self.start.x
        distance_y = self.end.y - self.start.y
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y
        slope = distance_y / distance_x

        if abs(distance_y) > abs(distance_x):
            x1, y1, x2, y2 = y1, x1, y2, x2
            distance_x, distance_y = distance_y, distance_x
            slope = distance_y / distance_x
            swapped_axes = True

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        error = None
        y0 = y1

        for x in range(x1, x2+1):
            if swapped_axes:
                self.points.append(Point(y0, x))
            else:
                self.points.append(Point(x, y0))

            error += slope

            if abs(error) >= 0.5:
                y0 += 1 if y2 > y1 else -1
                error -= 1.0 if error > 0 else -1.0

        return self.points[::-1] if swapped_axes else self.points


def LoadImage(image_path):
    pass


def LoadParmeters(file_path):
    pass


def DrawLine(image, x1, y1, x2, y2):
    pass


def FindObstacle(image, line):
    pass


def FindLineEndingPoints(x1, y1, angle):
    pass
