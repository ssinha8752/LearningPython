import time

from snake import *
from turtle import Turtle,Screen

screen=Screen()
screen.setup(660,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()




screen.exitonclick()