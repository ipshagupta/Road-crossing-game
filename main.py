import time
from turtle import Screen
from player import Player
from turtle import Turtle
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
screen.listen()
screen.onkeypress(player.player_move, "Up")
car = CarManager()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    # detecting collision between cars and the player
    for cars in car.all_cars:
        if cars.distance(player) < 15:
            game_is_on = False
            score.game_over()

    # detecting if player has reached the finish line
    if player.check_finishline():
        player.goto_start()
        car.level_up()
        score.level_up()

screen.exitonclick()
