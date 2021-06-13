from tkinter import Canvas, Button, Radiobutton, IntVar, BooleanVar, Label, CENTER

from battle_ship.cell import Cell_Act
from battle_ship.game import game_statement
from battle_ship.game.logic import get_halo_neigthbours_coords


def init_tk(self):
    self.tk.protocol("WM_DELETE_WINDOW", self.on_closing)
    self.tk.title("Игра Морской Бой")
    self.tk.resizable(0, 0)
    self.tk.wm_attributes("-topmost", 1)
    self.canvas = Canvas(self.tk, width=500 + self.menu_x + 500, height=500 + self.menu_y, bd=0,
                    highlightthickness=0)
    self.canvas.create_rectangle(0, 0, 500, 500, fill="white")
    self.canvas.create_rectangle(500 + self.menu_x, 0, 500 + self.menu_x + 500, 500, fill="lightyellow")
    self.canvas.pack()
    self.tk.update()

    self.draw_table()
    self.draw_table(500 + self.menu_x)

    self.t0 = Label(self.tk, text="Игрок №1", font=("Arial", 10))
    self.t0.place(x=500 // 2 - self.t0.winfo_reqwidth() // 2, y=500 + 3)
    self.t1 = Label(self.tk, text="Игрок №2" + self.add_to_label, font=("Arial", 10,))
    self.t1.place(x=500 + self.menu_x + 500 // 2 - self.t1.winfo_reqwidth() // 2, y=500 + 3)

    self.t0.configure(bg="red")
    self.t0.configure(bg="#f0f0f0")

    self.rb_var = BooleanVar()
    self.rb1 = Radiobutton(self.tk, text="Игра с компьютером", variable=self.rb_var, value=1, command=self.change_rb)
    self.rb2 = Radiobutton(self.tk, text="Игра с другом", variable=self.rb_var, value=0, command=self.change_rb)
    self.rb1.place(x=500 + self.menu_x // 2 - 75, y=50)
    self.rb2.place(x=500 + self.menu_x // 2 - 75, y=70)
    if self.computer_vs_human:
        self.rb1.select()

    self.tip = 1
    self.rb_2 = IntVar()
    self.rb3 = Radiobutton(self.tk, text="Любитель", variable=self.rb_2, value=1, command=self.change_rb2)
    self.rb4 = Radiobutton(self.tk, text="Профессионал", variable=self.rb_2, value=2, command=self.change_rb2)
    self.rb5 = Radiobutton(self.tk, text="Эксперт", variable=self.rb_2, value=3, command=self.change_rb2)
    self.rb3.place(x=500 + self.menu_x // 2 - 75, y=120)
    self.rb4.place(x=500 + self.menu_x // 2 - 75, y=140)
    self.rb5.place(x=500 + self.menu_x // 2 - 75, y=160)
    if self.computer_vs_human:
        self.rb3.select()

    self.b2 = Button(self.tk, text="Начать заново!", command=self.button_begin_again)
    self.b2.place(x=500 + self.menu_x // 2 - self.b2.winfo_reqwidth() // 2, y=10)

    self.b3 = Button(self.tk, text="Сохранить игру", command=self.save_game)
    self.b3.place(x=500 + self.menu_x // 2 - self.b3.winfo_reqwidth() // 2, y=430)
    self.b4 = Button(self.tk, text="Восстановить игру", command=self.load_game)
    self.b4.place(x=500 + self.menu_x // 2 - self.b4.winfo_reqwidth() // 2, y=470)

    self.b5 = Button(self.tk, text="Ручная расстановка", command=self.manual_placement)
    self.b6 = Button(self.tk, text="Авторасстановка", command=self.auto_placement)

    self.t3_1 = Label(self.tk, text="", font=("Arial", 1))
    self.t3_1.place(x=500 + self.menu_x // 2 - self.t3_1.winfo_reqwidth() // 2, y=225)

    self.wrong = Label(self.tk, text="Неправильно! \n Подумайте еще!", font=("Arial", 10,))
    self.right = Label(self.tk, text="Отлично! \n Можно дальше", font=("Arial", 10,))

    self.id1 = self.canvas.create_rectangle(500, 200, 500 + self.menu_x, 300, fill="yellow")
    # canvas_objects.append(id1)

    self.canvas.bind_all("<Button-1>", self.add_to_all)  # ЛКМ
    self.canvas.bind_all("<Button-3>", self.add_to_all)  # ПКМ

def draw_table(self, offset_x=0):
    for i in range(11):
        self.canvas.create_line(offset_x + 50 * i, 0, offset_x + 50 * i, 500)
        self.canvas.create_line(offset_x, 50 * i, offset_x + 500, 50 * i)

def mark_igrok(self, igrok_mark_1):  # подсвечивает чей ход
    if igrok_mark_1:
        self.t0.configure(bg="red")
        self.t0.configure(text="Игрок №1" + self.add_to_label2)
        self.t0.place(x=500 // 2 - self.t0.winfo_reqwidth() // 2, y=500 + 3)
        self.t1.configure(text="Игрок №2" + self.add_to_label)
        self.t1.place(x=500 + self.menu_x + 500 // 2 - self.t1.winfo_reqwidth() // 2, y=500 + 3)
        self.t1.configure(bg="#f0f0f0")
        self.t3_1.configure(text="Ход Игрока №2" + self.add_to_label, font=("Arial", 10,), justify=CENTER, background="yellow")
        self.t3_1.place(x=500 + self.menu_x // 2 - self.t3_1.winfo_reqwidth() // 2, y=220)
    else:
        self.t1.configure(bg="red")
        self.t0.configure(bg="#f0f0f0")
        self.t0.configure(text="Игрок №1")
        self.t0.place(x=500 // 2 - self.t0.winfo_reqwidth() // 2, y=500 + 3)
        self.t1.configure(text="Игрок №2" + self.add_to_label)
        self.t1.place(x=500 + self.menu_x + 500 // 2 - self.t1.winfo_reqwidth() // 2, y=500 + 3)
        self.t3_1.configure(text="Ход Игрока №1", font=("Arial", 10,), justify=CENTER, background="yellow")
        self.t3_1.place(x=500 + self.menu_x // 2 - self.t3_1.winfo_reqwidth() // 2, y=220)

def button_show_enemy(self, field, offset):
    for i in range(10):
        for j in range(10):
            if field.ships[j][i] > 0 and field.clicked[j][i] == 9:
                color = "green"
                _id = self.canvas.create_rectangle(offset + i * 50, j * 50, offset + (i + 1) * 50, (j + 1) * 50, fill=color)
                self.canvas_objects.append(_id)

def draw_point(self, field, x, y, offset_x):
    if field.ships[y][x] == 0:
        self.id1 = self.canvas.create_oval(offset_x + x * 50 + 50 // 3, y * 50 + 50 // 3,
                                 offset_x + x * 50 + 50 - 50 // 3, y * 50 + 50 - 50 // 3, fill="green")
        self.canvas_objects.append(self.id1)
    elif field.ships[y][x] > 0:
        self.id1 = self.canvas.create_line(offset_x + x * 50, y * 50 + 50, offset_x + x * 50 + 50, y * 50, fill="red", width=4)
        self.id2 = self.canvas.create_line(offset_x + x * 50, y * 50, offset_x + x * 50 + 50, y * 50 + 50, fill="red", width=4)
        self.canvas_objects.append(self.id1)
        self.canvas_objects.append(self.id2)

def draw_rectangle(self, x, y, offset_x, color):
    self.id1 = self.canvas.create_rectangle(offset_x + x * 50, y * 50,
                                offset_x + x * 50 + 50, y * 50 + 50, fill=color)
    self.canvas_objects.append(self.id1)

def draw_halo(self, field, x, y, list_prov, offset_x):
    for point in get_halo_neigthbours_coords(x, y):
        if field.clicked[point[1]][point[0]] == 9:
            self.draw_point(field, point[0], point[1], offset_x)
            field.clicked[point[1]][point[0]] = 0
            if point in self.pc_shoot_avaliable:
                self.pc_shoot_avaliable.remove((point[0], point[1]))
    for point in list_prov:
        for point_n in get_halo_neigthbours_coords(point[0], point[1]):
            self.draw_point(field, point_n[0], point_n[1], offset_x)
            field.clicked[point_n[1]][point_n[0]] = 0
            if point_n in self.pc_shoot_avaliable:
                self.pc_shoot_avaliable.remove((point_n[0], point_n[1]))

def add_to_all(self, event):
    mouse_x = self.canvas.winfo_pointerx() - self.canvas.winfo_rootx()
    mouse_y = self.canvas.winfo_pointery() - self.canvas.winfo_rooty()
    x = mouse_x // 50
    y = mouse_y // 50
    if self.game_mode == game_statement.playing_mode:
        # первое игровое поле
        if x < 10 and y < 10 and self.is_field1_current:
            if self.field1.clicked[y][x] == 9:
                self.field1.clicked[y][x] = self.field1.ships[y][x]
                self.draw_point(self.field1, x, y, 0)
                if self.field1.ships[y][x] == 0:
                    self.is_field1_current = False
                if self.is_killed(self.field1, x, y):
                    self.draw_halo(self.field1, x, y, self.list_prov, 0)
                if self.field1.check_winner():
                    self.is_field1_current = True
                    self.end_game("Игрок №2")

        # второе игровое поле
        if 10 + self.delta_menu_x <= x <= 10 + 10 + self.delta_menu_x and y < 10 and not self.is_field1_current:
            if self.field2.clicked[y][x - 10 - self.delta_menu_x] == 9:
                self.field2.clicked[y][x - 10 - self.delta_menu_x] = self.field2.ships[y][x - 10 - self.delta_menu_x]
                self.draw_point(self.field2, x - 10 - self.delta_menu_x, y, 500 + self.menu_x)
                if self.field2.ships[y][x - 10 - self.delta_menu_x] == 0:
                    self.is_field1_current = True

                if self.is_killed(self.field2, x - 10 - self.delta_menu_x, y):
                    self.draw_halo(self.field2, x - 10 - self.delta_menu_x, y, self.list_prov, 500 + self.menu_x)

                if self.field2.check_winner():
                    self.is_field1_current = False
                    self.end_game("Игрок №1")

                elif self.computer_vs_human:
                    self.mark_igrok(self.is_field1_current)
                    if self.is_field1_current:
                        self.move_pc()
        self.mark_igrok(self.is_field1_current)
    else:
        try:
            if self.is_field1_current_:
                if x < 10 and y < 10 and self.field1.activated[y][x] == Cell_Act.non_fixed:
                    self.draw_rectangle(self.field1, x - 10 - self.delta_menu_x, y, 500 + self.menu_x, "green")
                    self.field1.activated[y][x] = Cell_Act.half
                elif self.field1.activated[y][x] == Cell_Act.half:
                    self.draw_rectangle(self.field1, x - 10 - self.delta_menu_x, y, 500 + self.menu_x, "white")
                    self.field1.activated[y][x] = Cell_Act.non_fixed
            else:
                print(y)
                print(x)
                if 10 + self.delta_menu_x <= x <= 10 + 10 + self.delta_menu_x and y < 10 and self.field2.activated[y][x - 10 - self.delta_menu_x] == Cell_Act.non_fixed:
                    self.draw_rectangle(self.field2, x - 10 - self.delta_menu_x, y, 500 + self.menu_x, "green")
                    self.field2.activated[y][x - 10 - self.delta_menu_x] = Cell_Act.half
                elif self.field2.activated[y][x - 10 - self.delta_menu_x] == Cell_Act.half:
                    self.draw_rectangle(self.field2, x - 10 - self.delta_menu_x, y, 500 + self.menu_x, "light yellow")
                    self.field2.activated[y][x - 10 - self.delta_menu_x] = Cell_Act.non_fixed
        except Exception:
            pass


def end_game(self, winner):
    winner = "Победил " + winner
    self.t3_1.place_forget()
    self.button_show_enemy(self.field1, 0)
    self.button_show_enemy(self.field2, 500 + self.menu_x)
    self.field1.clicked = [[10 for _ in range(10)] for _ in range(10)]  # чтобы нельзя было ходить
    self.field2.clicked = [[10 for _ in range(10)] for _ in range(10)]
    self.id2 = self.canvas.create_text(500 + self.menu_x // 2, 255, text=winner, font=("Arial", 10,), justify=CENTER, fill="red")
    self.canvas_objects.append(self.id2)


def draw_loaded(self):
    for i in range(10):
        for j in range(10):
            if self.field1.clicked[j][i] != 9:
                self.draw_point(self.field1, i, j, 0)
            if self.field2.clicked[j][i] != 9:
                self.draw_point(self.field2, i, j, 500 + self.menu_x)