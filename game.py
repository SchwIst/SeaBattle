import json
import os

import colorama

from field import Field
from player import Player
from utils import Display, move_print, FILE_TEMPLATE


class Game(Display):
    _fields: list[Field] = []
    _players: list[Player] = []

    is_running: bool
    _should_redraw: bool = True

    def __init__(self):
        colorama.init()

        self._print_field_template()

        self.create_fields()

        self._players = [
            Player(),
            Player()
        ]

    def create_fields(self):
        for field in FILE_TEMPLATE["fields"]:
            [x, y] = field["position"]
            [width, height] = field["size"]

            field_object = Field(width, height, x, y)
            field_object.fill()

            self._fields.append(field_object)

    def run(self):
        from msvcrt import getch

        self.is_running = True
        while self.is_running:
            if self._should_redraw:
                self.print()
                self._should_redraw = False

            char = getch()

            action = self._players[0].react_to_keys(char)

            if isinstance(action, bool):
                self._fields[0].create_ship()
                self._should_redraw = True
            elif isinstance(action, tuple):
                self._fields[0].move_last_ship(action)
                self._should_redraw = True
            else:
                self._fields[0].rotate_last_ship(action)
                self._should_redraw = True

    @staticmethod
    def _clear():
        os.system(
            "cls"
            if os.name == "nt"
            else "clear"
        )

    def _print_field_template(self):
        Game._clear()

        with open(FILE_TEMPLATE["filename"], "r", encoding="UTF-8") as file:
            for line in file.readlines():
                print(line.removesuffix("\n"))

    def print(self):
        for field in self._fields:
            field.print()

        _, move_y = FILE_TEMPLATE["template_size"]
        move_print("", 1, move_y)
