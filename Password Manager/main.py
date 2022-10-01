from tkinter import *
from tkinter import messagebox

from random import choice, randint, shuffle

import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, string=password)

    pyperclip.lazy_load_stub_copy(text=password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_save():

    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:

        messagebox.showwarning(title='Oops', message="Please don't leave any fields empty.")

    else:

        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered:\nEmail: {email}\n'
                                                              f'Password: {password}\nIs it ok to save?')
        if is_ok:
            with open(file='data.txt', mode='a') as my_data:

                my_data.write(f'{website} | {email} | {password}\n')

            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager')
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)

my_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)

email_username_entry = Entry(width=52)
email_username_entry.insert(0, string='pantelis.kaliviotis@gmail.com')
email_username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text='Add', width=44, command=add_save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
