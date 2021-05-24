from cells import CellTypes
from utils import Display, move_print


class Ship(Display):
    size: int
    x: int
    y: int
    is_horizontal: bool

    def __init__(self, size: int, x: int, y: int):
        self.size = size
        self.x = x
        self.y = y
        self.is_horizontal = True

    def move(self, offset_x: int, offset_y: int):
        self.x += offset_x
        self.y += offset_y

    def _get_vector(self) -> tuple[int, int]:
        x = 0
        y = 0

        if self.is_horizontal:
            x = 1
        else:
            y = 1

        return x, y

    def get_all_coordinates(self) -> list[tuple[int, int]]:
        offset_x, offset_y = self._get_vector()

        coordinates: list[tuple[int, int]] = []
        for i in range(self.size):
            coordinates.append((self.x + offset_x * i, self.y + offset_y * i))

        return coordinates

    def get_padding_coordinates(self) -> list[tuple[int, int]]:
        offset_x, offset_y = self._get_vector()

        vertical_x, vertical_y = [0, 1]
        horizontal_x, horizontal_y = [1, 0]

        padding_positions = []
        for i in range(-1, self.size + 1):
            for j in range(-1, 1 + 1):
                if self.is_horizontal:
                    padding_positions.append((
                        vertical_x * j + horizontal_x * i + self.x,
                        vertical_y * j + horizontal_y * i + self.y
                    ))
                else:
                    padding_positions.append((
                        vertical_x * i + horizontal_x * j + self.x,
                        vertical_y * i + horizontal_y * j + self.y
                    ))

        return padding_positions

    def print(self):
        move_print(str(CellTypes["ship"]), self.x, self.y)
