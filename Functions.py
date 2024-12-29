import numpy as np
import math
from Classes import Point, Line
from DataLoad import LoadImageWithArray, LoadParameters
from Errors import WrongExtensionError, OutOfRangeError
from PIL import Image


def FindObstacle(image, line):
    image_array = np.array(image.convert("RGB"))
    height, width = image_array.shape[:2]
    prev_point = None

    for point in line.LinePoints():
        if 0 <= point.x < width and 0 <= point.y < height:
            if (image_array[point.y, point.x] == [0, 0, 0]).all():
                return point

            neighbors = [
                (point.x - 1, point.y),
                (point.x + 1, point.y),
                (point.x, point.y - 1),
                (point.x, point.y + 1)
            ]

            for nx, ny in neighbors:
                if 0 <= nx < width and 0 <= ny < height:
                    if (image_array[ny, nx] == [0, 0, 0]).all():
                        return point

            if prev_point is not None:
                dx = point.x - prev_point.x
                dy = point.y - prev_point.y

                if abs(dx) == 1 and abs(dy) == 1:
                    corner1 = (prev_point.x, point.y)
                    corner2 = (point.x, prev_point.y)

                    if (0 <= corner1[0] < width and
                            0 <= corner1[1] < height and
                            0 <= corner2[0] < width and
                            0 <= corner2[1] < height):
                        corner1_black = (
                            image_array[corner1[1], corner1[0]] == [0, 0, 0]
                        ).all()
                        corner2_black = (
                            image_array[corner2[1], corner2[0]] == [0, 0, 0]
                        ).all()

                        if corner1_black and corner2_black:
                            return prev_point

            prev_point = point

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


def Main():
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
