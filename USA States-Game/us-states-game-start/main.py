import turtle

import pandas

screen = turtle.Screen()

screen.title('U.S. States Game')

image = 'blank_states_img.gif'
screen.addshape(image)

screen.mainloop()

turtle.shape(image)


# def get_mouse_click_coor(x, y):
#     print(x, y)

# screen.onscreenclick(fun=get_mouse_click_coor)

usa_df = pandas.read_csv('50_states.csv')

states_list = usa_df.state.to_list()

guessed_states_list = []

while len(guessed_states_list) < 50:

    answer_state = screen.textinput(title=f'{len(guessed_states_list)}/50 States Correct',
                                    prompt="Whats another State's Name?").title()
    if answer_state == 'Exit':

        missing_states = [state for state in states_list if state not in guessed_states_list]
        new_usa_df = pandas.DataFrame(missing_states)
        new_usa_df.to_csv('states_to_learn.csv')
        break

    if answer_state in states_list:

        guessed_states_list.append(answer_state)

        location_turtle = turtle.Turtle()
        location_turtle.hideturtle()
        location_turtle.penup()

        state_row = usa_df[usa_df.state == answer_state]

        location_turtle.goto(x=int(state_row.x), y=int(state_row.y))
        location_turtle.write(arg=state_row.state.item())
