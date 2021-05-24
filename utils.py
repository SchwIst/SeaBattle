import json
from abc import abstractmethod

from colorama import Cursor

FILE_TEMPLATE = json.loads("".join(open("file_template.json").readlines()))

class Display:
    @abstractmethod
    def print(self):
        pass


def move_print(text: str, x: int, y: int):
    print(Cursor.POS(x, y) + text, end='')


class MessageBox(Display):
    message: str = ""

    def __init__(self,):
        self._x, self._y = FILE_TEMPLATE["message_box"]["position"]
        self._width, self._height = FILE_TEMPLATE["message_box"]["size"]

    def print(self):
        if len(self.message) > self._width:
            raise Exception("Cannot display message - it's too long")

        move_print(self.message, self._x, self._y)
