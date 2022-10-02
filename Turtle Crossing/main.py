import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

screen.listen()

screen.exitonclick()

player = Player()

screen.onkeypress(fun=player.only_move_up, key='UP')

scoreboard = ScoreBoard()

time_skip = 0
car_manager = CarManager()


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars_left()

    # Detect Collision With Car Objects
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect Successful Crossing
    if player.is_at_finish_line():
        player.gp_to_start()
        car_manager.level_up()
        scoreboard.update_level()

# A turtle moves forwards when you press the "Up" key.

# Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

# When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up.
# On the next level, the car speed increases

# When the turtle collides with a car, it's game over and everything stops.

