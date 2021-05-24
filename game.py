import json
import os

import colorama
from colorama import Cursor

from field import Field
from utils import Display


class Game(Display):
    _fields: list[Field] = []

    def __init__(self):
        self._file_template = json.loads("".join(open("file_template.json").readlines()))

        colorama.init()

        self._print_field_template()

        self.create_fields()

    def create_fields(self):
        for field in self._file_template["fields"]:
            [x, y] = field["position"]
            [width, height] = field["size"]

            self._fields.append(Field(width, height, x, y))

    def run(self):
        for field in self._fields:
            field.fill()

        self.print()

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
        print(Cursor.POS(1, move_y))

