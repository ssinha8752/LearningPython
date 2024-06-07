import time

from scoreboard import Scoreboard
from food import Food
from snake import *
from turtle import Turtle,Screen

screen=Screen()
screen.setup(660,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
point=Scoreboard()

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

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        point.score_inc()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        point.end_game()
        game_on=False

    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg)<10:
            game_on=True
            point.end_game()




screen.exitonclick()