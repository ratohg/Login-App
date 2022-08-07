from shutil import ExecError
from tkinter import *
from time import sleep

class Animation:
    def __init__(self, root):
        self.canvas = Canvas(root, width=400, height=400, background="#3632a8")
        self.canvas.place(x=-2, y=-2)
        self.text = Label(root, text="Loading", font=("Helvetica 15 bold"), background="#3632a8")
        self.text.place(x=150, y=300)
        self.stop = False
    def ball(self):
        self.ball = self.canvas.create_oval(170, 180, 150, 200, fill="#040940", outline="#040940")
        self.ball1 = self.canvas.create_oval(180, 150, 200, 170, fill="#040940", outline="#040940")
        self.ball2 = self.canvas.create_oval(230, 180, 210, 200, fill="#040940", outline="#040940")
        self.ball3 = self.canvas.create_oval(180, 210, 200, 230, fill="#040940", outline="#040940")
    def animation_ball(self):
        velocity = 3
        velocity_y1 = 3
        velocity1 = -3
        velocity_y2 = -3
        while True:
            if self.stop:
                break
            try:
                sleep(0.001)
                self.canvas.move(self.ball, velocity, 0)
                self.canvas.move(self.ball1, 0, velocity_y1)
                self.canvas.move(self.ball2, velocity1, 0)
                self.canvas.move(self.ball3, 0, velocity_y2)
                coord_x = (self.canvas.coords(self.ball)[0] + self.canvas.coords(self.ball)[1]) / 2
                coord_y_1 = (self.canvas.coords(self.ball1)[2] + self.canvas.coords(self.ball1)[3]) / 2
                coord_x1 = (self.canvas.coords(self.ball2)[0] + self.canvas.coords(self.ball2)[1]) / 2
                coord_y_2 = (self.canvas.coords(self.ball3)[2] + self.canvas.coords(self.ball3)[3]) / 2
                if coord_y_1 >= 230:
                    velocity_y1 = -3
                if coord_y_1 <= 170:
                    velocity_y1 = 3
                if coord_x >= 210:
                    velocity = -3
                if coord_x <= 150:
                    velocity = 3
                if coord_y_2 >= 230:
                    velocity_y2 = -3
                if coord_y_2 <= 170:
                    velocity_y2 = 3
                if coord_x1 >= 210:
                    velocity1 = -3
                if coord_x1 <= 150:
                    velocity1 = 3
            except Exception as error:
                print("Animação parada, ball")
    def animation_text(self):
        while True:
            if self.stop:
                break
            try:
                self.text["text"] = "Loading"
                sleep(1)
                self.text["text"] = "Loading."
                sleep(1)
                self.text["text"] = "Loading.."
                sleep(1)
                self.text["text"] = "Loading..."
                sleep(1)
            except Exception as error:
                print("Animação parada, text")
    def stop_animation(self):
        sleep(5)
        self.canvas.destroy()
        self.text.destroy()
        self.stop = True