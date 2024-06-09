from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score=0
        self.score = 0
        self.goto(0,270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score : {self.score}  Highest : {self.high_score}",move=False, align="center",font=("Verdana",15,"normal"))

    def end_game(self):
        self.penup()
        self.goto(0,0)
        self.write(arg=f"Game Over!!!",move=False, align="left",font=("Verdana",15,"normal"))

    def score_inc(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score=self.score
        self.score=0
        self.update_scoreboard()
