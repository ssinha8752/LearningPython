import random
import turtle as tim

tim.colormode(255)
t=tim.Turtle()
color_list=[(45, 95, 162), (126, 157, 207), (20, 39, 17), (34, 33, 21), (18, 30, 47), (103, 97, 66), (77, 122, 195), (19, 64, 121), (70, 99, 73), (212, 216, 232), (44, 83, 31), (63, 85, 21), (166, 162, 120), (133, 166, 47), (194, 230, 93), (35, 29, 32), (234, 238, 198), (174, 186, 217), (96, 84, 90), (236, 229, 234), (167, 154, 163), (134, 169, 126), (228, 244, 224), (106, 150, 88), (74, 59, 56), (41, 72, 80), (71, 59, 64), (167, 223, 24), (165, 224, 130), (144, 121, 114)]

t.speed("fastest")

t.penup()
t.setheading(225)
t.forward(350)
t.setheading(0)
t.pendown()

for i in range(1,101):
        t.penup()
        t.dot(20, random.choice(color_list))
        t.forward(50)
        t.pendown()
        if i%10==0:
            t.left(90)
            t.penup()
            t.forward(50)
            t.pendown()
            t.setheading(180)
            t.penup()
            t.forward(500)
            t.pendown()
            t.setheading(0)


t.hideturtle()
screen=tim.Screen()
screen.exitonclick()