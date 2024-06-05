import turtle as t
import random
turtle=t.Turtle()
#timmy.shape("turtle")

#c=["black","blue","orange","green","yellow","red","pink","purple"]
#turtle.width(15)
turtle.speed("fastest")
t.colormode(255)

#count=50
#while count>0:
#    dist = 30
#    if (-300 < turtle.xcor() < 300) and (-300 < turtle.ycor() < 300):
#        turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
#        turtle.right(random.choice([0, 90, 180, 270]))
#        turtle.forward(dist)
#    else:
#        turtle.color(random.choice[c])
#        turtle.right(180)
#        turtle.forward(dist)
#    count-=1

radius=100
total=100
for i in range(1,total):
    turtle.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    turtle.circle(radius)
    turtle.left(360/total)

screen = t.Screen()
screen.exitonclick()