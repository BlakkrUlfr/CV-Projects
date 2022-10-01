from tkinter import *

import pandas as pd

import random as rd

BACKGROUND_COLOR = "#B1DDC6"

random_record = {}

learn_dict = {}

try:

    df = pd.read_csv(filepath_or_buffer='data/words_to_learn.csv')

except FileNotFoundError:

    original_df = pd.read_csv(filepath_or_buffer='data/french_words.csv')
    learn_dict = original_df.to_dict(orient='records')

else:

    learn_dict = df.to_dict(orient='records')


def card_flip():

    canvas.itemconfig(tagOrId=image_bg, image=back_image)

    translation = random_record['English']

    canvas.itemconfig(tagOrId=card_word, text=translation, fill='white')

    canvas.itemconfig(card_title, text='English', fill='white')


def random_word():

    global random_record, flip_timer

    window.after_cancel(id=flip_timer)

    random_record = rd.choice(learn_dict)
    current_word = random_record['French']

    canvas.itemconfig(tagOrId=card_word, text=current_word, fill='black')

    canvas.itemconfig(tagOrId=card_title, text='French', fill='black')

    canvas.itemconfig(tagOrId=image_bg, image=front_image)

    flip_timer = window.after(ms=3000, func=card_flip)


def knew_that():

    learn_dict.remove(random_record)

    new_df = pd.DataFrame(data=learn_dict)

    new_df.to_csv(path_or_buf='data/words_to_learn.csv', index=False)

    random_word()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(ms=3000, func=card_flip)

canvas = Canvas(master=window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

front_image = PhotoImage(file='images/card_front.png')
image_bg = canvas.create_image((403, 267), image=front_image)

back_image = PhotoImage(file='images/card_back.png')

card_title = canvas.create_text((400, 150), font=('Arial', 40, 'italic'), text='')
card_word = canvas.create_text((400, 283), font=('Arial', 40, 'italic'), text='')

check_image = PhotoImage(file='images/right.png')

check_button = Button(image=check_image, borderwidth=0, highlightthickness=0, command=knew_that)
check_button.grid(row=1, column=1)

cross_image = PhotoImage(file='images/wrong.png')

cross_button = Button(image=cross_image, borderwidth=0, highlightthickness=0, command=random_word)
cross_button.grid(row=1, column=0)

random_word()

window.mainloop()


