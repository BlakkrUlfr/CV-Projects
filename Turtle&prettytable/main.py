# import turtle
from turtle import Turtle, Screen

# import prettytable (package)
from prettytable import PrettyTable

# pan = turtle.Turtle()

# Initialise an Object from a Class

pan = Turtle()
print(pan)
pan.shape('turtle')
pan.color('DarkGreen')

pan.forward(100.00)

my_screen = Screen()
print(my_screen.canvwidth)
print(my_screen.canvheight)

my_screen.exitonclick()


table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander", "Bulbasaur"])
table.add_column("Type", ["Electric", "Water", "Fire", "Grass"])

table.align = "l"
print(table.align)

print(table)


