import colorama

from old_version.game.player import Player
from old_version.game.player.field import Field
from old_version.game.utils import Display, MessageBox


class Game(Display):
    _fields: list[Field] = []
    _user: Player
    _computer: Player

    _should_redraw: bool = True
    _start_match: bool = False

    from ._print import display, _clear
    from ._print import _print_field_template

    from ._savings import save, restore

    def __init__(self):
        colorama.init()

        self._print_field_template()

        self.create_fields()

        self._user = Player(self._fields[0], self._fields[1])
        self._computer = Player(self._fields[1], self._fields[0])

        self.message_box = MessageBox()

    from ._running import run, play, set_user_ships, set_computer_ships

    from ._creation import create_fields
