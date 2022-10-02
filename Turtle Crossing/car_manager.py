# Create cars that are 20px high by 40px wide that are randomly generated along the y-axis
# and move to the left edge of the screen.
# No cars should be generated in the top and bottom 50px of the screen
# (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs.

# Detect when the turtle player has reached the top edge of the screen (i.e., reached the FINISH_LINE_Y).
# When this happens, return the turtle to the starting position and increase the speed of the cars.
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase the car speed.

from turtle import Turtle

import random

# Use of Constants in Coding

COLOURS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):

        random_chance = random.randint(a=1, b=6)
        if random_chance == 6:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLOURS))
            random_ycor = random.randint(a=-250, b=250)
            new_car.goto(x=300, y=random_ycor)
            self.all_cars.append(new_car)

    def move_cars_left(self):

        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

