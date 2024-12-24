class WrongExtensionError(ValueError):
    def __init__(self, message="Wrong file extension"):
        super().__init__(message)


class OutOfRangeError(ValueError):
    def __init__(self, message="Data out of range"):
        super().__init__(message)
