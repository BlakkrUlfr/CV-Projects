from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0

timer = ''

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():

    window.after_cancel(id=timer)

    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    counter_label.config(text='')

    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():

    global reps

    reps += 1

    work_sec = WORK_MIN * 60

    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        timer_label.config(text='Short Break', fg=PINK)
        count_down(short_break)
    elif reps % 8 == 0:
        timer_label.config(text='Long Break', fg=RED)
        count_down(long_break)
    else:
        timer_label.config(text='Work', fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds == 0:
        count_seconds = '00'
    elif count_seconds < 10:
        count_seconds = f'0{count_seconds}'

    canvas.itemconfig(timer_text, text=f'{count_minutes}:{count_seconds}')

    if count > 0:

        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()

        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔'
        counter_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title(string='Pomodoro')
window.config(padx=75, pady=50, bg=YELLOW)

blank_label = Label(text='')
blank_label.grid(column=0, row=0)

timer_label = Label(text='Timer', font=(FONT_NAME, 33, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

counter_label = Label(text='', bg=YELLOW, fg=GREEN)
counter_label.grid(column=1, row=3)

canvas = Canvas(width=205, height=230, bg=YELLOW, highlightthickness=0)

photo_image = PhotoImage(file='tomato.png')

canvas.create_image(102.5, 115, image=photo_image)

timer_text = canvas.create_text(102.5, 130, text='00:00', fill='white', font=(FONT_NAME, 30, 'bold'))

canvas.grid(column=1, row=1)


window.mainloop()
