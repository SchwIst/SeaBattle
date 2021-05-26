from typing import Union, Callable

from game.player.field import Cell, TYPES
from game.player.field import Field
from game.player.field import Ship
from game.utils import Display, move_print
from .read_input import Input
from .shooter import Shooter


class Player(Shooter, Display, Input):
    chosen_position_x: int
    chosen_position_y: int

    field: Field
    enemy_field: Field
    enemy_field_hidden: Field

    moving_ships: bool = True

    def __init__(self, our_field: Field, enemy_field: Field):
        self.field = our_field

        self.enemy_field = enemy_field
        self.enemy_field_hidden = enemy_field.clone()

        self.chosen_position_x = 0
        self.chosen_position_y = 0

    def get_enemy_field_hidden(self) -> Field:
        return self.enemy_field_hidden

    def get_enemy_field(self):
        return self.enemy_field

    def get_shoot_coordinates(self) -> tuple[int, int]:
        return self.chosen_position_x, self.chosen_position_y

    def display(self):
        self.field.display()
        self.enemy_field.display()

        move_print(str(TYPES["selected"]), self.chosen_position_x, self.chosen_position_y)

    def react_to_keys(self, pressed_key: bytes) -> Union[tuple[int, int], Callable[[Ship], None], bool]:
        _match: dict[bytes, Union[tuple[int, int], Callable[[Ship], None]], bool] = {
            b"w": (0, -1),
            b"a": (-1, 0),
            b"s": (0, 1),
            b"d": (1, 0),
            b"r": lambda x: x.rotate(),
            b"e": True
        }

        return _match[pressed_key]
