from turtle import Turtle, Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import Cars

screen =  Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0) 

player = Player()
car_manager = Cars()
scoreboard = Scoreboard()

game_is_on = True


screen.listen()
screen.onkeypress(player.move, "Up")

while game_is_on:
    screen.update() 
    time.sleep(0.1)
    car_manager.create_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish():
        player.restart()
        scoreboard.add_point()
        car_manager.level_up()

screen.exitonclick()

