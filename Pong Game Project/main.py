from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600, startx=None, starty=None)
screen.bgcolor('black')
screen.title('Welcome to the PONG!')
screen.exitonclick()
screen.tracer(n=0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = ScoreBoard()

screen.listen()

screen.onkey(key='UP', fun=r_paddle.move_up)
screen.onkey(key='DOWN', fun=r_paddle.move_down)

screen.onkey(key='w', fun=l_paddle.move_up)
screen.onkey(key='s', fun=l_paddle.move_down)

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with Walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect Collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses
    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.r_point()
