class Display:
    def display(self):
        pass


def char_to_vector(string: bytes) -> tuple[int, int]:
    match = {
        b"\xe0H": (0, -1),
        b"\xe0P": (0, 1),
        b"\xe0K": (-1, 0),
        b"\xe0M": (1, 0),
    }

    return match[string]


class FieldDraw:

    def __init__(self):
        self.s = """
           SEA  BATTLE           
┌────────────────────────────────┐
│   Ваше поле     Поле врага     │
│   ╔ABCDEFGHIJ╗  ╔ABCDEFGHIJ╗   │
│   0          ║  0          ║   │
│   1          ║  1          ║   │
│   2          ║  2          ║   │
│   3          ║  3          ║   │
│   4          ║  4          ║   │
│   5          ║  5          ║   │
│   6          ║  6          ║   │
│   7          ║  7          ║   │
│   8          ║  8          ║   │
│   9          ║  9          ║   │
│   ╚══════════╝  ╚══════════╝   │
├────────────────────────────────┤
│ Сообщение:                     │
│                                │
└────────────────────────────────┘"""


    def mark_player_empty_shoot(coord_x, coord_y):

