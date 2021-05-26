import random


def set_user_ships(self):
    from msvcrt import getch

    while not self._start_match:
        if self._should_redraw:
            self.display()
            self._should_redraw = False

        char = getch()

        action = self._user.react_to_keys(char)

        if isinstance(action, bool):
            if self._user.field.not_intersect_padding():
                self._start_match = self._user.field.create_ship()
                self._should_redraw = True
        elif isinstance(action, tuple):
            self._user.field.move_last_ship(action)
            self._should_redraw = True
        else:
            self._user.field.rotate_last_ship(action)
            self._should_redraw = True


def set_computer_ships(self):
    while len(self._computer.field.possible_ships) > 0:
        self._computer.field.create_ship()

        if random.randint(0, 100) % 2 == 0:
            self._computer.field.rotate_last_ship(lambda x: x.rotate())

        if not self._computer.field.not_intersect_padding():
            self._computer.field.pop_last_ship()


def play(self):
    pass


def run(self):
    self.set_user_ships()
    self.set_computer_ships()
    self.play()
