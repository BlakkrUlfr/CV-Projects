import turtle as t

t.colormode(255)

import random

pan = t.Turtle()
pan.shape('turtle')
pan.color('green')

screen = t.Screen()
screen.exitonclick()

for side in range(4):
    pan.forward(100)
    pan.right(90)

for _ in range(5):
    pan.forward(10)
    pan.penup()
    pan.forward(10)
    pan.pendown()

num_sides = 3
angle = 0

while num_sides <= 10:
    angle = 360/num_sides
    for _ in range(num_sides):
        pan.forward(100)
        pan.right(angle)
    num_sides += 1

colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen"
]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        pan.forward(100)
        pan.right(angle)


for shape_side_n in range(3, 11):
    pan.color(random.choice(colours))
    draw_shape(shape_side_n)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour_tuple = (r, g, b)
    return colour_tuple


pan.pensize(15)
pan.speed(6)

direction = [0, 90, 180, 270]

steps = random.randint(1, 100)
random_direction = random.choice(direction)

for _ in range(steps):
    pan.setheading(random_direction)
    pan.color(random_colour())
    pan.forward(30)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        pan.color(random_colour())
        pan.circle(100)
        pan.setheading(pan.heading() + size_of_gap)
