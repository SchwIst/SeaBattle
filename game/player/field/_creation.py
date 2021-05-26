from game.player.field.cells import TYPES


def _empty(self):
    for i in range(self._height):
        self._cells.append([])
        for j in range(self._width):
            self._cells[i].append(TYPES["empty"])


def fill(self):
    self._empty()
