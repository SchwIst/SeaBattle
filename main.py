import datetime
import io

import numpy as np

from colored import fore, stylize, fg, bg


class Cell:
    empty = stylize(' ', bg("white"))
    ship = stylize('@', fg("blue") + bg("white"))
    damaged = stylize('X', fg("red") + bg("white"))
    miss = stylize('•', fg("grey_74") + bg("white"))
    killed = stylize('X', fg("white") + bg("red"))
    striked = stylize('0', fg("yellow"))

    SIZE_IN_BITS = 3

    _type = [
        empty,
        ship,
        damaged,
        miss,
        killed
    ]

    @staticmethod
    def byte_to_color(byte: int) -> str:
        return Cell._type[byte]


class Ship:
    def __init__(self, size: list[int], position: list[int]):
        self.size = size
        self.position = position


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


class Game:
    _saves_filename = "savefile"

    def __init__(self):
        self.field = Field.empty((10, 10))

    def start(self):
        pass

    def end(self):
        pass

    def save(self):
        with open(Game._saves_filename, "wb") as file:
            file.write(bytes(self.field.arr.astype(np.uint8)))

    def restore(self):
        with open(Game._saves_filename, "rb") as file:
            self.field = Field.from_byte_array((10, 10), list(file.readline()))


def main():
    game = Game()


if __name__ == '__main__':
    main()
