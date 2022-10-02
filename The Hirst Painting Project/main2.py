import colorgram

import random

import turtle as t

# colour_objects = colorgram.extract('C:/Users/Admin/PycharmProjects/The_Hirst_Painting_project/image.jpg', 84)

# rgb_colours_tuples = []

# for colour_object in colour_objects:
#     rgb_colours_tuples.append(colour_object.rgb)

# for colour_object in colour_objects:
#     Colour_rgb = colour_object.rgb
#     rgb_colours_tuples.append(Colour_rgb)

# for colour_object in colour_objects:
#     r = colour_object.rgb.r
#     g = colour_object.rgb.g
#     b = colour_object.rgb.b
#     new_colour = (r, g, b)
#     rgb_colours_tuples.append(new_colour)

# print(rgb_colours_tuples)

t.colormode(255)

pan = t.Turtle()

screen = t.Screen()
screen.exitonclick()

rgb_colours_tuples = [
 (245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136),
 (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35),
 (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
 (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
 (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)
]

pan.speed('fastest')
pan.penup()
pan.hideturtle()
pan.setheading(225)
pan.forward(300)
pan.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    pan.dot(20, random.choice(rgb_colours_tuples))
    pan.forward(50)

    if dot_count % 10 == 0:
        pan.setheading(90)
        pan.forward(50)
        pan.setheading(180)
        pan.forward(500)
        pan.setheading(0)
