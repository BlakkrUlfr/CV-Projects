# Create a scoreboard that keeps track of which level the user is on.
# Every time the turtle player does a successful crossing, the level should increase.
# When the turtle hits a car, GAME OVER should be displayed in the centre.

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()

        self.level = 0
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=-260)
        self.update_scoreboard()

    def update_scoreboard(self):

        self.clear()

        self.write(arg=f'Level : {self.level}', align='left', font=FONT)

    def update_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg='GAME OVER', align='center', font=FONT)

