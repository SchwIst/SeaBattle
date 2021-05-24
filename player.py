from abc import abstractmethod

from cells import CellTypes
from field import Field
from utils import Display, move_print


class Shooter:
    @abstractmethod
    def shoot(self, field: Field):
        pass


class Player(Shooter, Display):
    chosen_position_x: int
    chosen_position_y: int

    def print(self):
        move_print(str(CellTypes["selected"]), self.chosen_position_x, self.chosen_position_y)

    def shoot(self, field: Field):
        pass
