from colorama import Fore, Back
from colorama.ansi import AnsiBack, AnsiFore

from utils import Display


class Cell(Display):
    foreground: AnsiFore
    background: AnsiBack
    text: str

    def __init__(self, text: str, foreground: AnsiFore, background: AnsiBack):
        self.text = text
        self.background = background
        self.foreground = foreground

    def __str__(self):
        return self.background + \
               self.foreground + \
               self.text + \
               Fore.RESET + Back.RESET

    def print(self):
        print(str(self), end='')


CellTypes: dict[str, Cell] = {
    "empty": Cell(' ', Fore.WHITE, Back.WHITE),
    "ship": Cell('@', Fore.BLUE, Back.WHITE),
    "damaged": Cell('X', Fore.RED, Back.WHITE),
    "miss": Cell('•', Fore.BLACK, Back.WHITE),
    "killed": Cell('X', Fore.WHITE, Back.RED),
    "struck": Cell('0', Fore.YELLOW, Back.RESET)
}


