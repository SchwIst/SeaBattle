import random
from msvcrt import getch


def set_user_ships(self):
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
            self._user.field.rotate_last_ship()
            self._should_redraw = True

    self._user.field.bake_ships()


def set_computer_ships(self):
    while len(self._computer.field.possible_ships) > 0:
        self._computer.field.create_ship()

        if random.randint(0, 100) % 2 == 0:
            self._computer.field.rotate_last_ship()

        if not self._computer.field.not_intersect_padding():
            self._computer.field.pop_last_ship()

    self._computer.field.bake_ships()


def play(self):
    while self._start_match:  # TODO: MAKE AN CONDITION TO EXIT|FINISH GAME
        if self._should_redraw:
            self.display()
            self._should_redraw = False

        char = getch()

        action = self._user.react_to_keys(char)

        if isinstance(action, tuple):
            self._user.move_cursor(action)
            self._should_redraw = True
        elif isinstance(action, bool):
            self._user.shoot(self.message_box)


def run(self):
    # self.set_user_ships()
    # self.set_computer_ships()
    # self.save()
    self.restore()
    self.play()
