from random import random
import random

from cell import  Cell_Act


class Field:
    def __init__(self):
        self.ships = [[0 for _ in range(11)] for _ in
                      range(11)]  # +1 для доп. линии справа и снизу, для успешных проверок генерации противника
        self.clicked = [[9 for _ in range(10)] for _ in range(10)]
        self.weight = [[9 for _ in range(10)] for _ in range(10)]
        self.activated = [[Cell_Act.non_fixed for _ in range(11)] for _ in range(11)] # new

    def generate_ships(self, pc_shoot_avaliable):
        current_sum = 0
        ships_list = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
        for i in range(0, 10):
            for j in range(0, 10):
                pc_shoot_avaliable.append((i, j))

        while current_sum != 20:
            self.__init__()
            for i in range(10):
                len = ships_list[i]
                horizont_vertikal = random.randrange(1, 3)
                primerno_x = random.randrange(10)
                if primerno_x + len > 10:
                    primerno_x = primerno_x - len
                primerno_y = random.randrange(10)
                if primerno_y + len > 10:
                    primerno_y = primerno_y - len
                if horizont_vertikal == 1:
                    if primerno_x + len <= 10:
                        for j in range(0, len):
                            try:
                                check_near_ships = self.ships[primerno_y][primerno_x - 1] + \
                                                   self.ships[primerno_y][primerno_x + j] + \
                                                   self.ships[primerno_y][primerno_x + j + 1] + \
                                                   self.ships[primerno_y + 1][primerno_x + j + 1] + \
                                                   self.ships[primerno_y - 1][primerno_x + j + 1] + \
                                                   self.ships[primerno_y + 1][primerno_x - 1] + \
                                                   self.ships[primerno_y - 1][primerno_x - 1] + \
                                                   self.ships[primerno_y + 1][primerno_x + j] + \
                                                   self.ships[primerno_y - 1][primerno_x + j]
                                if check_near_ships == 0:
                                    self.ships[primerno_y][primerno_x + j] = len
                            except Exception:
                                pass
                if horizont_vertikal == 2:
                    if primerno_y + len <= 10:
                        for j in range(0, len):
                            try:
                                check_near_ships = self.ships[primerno_y - 1][primerno_x] + \
                                                   self.ships[primerno_y - 1][primerno_x + 1] + \
                                                   self.ships[primerno_y - 1][primerno_x - 1] + \
                                                   self.ships[primerno_y + j][primerno_x] + \
                                                   self.ships[primerno_y + j + 1][primerno_x] + \
                                                   self.ships[primerno_y + j + 1][primerno_x + 1] + \
                                                   self.ships[primerno_y + j + 1][primerno_x - 1] + \
                                                   self.ships[primerno_y + j][primerno_x + 1] + \
                                                   self.ships[primerno_y + j][primerno_x - 1]
                                if check_near_ships == 0:
                                    self.ships[primerno_y + j][primerno_x] = len
                            except Exception:
                                pass
            # делаем подсчет 1ц
            current_sum = 0
            for i in range(10):
                for j in range(10):
                    if self.ships[j][i] <= 0:
                        continue
                    current_sum = current_sum + 1

    def check_ship_fits(self, ship):
        if self.clicked[ship.y][ship.x] != 9:
            return False
        if ship.rotation == 0:
            n = ship.x - ship.size + 1
            if n < 0:
                n = 0
            k = ship.x
            if ship.x + ship.size - 1 > 9:
                k = 10 - ship.size
            for beg in range(n, k + 1):
                kolfree = 0
                for ii in range(beg, beg + ship.size):
                    if self.clicked[ship.y][ii] == 9:
                        kolfree += 1
                if kolfree == ship.size:
                    return True
        else:
            n = ship.y - ship.size + 1
            if n < 0:
                n = 0
            k = ship.y
            if ship.y + ship.size - 1 > 9:
                k = 10 - ship.size
            for beg in range(n, k + 1):
                kolfree = 0
                for jj in range(beg, beg + ship.size):
                    if self.clicked[jj][ship.x] == 9:
                        kolfree += 1
                if kolfree == ship.size:
                    return True
        return False

    def check_winner(self):
        win = True
        for i in range(10):
            for j in range(10):
                if self.ships[j][i] > 0 and self.clicked[j][i] == 9:
                    win = False
        return win
