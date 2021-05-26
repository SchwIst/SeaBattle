from abc import abstractmethod, abstractproperty

from game.player import Cell
from game.player.field import TYPES
from game.player.field import Field
from game.utils import MessageBox


class Shooter:
    @abstractmethod
    def get_enemy_field_hidden(self) -> Field:
        pass

    @abstractmethod
    def get_enemy_field(self):
        pass

    @abstractmethod
    def get_shoot_coordinates(self) -> tuple[int, int]:
        pass

    def shoot(self, result_message_box: MessageBox):
        enemy_field_hidden = self.get_enemy_field_hidden()
        enemy_field = self.get_enemy_field()
        shoot_x, shoot_y = self.get_shoot_coordinates()

        _match: dict[str, tuple[str, Cell]] = {
            TYPES["empty"].text: ("Вы промахнулись", TYPES["miss"]),
            TYPES["ship"].text: ("Вы попали!! 😎", TYPES["damaged"]),
        }

        message, new_cell = _match[enemy_field.get_cell(shoot_x, shoot_y)]

        result_message_box.message = message

        enemy_field.set_cell(shoot_x, shoot_y, new_cell)
        enemy_field_hidden.set_cell(shoot_x, shoot_y, new_cell)