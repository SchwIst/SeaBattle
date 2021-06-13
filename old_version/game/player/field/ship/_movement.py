from old_version.game.utils import FILE_TEMPLATE


def move(self, offset_x: int, offset_y: int):
    if self.x + offset_x not in range(
            FILE_TEMPLATE["fields"][0]["size"][0] - ((self.size - 1) if self._is_horizontal else 0)
    ) or self.y + offset_y not in range(
        FILE_TEMPLATE["fields"][0]["size"][1] - (0 if self._is_horizontal else (self.size - 1))
    ):
        return

    self.x += offset_x
    self.y += offset_y


def rotate(self):
    if self.x > FILE_TEMPLATE["fields"][0]["size"][0] - self.size or \
            self.y > FILE_TEMPLATE["fields"][0]["size"][1] - self.size:
        return

    self._is_horizontal = not self._is_horizontal
