class Point:
    def __init__(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Coordinates must be integers")
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
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

    def LinePoints(self) -> list:
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y

        distance_x = abs(x2 - x1)
        distance_y = abs(y2 - y1)

        step_x = 1 if x1 < x2 else -1
        step_y = 1 if y1 < y2 else -1
        error = distance_x - distance_y

        while True:
            self.points.append(Point(x1, y1))
            if x1 == x2 and y1 == y2:
                break
            e2 = 2 * error
            if e2 > -distance_y:
                error -= distance_y
                x1 += step_x
            if e2 < distance_x:
                error += distance_x
                y1 += step_y
        return self.points
