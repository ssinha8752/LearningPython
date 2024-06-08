import random
import time
from turtle import Turtle,Screen

from car_manager import CarManager
from player import Player
from scoreboard import  Scoreboard

screen=Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p=Player()
s=Scoreboard()
c = CarManager()

screen.listen()
screen.onkey(p.move_up_turtle,"Up")
screen.onkey(p.move_down_turtle,"Down")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    c.create_cars()
    c.move_car()

    for car in c.all_cars:
        if car.distance(p) < 20:
            game_on=False
            s.end_game()

    if p.ycor() >= p.FINISH_LINE_Y:
        s.score_inc()
        p.next_level()
        c.speed_increase()

screen.exitonclick()