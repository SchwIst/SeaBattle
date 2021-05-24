from colored import stylize, bg, fg


class Cell:
    empty = stylize(' ', bg("white"))
    ship = stylize('@', fg("blue") + bg("white"))
    damaged = stylize('X', fg("red") + bg("white"))
    miss = stylize('•', fg("grey_74") + bg("white"))
    killed = stylize('X', fg("white") + bg("red"))
    struck = stylize('0', fg("yellow"))

    _type = [
        empty,
        ship,
        damaged,
        miss,
        killed
    ]

    @staticmethod
    def byte_to_color(byte: int) -> str:
        return Cell._type[byte]

    @staticmethod
    def color_to_byte(color):
        return Cell._type.index(color)
