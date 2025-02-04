from turtle import  Turtle, Screen

tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_counter_clockwise():
    tim.left(10)

def clean():
    tim.clear()
    tim.penup()
    tim.home()



screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="d",fun=move_clockwise)
screen.onkey(key="a",fun=move_counter_clockwise)
screen.onkey(key="c",fun=clean)

screen.exitonclick()
