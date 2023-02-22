import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
STARTING_LIMIT = -250
ENDING_LIMIT = 280
RIGHT = 180


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.CARS = []
        self.create_cars()
        self.penup()
        self.hideturtle()

    def create_cars(self):
        for i in range(20):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(random.randint(STARTING_LIMIT, ENDING_LIMIT), random.randint(STARTING_LIMIT, ENDING_LIMIT))
            new_car.setheading(RIGHT)
            self.CARS.append(new_car)

    def move_cars(self):
        for cars in self.CARS:
            cars.forward(self.move_speed)

    def reset_car(self,car):
        car.goto(290, random.randint(STARTING_LIMIT, ENDING_LIMIT))

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT


    pass
