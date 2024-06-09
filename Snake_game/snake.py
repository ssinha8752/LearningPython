from turtle import Turtle


starting_pos = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for i in starting_pos:
            self.add_block(i)

    def move(self):
        for i in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(20)


    def add_block(self,position):
        new_block = Turtle("square")
        new_block.color("white")
        new_block.penup()
        new_block.goto(position)
        self.segments.append(new_block)

    def extend_snake(self):
        self.add_block(self.segments[-1].position())

    def up(self):
        if self.segments[0].heading()!=270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)


    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()