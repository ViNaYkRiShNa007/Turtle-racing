from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 260)
        self.level = 1
        self.update_level(False,3)

    def update_level(self,player_reached_top,lives):
        self.clear()
        if player_reached_top:
            self.level += 1
        self.write(f"Level : {self.level} ❤ X {lives}", font=FONT)

    def game_over(self):
        self.goto(-90, 0)
        self.write("GAME OVER !!!", font=FONT)

    pass
