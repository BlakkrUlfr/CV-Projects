# Create a turtle player that starts at the bottom of the screen and listen for the "Up" keypress to move
# the turtle north.

# Detect when the turtle player collides with a car and stop the game if this happens.

from turtle import Turtle

# Use of Constants In Coding

STARTING_POSITION = (0, -280)

MOVE_DISTANCE = 10

FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.color('black')
        self.penup()
        self.gp_to_start()

        self.setheading(to_angle=90)

    def only_move_up(self):
        self.forward(MOVE_DISTANCE)

    def gp_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

