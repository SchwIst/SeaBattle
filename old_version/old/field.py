import numpy as np


class Field:
    size: tuple[int, int]
    arr: np.ndarray

    def __init__(self):
        pass

    @staticmethod
    def from_byte_array(size: tuple[int, int], array: list[bytes]):
        field = Field()

        field.size = size
        field.arr = np.array(array).reshape(size)

        return field

    @staticmethod
    def empty(size: tuple[int, int]):
        field = Field()

        field.size = size
        field.arr = np.zeros(size[0] * size[1]).reshape(size)

        return field
