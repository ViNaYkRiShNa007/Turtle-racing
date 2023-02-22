import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Crossing game")

player = Player()  # creating a player on the screen
cars = CarManager()  # creating car on the screen
scoreboard = Scoreboard()  # creating scoreboard on the screen

screen.onkey(player.move, "Up")  # moving the player forward on press Up arrow key

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_cars()

    for car in cars.CARS:
        # resetting the car's position once it has moved out of frame
        if car.xcor() < -290:
            cars.reset_car(car)

        # detecting turtle collision with car
        if car.distance(player) < 25:
            # checking if player has lives left
            if player.lives == 0:
                game_is_on = False
                scoreboard.game_over()
            else:
                player.lives -= 1
                player.reset()
                scoreboard.update_level(False,player.lives)

        # increasing level, speed of the car and resetting the player
        if player.ycor() >= 280:
            player.reset()
            cars.increase_speed()
            scoreboard.update_level(True,player.lives)

screen.exitonclick()
