from abc import abstractmethod

from old_version.game.player import Cell
from old_version.game.player.field import Field
from old_version.game.player.field import TYPES
from old_version.game.utils import MessageBox


class Shooter:
    @abstractmethod
    def get_shoot_coordinates(self) -> tuple[int, int]:
        pass

    enemy_field: Field
    enemy_field_hidden: Field

    def shoot(self, result_message_box: MessageBox):
        shoot_x, shoot_y = self.get_shoot_coordinates()

        _match: dict[str, tuple[str, Cell]] = {
            TYPES["empty"].text: ("Вы промахнулись", TYPES["miss"]),
            TYPES["ship"].text: ("Вы попали!! 😎", TYPES["damaged"]),
        }

        text = self.enemy_field.get_cell(shoot_y, shoot_x).text
        if text in _match.keys():
            message, new_cell = _match[text]

            result_message_box.message = message
            result_message_box.should_redraw = True

            self.enemy_field.set_cell(shoot_x, shoot_y, new_cell)
            self.enemy_field_hidden.set_cell(shoot_x, shoot_y, new_cell)
