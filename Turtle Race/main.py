from turtle import Turtle, Screen

pan = Turtle()

screen = Screen()

screen.exitonclick()


def c_h():
    pan.clear()
    pan.penup()
    pan.home()
    pan.pendown()


def p_f():
    pan.forward(30)


def p_b():
    pan.back(30)


def p_l():
    pan.left(30)
# new_heading = pan.heading + 30
# pan.setheading(new_heading)


def p_r():
    pan.right(30)
# new_heading = pan.heading - 30
# pan.setheading(new_heading)


screen.listen()
screen.onkey(fun=p_f, key='w')
screen.onkey(fun=p_b, key='s')
screen.onkey(fun=p_l, key='a')
screen.onkey(fun=p_r, key='d')
screen.onkey(fun=c_h, key='c')



