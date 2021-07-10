
import tkinter.messagebox
from tkinter import *
import random
import time

class Ball:

    def __init__(self, canvas, color):

        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 45, 45, fill=color)
        self.canvas.move(self.id, 245, 100)

        starts = [-3, -2, -1, 1, 2, 3]

        random.shuffle(starts)

        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
        self.points = 0


    def hit_paddle(self, pos):

        paddle_pos = self.canvas.coords(self.paddle.id)

        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:

                return True

        return False


    def draw(self):

        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[1] <= 0:

            self.y = 3

        if pos[3] >= self.canvas_height:

            self.hit_bottom = True

        if self.hit_paddle(pos) == True:

            self.y = -3
            self.points += 1

        if pos[0] <= 0:

            self.x = 3

        if pos[2] >= self.canvas_width:

            self.x = -3


class Paddle:

    def __init__(self, canvas, color):

        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)


    def draw(self):

        self.canvas.move(self.id, self.x, 0)

        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:

            self.x = 0

        elif pos[2] >= self.canvas_width:

            self.x = 0


    def turn_left(self, evt):

        self.x = -2


    def turn_right(self, evt):

        self.x = 2


tk = Tk()

tk.title("Game")

tk.resizable(0, 0)

tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)

canvas.pack()

tk.update()


lable_1 = tkinter.Label(tk, text=f"Points: {0}")

lable_1.config(font=("Arial", 22))

lable_1.pack(side=tkinter.LEFT)


paddle = Paddle(canvas, 'blue')

ball = Ball(canvas, 'red')


while 1:

    if not ball.hit_bottom:

        ball.draw()

        paddle.draw()

        tk.update_idletasks()

    else:

        tkinter.messagebox.showerror('Game Over', f"Game Over\nYour Points = {ball.points}")

        tk.destroy()


    lable_1['text'] = f"Points: {ball.points}"

    lable_1.pack()

    tk.update()

    time.sleep(0.02)
