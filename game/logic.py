import random
import time
from tkinter import Button, CENTER, Label, messagebox

from battle_ship.cell import Cell_Act
from battle_ship.game import game_statement
from battle_ship.ship import Ship


def auto_placement(self):
    self.b5.place_forget()
    self.b6.place_forget()
    self.t3_1.place_forget()
    self.canvas.delete(self.id2)
    self.id2 = self.canvas.create_text(500 + self.menu_x // 2, 225, text="Нажмите Играть", font=("Arial", 10,),
                                       justify=CENTER, fill="red")
    self.field1.generate_ships(self.pc_shoot_avaliable)
    self.field2.generate_ships(self.pc_shoot_avaliable)
    self.play1 = Button(self.tk, text="Играть!", command=lambda: self.start_play(self.play1))
    self.play1.place(x=500 + self.menu_x // 2 - self.play1.winfo_reqwidth() // 2, y=260)


def save_game(self):
    my_file = open("saves.txt", "w+")
    my_file.truncate()
    for field in (self.field1.ships, self.field2.ships, self.field1.clicked, self.field2.clicked):
        for line in field:
            for cell in line:
                my_file.write(str(cell))
            my_file.write(str("\n"))
        my_file.write(str("\n"))
    my_file.write(str(self.computer_vs_human))
    my_file.write("\n")
    my_file.write(str(self.tip))
    my_file.write("\n")
    my_file.write(str(self.is_field1_current))
    my_file.write("\n")
    my_file.write(str())
    for i in range(4):
        my_file.write(str(self.current_count_ships[i]))
    my_file.close()


def load_game(self):
    my_file = open("saves.txt", "r+")
    for el in self.canvas_objects:
        self.canvas.delete(el)
    for field in (self.field1.ships, self.field2.ships, self.field1.clicked, self.field2.clicked):
        for i in range(len(field)):
            for j in range(len(field)):
                field[i][j] = int(my_file.read(1))
            my_file.readline()
        my_file.readline()
    self.r1 = my_file.readline()[0:-1]
    self.computer_vs_human = True if self.r1 == "True" else False
    self.rb_var.set(self.computer_vs_human)
    self.tip = int(my_file.readline()[0:-1])
    self.rb_2.set(self.tip)
    self.is_field1_current = True if my_file.readline()[0:-1] == "True" else False
    self.mark_igrok(self.is_field1_current)
    for i in range(4):
        self.current_count_ships[i] = int(my_file.read(1))
    my_file.close()

    if self.computer_vs_human:
        self.rb1.select()
        self.pc_shoot_avaliable = []
        for i in range(len(field)):
            for j in range(len(field)):
                if self.field1.clicked[j][i] == 9:
                    self.pc_shoot_avaliable.append((i, j))
    else:
        self.rb2.select()

    if self.computer_vs_human:
        self.add_to_label = " (Компьютер)"
        self.add_to_label2 = " (прицеливается)"
    self.mark_igrok(self.is_field1_current)
    self.draw_loaded()


def start_play(self, play):
    play.place_forget()
    self.canvas.delete(self.id2)


def change_player(self):
    self.is_field1_current_ = False
    for i in range(10):
        for j in range(10):
            self.draw_rectangle(self.field1, i - 10 - self.delta_menu_x, j, 500 + self.menu_x, "white")
    self.go_to.place_forget()
    self.end.place_forget()
    self.manual_placement()


def check_place(self, field):
    point_list = []
    fixed_neighbours = 0
    for i in range(10):
        for j in range(10):
            if field.activated[j][i] == Cell_Act.half:
                point_list.append((j, i))
                for k in range(-1, 2):
                    for v in range(-1, 2):
                        if field.activated[k + j][v + i] == Cell_Act.fixed:
                            fixed_neighbours += 1
    if len(point_list) == 0:  # если пользователь не нажал ни на одну клетку - надо обработать отдельно
        self.right.place_forget()
        self.wrong.place(x=500 + self.menu_x // 2 - self.wrong.winfo_reqwidth() // 2, y=150)
    else:
        x = point_list[0][0]
        y = point_list[0][1]
        x_equality = True  # равенство по иксам или оп игрекам
        y_equality = True
        for i in range(1, len(point_list)):
            if x != point_list[i][0]:
                x_equality = False
            if y != point_list[i][1]:
                y_equality = False
        if (x_equality != True and y_equality != True) or len(point_list) != self.ships_list[
            self.index] or fixed_neighbours > 0:
            self.right.place_forget()
            self.wrong.place(x=500 + self.menu_x // 2 - self.wrong.winfo_reqwidth() // 2, y=150)
        else:
            is_right = True
            if x_equality == True:
                y_list = []
                for i in range(len(point_list)):
                    y_list.append(point_list[i][1])
                y_list.sort()
                for i in range(len(point_list) - 1):
                    if y_list[i + 1] - y_list[i] != 1:
                        is_right = False
            else:
                x_list = []
                for i in range(len(point_list)):
                    x_list.append(point_list[i][0])
                x_list.sort()
                for i in range(len(point_list) - 1):
                    if x_list[i + 1] - x_list[i] != 1:
                        is_right = False
            if is_right and self.index < 10:
                if 1 <= self.index + 1 <= 2:
                    self.t3.place(x=500 + self.menu_x // 2 - self.t3.winfo_reqwidth() // 2, y=220)
                elif 3 <= self.index + 1 <= 5:
                    self.t2.place(x=500 + self.menu_x // 2 - self.t2.winfo_reqwidth() // 2, y=220)
                elif 6 <= self.index + 1 <= 9:
                    self.t1.place(x=500 + self.menu_x // 2 - self.t1.winfo_reqwidth() // 2, y=220)

                self.wrong.place_forget()
                self.right.place(x=500 + self.menu_x // 2 - self.right.winfo_reqwidth() // 2, y=150)
                for i in range(10):
                    for j in range(10):
                        if field.activated[j][i] == Cell_Act.half:
                            field.activated[j][i] = Cell_Act.fixed
                            field.ships[j][i] = self.ships_list[self.index]  # "переводим" в ships
                            if self.is_field1_current_:
                                self.draw_rectangle(field, i - 10 - self.delta_menu_x, j, 500 + self.menu_x, "yellow")
                            else:
                                self.draw_rectangle(field, i, j, 500 + self.menu_x, "yellow")

                if self.index == 9 and is_right:  # если кончились корабли
                    self.right.place_forget()
                    self.wrong.place_forget()
                    self.t1.place_forget()
                    self.t2.place_forget()
                    self.t3.place_forget()
                    self.t4.place_forget()
                    self.but.place_forget()
                    self.end.place(x=500 + self.menu_x // 2 - self.wrong.winfo_reqwidth() // 2, y=150)
                    self.index = 0  # обнуляем индекс массива кораблей
                    if self.computer_vs_human == True:
                        self.play.place(x=500 + self.menu_x // 2 - self.play.winfo_reqwidth() // 2, y=260)
                    else:
                        if self.is_field1_current_:
                            self.go_to.place(x=500 + self.menu_x // 2 - self.go_to.winfo_reqwidth() // 2, y=260)
                        else:
                            self.play.place(x=500 + self.menu_x // 2 - self.play.winfo_reqwidth() // 2, y=260)
                else:
                    self.index += 1
            else:
                print(is_right)
                self.right.place_forget()
                self.wrong.place(x=500 + self.menu_x // 2 - self.wrong.winfo_reqwidth() // 2, y=150)


def change_mode(self, play):
    self.game_mode = game_statement.playing_mode
    if self.computer_vs_human:
        for i in range(10):
            for j in range(10):
                self.draw_rectangle(self.field1, i - 10 - self.delta_menu_x, j, 500 + self.menu_x, "white")
        self.field2.generate_ships()
    else:
        for i in range(10):
            for j in range(10):
                self.draw_rectangle(self.field1, i - 10 - self.delta_menu_x, j, 500 + self.menu_x, "white")
        for i in range(10):
            for j in range(10):
                self.draw_rectangle(self.field1, i, j, 500 + self.menu_x, "light yellow")
    play.place_forget()


def manual_placement(self):
    self.b5.place_forget()
    self.b6.place_forget()
    self.t3_1.place_forget()
    self.game_mode = game_statement.placement_mode
    for el in self.canvas_objects:
        self.canvas.delete(el)
    self.canvas_objects = []
    self.rb1.place_forget()  # фича, с помощью которой можно скрывать кнопки
    self.rb2.place_forget()
    self.rb3.place_forget()
    self.rb4.place_forget()
    self.rb5.place_forget()
    self.b5.place_forget()

    self.t4 = Label(self.tk, width=22, text="Расставьте четырехпалубник", font=("Arial", 10,), background="yellow")
    self.t3_1 = Label(self.tk, width=22, text="Расставьте трехпалубник", font=("Arial", 10,), background="yellow")
    self.t2 = Label(self.tk, width=22, text="Расставьте двухпалубник", font=("Arial", 10,), background="yellow")
    self.t1 = Label(self.tk, width=22, text="Расставьте однопалубник", font=("Arial", 10,), background="yellow")

    self.end = Label(self.tk, text="Расстановка \n завершена", font=("Arial", 10,))
    self.go_to = Button(self.tk, text="Перейти к \n следующему игроку",
                        command=lambda: self.change_player(self.go_to, self.end))
    self.play = Button(self.tk, text="Играть!", command=lambda: self.change_mode(self.play))

    self.t4.place(x=500 + self.menu_x // 2 - self.t4.winfo_reqwidth() // 2, y=220)
    if self.is_field1_current_:
        self.but = Button(self.tk, text="Следующий корабль",
                          command=lambda: self.check_place(self, self.field1))
    else:
        self.but = Button(self.tk, text="Следующий корабль",
                          command=lambda: self.check_place(self, self.field2))
    self.but.place(x=500 + self.menu_x // 2 - self.but.winfo_reqwidth() // 2, y=260)


def on_closing(self):
    if messagebox.askokcancel("Выход из игры", "Хотите выйти из игры?"):
        self.app_running = False
        self.tk.destroy()


def change_rb(self):
    if self.rb_var.get():
        self.computer_vs_human = True
        self.add_to_label = " (Компьютер)"
        self.add_to_label2 = " (прицеливается)"
    else:
        self.computer_vs_human = False
        self.add_to_label = ""
        self.add_to_label2 = ""
    self.mark_igrok(self.is_field1_current)


def change_rb2(self):
    self.tip = self.rb_2.get()


def button_begin_again(self):
    self.id2 = self.canvas.create_text(500 + self.menu_x // 2, 225, text="Выберите расстановку", font=("Arial", 10,),
                                       justify=CENTER,
                                       fill="red")
    self.b5.place(x=500 + self.menu_x // 2 - self.b5.winfo_reqwidth() // 2, y=390)
    self.b6.place(x=500 + self.menu_x // 2 - self.b6.winfo_reqwidth() // 2, y=350)
    self.right.place_forget()
    self.wrong.place_forget()
    self.t3_1.place_forget()
    for el in self.canvas_objects:
        self.canvas.delete(el)
    self.canvas_objects = []
    self.current_count_ships = [4, 3, 2, 1]
    for i in range(0, 10):
        for j in range(0, 10):
            self.pc_shoot_avaliable.append((i, j))
            self.field1.clicked[j][i] = 9
            self.field1.weight[j][i] = 9
            self.field2.clicked[j][i] = 9
            self.field2.weight[j][i] = 9

    for i in range(0, 11):
        for j in range(0, 11):
            self.field1.ships[j][i] = 0
            self.field2.ships[j][i] = 0
            self.field1.activated[j][i] = Cell_Act.non_fixed
            self.field2.activated[j][i] = Cell_Act.non_fixed

    self.rb1.place(x=500 + self.menu_x // 2 - 75, y=50)
    self.rb2.place(x=500 + self.menu_x // 2 - 75, y=70)
    self.rb3.place(x=500 + self.menu_x // 2 - 75, y=120)
    self.rb4.place(x=500 + self.menu_x // 2 - 75, y=140)
    self.rb5.place(x=500 + self.menu_x // 2 - 75, y=160)


def recalculate_weights(self, available_ships):
    if self.tip == 2 or random.randrange(0, 4) != 0:
        self.field1.weight = [[1 for _ in range(10)] for _ in range(10)]
    else:
        for i in range(10):
            for j in range(10):
                if self.field1.clicked[j][i] == 9 and self.field1.ships[j][i] in range(1, 5):
                    self.field1.weight[j][i] = 1 + self.field1.ships[j][i]
                else:
                    self.field1.weight[j][i] = 1

    for ship_size in range(0, 4):
        if available_ships[ship_size] > 0:
            for _ in (1, available_ships[ship_size]):
                ship = Ship(ship_size + 1, 1, 1, 0)
                for x in range(10):
                    for y in range(10):
                        if self.field1.clicked[y][x] in range(0, 5):
                            if self.field1.weight[y][x] == 0:
                                self.field1.weight[y][x] = 0
                                continue
                        for rotation in range(2):
                            ship.set_position(x, y, rotation)
                            if self.field1.check_ship_fits(ship):
                                self.field1.weight[y][x] += 1


def get_points_with_max_weight(self):
    weights = {}
    max_weight = 0
    for x in range(10):
        for y in range(10):
            if self.field1.weight[y][x] > max_weight:
                max_weight = self.field1.weight[y][x]
            weights.setdefault(self.field1.weight[y][x], []).append((x, y))
    return weights[max_weight]


def random_point(self):
    if self.tip == 1:
        if len(self.pc_shoot_avaliable) > 0:
            return random.choice(self.pc_shoot_avaliable)
        else:
            for i in range(10):
                for j in range(10):
                    if self.field1.clicked[j][i] == 9:
                        return (i, j)
    if self.tip >= 2:
        if self.current_count_ships[1] == self.current_count_ships[2] == self.current_count_ships[3] == 0:
            list_point = self.pc_shoot_avaliable
        else:
            self.recalculate_weights(self.current_count_ships)
            list_point = self.get_points_with_max_weight()
        for i in range(5):
            point = random.choice(list_point)
            if ((point[0] + point[1]) % 2) != 0:
                return point
        if len(list_point) > 0:
            return random.choice(list_point)
        else:
            for i in range(10):
                for j in range(10):
                    if self.field1.clicked[j][i] == 9:
                        return (i, j)


def move_pc(self):
    self.tk.update()
    time.sleep(1)
    x = 0
    y = 0
    while self.is_field1_current:
        if self.stat == 1:
            while True:
                [x, y] = self.random_point()
                if self.field1.clicked[y][x] == 9:
                    if 1 <= self.field1.ships[y][x] <= 4:
                        self.x_old = x
                        self.y_old = y
                        self.list_next.clear()
                        for point in get_neigthbours_coords(x, y):
                            if self.field1.clicked[point[1]][point[0]] == 9:
                                self.list_next.append([point[0], point[1]])
                    break

        elif self.stat == 2:
            while len(self.list_next) > 0:
                point = random.choice(self.list_next)
                if self.field1.clicked[point[1]][point[0]] == 9:
                    if 1 <= self.field1.ships[point[1]][point[0]] <= 4:
                        x_old = x
                        y_old = y
                        x = point[0]
                        y = point[1]
                        self.list_next.remove(point)

                        list = self.list_next.copy()
                        for point in list:
                            if not (x_old == x == point[0]) and not (y_old == y == point[1]):
                                self.list_next.remove(point)

                        for point in get_neigthbours_coords(x, y):
                            if self.field1.clicked[point[1]][point[0]] == 9 and \
                                    (x_old == x == point[0] or y_old == y == point[1]):
                                self.list_next.append([point[0], point[1]])
                    break
            else:
                while True:
                    [x, y] = self.random_point()
                    if self.field1.clicked[y][x] == 9:
                        break

        elif self.stat >= 3:
            while len(self.list_next) > 0:
                point = random.choice(self.list_next)
                if self.field1.clicked[point[1]][point[0]] == 9:
                    x = point[0]
                    y = point[1]
                    self.list_next.remove(point)
                    if 1 <= self.field1.ships[y][x] <= 4:
                        for point in get_neigthbours_coords(x, y):
                            if self.field1.clicked[point[1]][point[0]] == 9 and \
                                    (self.x_old == x == point[0] or self.y_old == y == point[1]):
                                self.list_next.append([point[0], point[1]])
                    break
            else:
                while True:
                    [x, y] = self.random_point()
                    if self.field1.clicked[y][x] == 9:
                        break

        self.field1.clicked[y][x] = self.field1.ships[y][x]
        if (x, y) in self.pc_shoot_avaliable:
            self.pc_shoot_avaliable.remove((x, y))
        self.draw_point(self.field1, x, y, 0)
        if self.field1.ships[y][x] == 0:
            self.is_field1_current = False
        else:
            self.stat = self.stat + 1

            if self.is_killed(self.field1, x, y):
                self.draw_halo(self.field1, x, y, self.list_prov, 0)
                self.list_next.clear()
                self.x_old = 0
                self.y_old = 0
                self.stat = 1

            if self.field1.check_winner():
                self.is_field1_current = False
                self.end_game("Игрок №2" + self.add_to_label)


def get_neigthbours_coords(x, y):
    list = []
    if x + 1 < 10:
        list.append((x + 1, y))
    if x - 1 >= 0:
        list.append((x - 1, y))
    if y + 1 < 10:
        list.append((x, y + 1))
    if y - 1 >= 0:
        list.append((x, y - 1))
    return list


def get_halo_neigthbours_coords(x, y):
    list = []
    for i in range(x - 1, x + 2):
        if i in range(0, 10):
            for j in range(y - 1, y + 2):
                if j in range(0, 10):
                    list.append((i, j))
    return list


def is_killed(self, field, x, y):
    self.list_prov.clear()
    if field.ships[y][x] == 0:
        return False
    if field.ships[y][x] == 1:
        self.current_count_ships[0] -= 1
        return True
    elif field.ships[y][x] >= 2:
        self.list_prov.append([x, y])
        for point in get_neigthbours_coords(x, y):
            if field.ships[point[1]][point[0]] == field.ships[y][x]:
                if field.clicked[point[1]][point[0]] == 9:
                    return False
                else:
                    self.list_prov.append([point[0], point[1]])
                    if field.ships[y][x] == 2:
                        self.current_count_ships[1] -= 1
                        return True

        for i in range(0, field.ships[y][x] - 2):
            list = self.list_prov.copy()
            for point_n in list:
                for point in get_neigthbours_coords(point_n[0], point_n[1]):
                    if field.ships[point[1]][point[0]] == field.ships[y][x]:
                        if field.clicked[point[1]][point[0]] == 9:
                            return False
                        elif field.clicked[point[1]][point[0]] == field.ships[y][x] and (
                                point[1] != y or point[0] != x):
                            self.list_prov.append([point[0], point[1]])
                            x = point[0]
                            y = point[1]
        self.current_count_ships[field.ships[y][x] - 1] -= 1
        return True
    else:
        return False
