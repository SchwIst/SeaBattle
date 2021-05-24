from abc import abstractmethod

from colorama import Cursor


class Display:
    @abstractmethod
    def print(self):
        pass


def move_print(text: str, x: int, y: int):
    print(Cursor.POS(x, y) + text, end='')


class MessageBox(Display):
    message: str = ""

    def __init__(self, x, y, width, height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    def print(self):
        if len(self.message) > self._width:
            raise Exception("Cannot display message - it's too long")

        move_print(self.message, self._x, self._y)
