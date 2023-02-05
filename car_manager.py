import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "purple", "blue", "pink"]
START_X = 400
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.n = 6

    def create_car(self):
        create = random.randint(1, self.n)
        if create == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(400, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    # speed of the cars increase everytime the turtle returns to the start position
    def level_up(self):
        self.car_speed += 5
        if self.n >= 0:
            self.n = self.n - 1
