from PIL import Image
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


def LoadImageWithArray(image_path):
    if not image_path.endswith(".png"):
        raise WrongExtensionError("Wrong file extension")
    image = Image.open(image_path)
    return image, np.array(image)


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


def FindObstacle(image, line):
    image_array = np.array(image.convert("RGB"))
    height, width = image_array.shape[:2]
    for point in line.LinePoints():
        if 0 <= point.x < width and 0 <= point.y < height:
            neighbors = [
                (point.x - 1, point.y), (point.x + 1, point.y),
                (point.x, point.y - 1), (point.x, point.y + 1),
                (point.x - 1, point.y - 1), (point.x + 1, point.y + 1),
                (point.x - 1, point.y + 1), (point.x + 1, point.y - 1)
            ]
            for nx, ny in neighbors:
                if (image_array[ny, nx] == [0, 0, 0]).all():
                    return point
            if (image_array[point.y, point.x] == [0, 0, 0]).all():
                return point
    return None


def DrawLine(image_array, line_points, line_length=60):
    for point in line_points[:line_length]:
        image_array[point.y, point.x] = [255, 0, 0]


def FindLineEndingPoints(x1, y1, angle, length=60):
    angle = int(angle) % 360
    angle_rad = math.radians(angle)
    x2 = x1 + length * math.cos(angle_rad)
    y2 = y1 - length * math.sin(angle_rad)
    return Point(int(x2), int(y2))


def SimulateLaserScanner(image_path, params_path):
    image, image_array = LoadImageWithArray(image_path)
    start_point, base_angle = LoadParameters(params_path)
    line_lengths = []
    line_angles = [base_angle - 90 + 10 * i for i in range(19)]

    for angle in line_angles:
        end_point = FindLineEndingPoints(
            start_point.x, start_point.y, angle)
        line = Line(start_point, end_point)
        line_points = line.LinePoints()
        line_length = 0
        obstacle = FindObstacle(image, line)

        for point in line_points:
            if 0 <= point.x < 320 and 0 <= point.y < 240:
                if point == obstacle:
                    line_length += 1
                    break
                line_length += 1
            else:
                break
        line_lengths.append(line_length)
        DrawLine(image_array, line_points, line_length)

    return image_array, line_lengths


def main():
    environment_path = "otoczenie.png"
    params_path = "parametry.txt"

    try:
        print("Starting simulation")
        image_array, line_lengths = (
            SimulateLaserScanner(environment_path, params_path))

        simulation_image = Image.fromarray(image_array)
        simulation_image.save("symulacja.png")
        print("Simulation image saved as 'symulacja.png'")

        with open("wyniki.txt", "w") as file:
            file.write('\n'.join(map(str, line_lengths)))
        print("Line lengths saved to 'wyniki.txt'")

    except WrongExtensionError as e:
        print(f"Error: {e}")
    except OutOfRangeError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
