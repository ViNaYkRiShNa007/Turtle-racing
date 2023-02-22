from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.reset()
        self.lives = 3

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.clear()
        self.goto(STARTING_POSITION)
        self.setheading(UP)
    pass
