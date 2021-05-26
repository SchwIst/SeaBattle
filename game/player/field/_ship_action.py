import random

from game.player.field.cells import TYPES
from game.player.field.ship import Ship


def create_ship(self) -> bool:
    if len(self.possible_ships) != 0:
        ship_length = self.possible_ships.pop()

        x, y = 1, 1

        coordinates: dict[tuple[int, int], bool] = {}
        for i in self.ships:
            for j in i.get_all_coordinates():
                coordinates[j] = True

        while (x, y) in coordinates.keys():
            x = random.randint(0, self._width - ship_length)
            y = random.randint(0, self._height - ship_length)

        self.ships.append(Ship(ship_length, x, y))

        return False

    return True


def not_intersect_padding(self):
    if len(self.ships) > 0:
        used_coordinates: dict[tuple[int, int], bool] = {}

        ship_coordinates = self.ships[-1].get_all_coordinates()

        for ship in self.ships[0:-1]:
            for i in ship.get_padding_coordinates():
                if i not in used_coordinates.keys():
                    used_coordinates[i] = True

        for i in ship_coordinates:
            if i in used_coordinates.keys():
                return False

    return True


def not_intersect(self):
    used_coordinates: dict[tuple[int, int], bool] = {}

    for ship in self.ships:
        for i in ship.get_all_coordinates():
            if i not in used_coordinates.keys():
                used_coordinates[i] = True
            else:
                return False

    return True


def move_last_ship(self, vector: tuple[int, int]):
    if len(self.ships) > 0:
        self.ships[-1].move(vector[0], vector[1])

        if self.not_intersect():
            return

        self.ships[-1].move(-vector[0], -vector[1])


def rotate_last_ship(self):
    if len(self.ships) > 0:
        self.ships[-1].rotate()


def pop_last_ship(self):
    s = self.ships.pop()
    self.possible_ships.append(s.size)


def bake_ships(self):
    for ship in self.ships:
        for y, x in ship.get_all_coordinates():
            self.set_cell(x, y, TYPES["ship"])

    for i in range(len(self.ships)):
        self.ships.pop()
