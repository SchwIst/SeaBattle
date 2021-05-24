from colorama import Cursor

from cells import Cell, CellTypes
from utils import Display


class Field(Display):
    _width: int
    _height: int

    _x: int = 0
    _y: int = 0

    _cells: list[list[Cell]]

    def __init__(self, width: int, height: int, x: int, y: int):
        self._width = width
        self._height = height

        self._x = x
        self._y = y

        self._cells = []

    def _empty(self):
        for i in range(self._height):
            self._cells.append([])
            for j in range(self._width):
                self._cells[i].append(CellTypes["ship"])

    def fill(self):
        self._empty()

    def print(self):
        for x, row in enumerate(self._cells):
            for y, element in enumerate(row):
                move = Cursor.POS(self._x + x, self._y + y)

                print(move + str(element), end='')
