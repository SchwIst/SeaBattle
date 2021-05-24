import json
import os

import colorama

from field import Field
from player import Player
from utils import Display, move_print


class Game(Display):
    _fields: list[Field] = []
    _players: list[Player] = []

    is_running: bool
    _should_redraw: bool = True

    def __init__(self):
        self._file_template = json.loads("".join(open("file_template.json").readlines()))

        colorama.init()

        self._print_field_template()

        self.create_fields()

        self._players = [
            Player(),
            Player()
        ]

    def create_fields(self):
        for field in self._file_template["fields"]:
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

            self._players[0].react_to_keys(getch())

    @staticmethod
    def _clear():
        os.system(
            "cls"
            if os.name == "nt"
            else "clear"
        )

    def _print_field_template(self):
        Game._clear()

        with open(self._file_template["filename"], "r", encoding="UTF-8") as file:
            for line in file.readlines():
                print(line.removesuffix("\n"))

    def print(self):
        for field in self._fields:
            field.print()

        _, move_y = self._file_template["template_size"]
        move_print("", 1, move_y)
