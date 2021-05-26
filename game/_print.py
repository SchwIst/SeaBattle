import os

from game.utils import FILE_TEMPLATE, cursor_end_position


def _clear():
    os.system(
        "cls"
        if os.name == "nt"
        else "clear"
    )


def _print_field_template(self):
    _clear()

    with open(FILE_TEMPLATE["filename"], "r", encoding="UTF-8") as file:
        for line in file.readlines():
            print(line.removesuffix("\n"))


def display(self):
    if self.message_box.should_redraw:
        self._print_field_template()
        self.message_box.display()
        self.message_box.should_redraw = False

    self._user.display()

    cursor_end_position()
