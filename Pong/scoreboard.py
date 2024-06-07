from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_x = 0
        self.score_y=0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.score_x} : {self.score_y}",move=False, align="center",font=("Verdana",15,"normal"))

    def end_game(self):
        self.penup()
        self.goto(0,0)
        self.write(arg=f"Game Over!!!",move=False, align="left",font=("Verdana",15,"normal"))
    def score_inc_x(self):
        self.score_x += 1
        self.update_scoreboard()

    def score_inc_y(self):
        self.score_y += 1
        self.update_scoreboard()
