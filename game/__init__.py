import time
from enum import Enum
from tkinter import Tk

from field import Field


class game_statement(Enum):
    playing_mode = 0
    placement_mode = 1


class Game:
    delta_menu_x = 190 // 50 + 1

    ships_list = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

    def __init__(self):
        self.tk = Tk()
        self.index = 0
        self.app_running = True
        self.stat = 1
        self.menu_x = 50 * Game.delta_menu_x  # 250
        self.menu_y = 40
        self.field1 = Field()
        self.field2 = Field()
        self.canvas_objects = []  # список объектов canvas
        self.list_prov = []
        self.pc_shoot_avaliable = []
        self.current_count_ships = [4, 3, 2, 1]

        self.is_field1_current_ = True
        self.is_field1_current = False  # Истина - то ходит игрок №2, иначе ходит игрок №1
        self.computer_vs_human = True  # Истина - то играем против компьютера
        if self.computer_vs_human:
            self.add_to_label = " (Компьютер)"
            self.add_to_label2 = " (прицеливается)"
            self.is_field1_current = False
        else:
            self.add_to_label = ""
            self.add_to_label2 = ""
            self.is_field1_current = False

        self.list_next = []
        self.x_old = 0
        self.y_old = 0

    from .graphics import init_tk, add_to_all, mark_igrok, button_show_enemy, draw_table, draw_point, draw_halo, \
        draw_loaded, draw_rectangle, end_game
    from .logic import start_play, button_begin_again, check_place, load_game, save_game, \
        get_neigthbours_coords, get_halo_neigthbours_coords, get_points_with_max_weight, random_point, \
        recalculate_weights, change_player, change_rb2, change_rb, change_mode, auto_placement, manual_placement, \
        move_pc, on_closing, is_killed

    def run(self):
        self.init_tk()

        self.game_mode = game_statement.playing_mode

        while self.app_running:
            if self.app_running:
                self.tk.update_idletasks()
                self.tk.update()
            time.sleep(0.016)
