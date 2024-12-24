from Errors import WrongExtensionError, OutOfRangeError
from PIL import Image
import numpy as np
from Classes import Point


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
