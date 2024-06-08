import random, time
from turtle import Turtle,Screen

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

screen=Screen()
screen.tracer(0)

class CarManager(Turtle):

    def __init__(self):
        self.all_cars=[]
        self.dist = STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_chance = random.randint(1,3)
        if random_chance==1:
            new_car = Turtle()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(270, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_car(self):
        super().__init__()
        for car in self.all_cars:
            car.backward(self.dist)

    def speed_increase(self,):
        self.dist += MOVE_INCREMENT

