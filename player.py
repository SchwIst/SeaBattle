from abc import abstractmethod
from typing import Union, Callable

from cells import CellTypes, Cell
from field import Field
from ship import Ship
from utils import Display, move_print, MessageBox


class Shooter:
    @abstractmethod
    def shoot(self, field: Field, result_message_box: MessageBox):
        pass

    @staticmethod
    def get_message(field: Field, shoot_x: int, shoot_y: int) -> str:
        _match: dict[str, str] = {
            CellTypes["empty"].text: "Вы промахнулись",
            CellTypes["ship"].text: "Вы попали!! 😎",
        }

        cell = field.cells[shoot_y][shoot_x]

        return _match[cell.text]


class Input:
    @abstractmethod
    def react_to_keys(self, pressed_key: bytes):
        pass


class Player(Shooter, Display, Input):
    chosen_position_x: int
    chosen_position_y: int

    moving_ships: bool = True

    def print(self):
        move_print(str(CellTypes["selected"]), self.chosen_position_x, self.chosen_position_y)

    def shoot(self, field: Field, result_message_box: MessageBox):
        message = Shooter.get_message(field, self.chosen_position_x, self.chosen_position_y)

        result_message_box.message = message

        _match: dict[str, Cell] = {
            CellTypes["empty"].text: CellTypes["miss"],
            CellTypes["ship"].text: CellTypes[""],
        }

    def react_to_keys(self, pressed_key: bytes) -> Union[tuple[int, int], Callable[[Ship], None]]:
        _match: dict[bytes, Union[tuple[int, int], Callable[[Ship], None]]] = {
            b"w": (0, -1),
            b"a": (-1, 0),
            b"s": (0, 1),
            b"d": (1, 0),
            b"r": lambda x: x.rotate()
        }

        return _match[pressed_key]
