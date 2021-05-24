from collections import Callable

from cells import Cell, CellTypes
from ship import Ship
from utils import Display, move_print


class Field(Display):
    _width: int
    _height: int

    _x: int = 0
    _y: int = 0

    _possible_ships = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

    _ships: list[Ship]

    _cells: list[list[Cell]]

    def __init__(self, width: int, height: int, x: int, y: int):
        self._width = width
        self._height = height

        self._x = x
        self._y = y

        self._cells = []
        self._ships = []

    def _empty(self):
        for i in range(self._height):
            self._cells.append([])
            for j in range(self._width):
                self._cells[i].append(CellTypes["empty"])

    def fill(self):
        self._empty()

    def get_cell(self, x: int, y: int):
        return self._cells[y][x]

    def create_ship(self):
        l = self._possible_ships.pop()

        self._ships.append(Ship(l, 1, 1))

    def move_last_ship(self, vector: tuple[int, int]):
        self._ships[-1].move(vector[0], vector[1])

    def rotate_last_ship(self, func: Callable[[Ship], None]):
        func(self._ships[-1])

    def print(self):
        for x, row in enumerate(self._cells):
            for y, element in enumerate(row):
                lx, ly = self._x + x, self._y + y

                move_print(str(element), lx, ly)

        for ship in self._ships:
            for x, y in ship.get_all_coordinates():
                move_print(str(CellTypes["ship"]), x + self._x, y + self._y)
