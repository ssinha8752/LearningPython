STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

import time
from turtle import Turtle, Screen

class Player(Turtle):
    screen = Screen()
    screen.tracer(0)

    def __init__(self):
        super().__init__()
        self.FINISH_LINE_Y = FINISH_LINE_Y
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_up_turtle(self):
        self.forward(MOVE_DISTANCE)

    def move_down_turtle(self):
        self.backward(MOVE_DISTANCE)

    def next_level(self):
        self.goto(STARTING_POSITION)

    time.sleep(0.1)
    screen.update()

