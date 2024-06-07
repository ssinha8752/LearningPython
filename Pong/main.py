import time
from turtle import  Screen,Turtle

from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.tracer(0)

r_paddle=Paddle(350,0)
l_paddle=Paddle(-350,0)
ball=Ball()
score=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.xcor() > 320 and ball.distance(r_paddle)<50 or ball.xcor() < -320 and ball.distance(l_paddle)<50:
        print("CONTACT")
        ball.collision()

    if ball.xcor() > 380:
        ball.reset()
        score.score_inc_x()

    if ball.xcor() < -380:
        ball.reset()
        score.score_inc_y()

screen.exitonclick()