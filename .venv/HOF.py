from turtle import  Turtle, Screen
import random

colors=["red","yellow","green","blue","purple","orange"]
all_turtles=[]
race=False
screen=Screen()

screen.setup(500,400)

bet=screen.textinput(title="Bet?", prompt="Turtle?")
if bet:
    race=True


tim=Turtle()

for i in range(len(colors)):
    obj=Turtle()
    obj.speed("fastest")
    obj.color(colors[i])
    obj.shape("turtle")
    obj.penup()
    obj.goto(x=-240,y=-120+(35*i))
    all_turtles.append(obj)

while race:
    for t in all_turtles:
        if t.xcor() > 230:
            race=False
            win_color=t.pencolor()
            if win_color==bet:
                print("You Win!!!")
            else:
                print(f"You Lose!!!, winner is {win_color}")
        random_distance=random.randint(0,10)
        t.forward(random_distance)


screen.exitonclick()
