from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=0
        self.hideturtle()
        self.penup()
        self.goto(-270,260)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Level {self.level}", move=False, align="left", font=FONT)
    def score_inc(self):
        self.level +=1
        self.score_update()

    def end_game(self):
        self.goto(0,0)
        self.write(f"Game Over!", move=False, align="center", font=FONT)

