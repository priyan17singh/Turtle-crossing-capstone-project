import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move_player,key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move_cars()
 
    # Detects if the player has reached to the net level.
    if player.ycor() >280:
        player.refresh_player()
        scoreboard.refresh_score()
        car.reset_car_speed() 
    #  Detecte collision with car
    if car.collision(player):
        scoreboard.game_over()
        game_is_on = False
    
screen.exitonclick()