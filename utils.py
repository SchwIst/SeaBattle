from abc import abstractmethod

from colorama import Cursor


class Display:
    @abstractmethod
    def print(self):
        pass


def move_print(text: str, x: int, y: int):
    print(Cursor.POS(x, y) + text, end='')
