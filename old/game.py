import msvcrt
import os

import numpy as np

from cell import Cell
from field import Field
from ship import Ship
from utils import char_to_vector


class Game:
    _saves_filename = "savefile"
    _ships_count = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

    def start(self):
        self.build_field()

    def end(self):
        pass

    def save(self):
        with open(Game._saves_filename, "wb") as file:
            file.write(bytes(self.field.arr.astype(np.uint8)))

    def restore(self):
        with open(Game._saves_filename, "rb") as file:
            self.field = Field.from_byte_array((10, 10), list(file.readline()))

    @staticmethod
    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    def display(self):
        pass

    def build_field(self):
        field_size = (
            int(input("Ширина поля: ")),
            int(input("Высота поля: "))
        )

        field = Field.empty(field_size)

        ships: list[Ship] = []

        def intersect() -> bool:
            ships_coords: list[np.ndarray] = list(map(
                lambda x: x.get_padding_coords(),
                ships
            ))

            ship_coords_dict: dict[np.ndarray, int] = {}

            for k in ships_coords:
                for l in k:
                    if l not in ship_coords_dict.keys():
                        ship_coords_dict[l] = 0
                    else:
                        return False

            return True

        for i in Game._ships_count:
            ship = Ship(i, np.array(0, 0))

            while True:
                char = msvcrt.getch()

                if char == b"\r" and not intersect():
                    break
                else:
                    vector = char_to_vector(char)

                    ship.move(vector)

        for i in ships:
            field.arr[i.position[0]][i.position[1]] = Cell.color_to_byte(Cell.ship)
