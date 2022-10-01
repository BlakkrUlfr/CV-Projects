from tkinter import *

CONSTANT = 1.609344


def calculate():
    result = round(number=float(entry.get()) * CONSTANT, ndigits=3)
    label_output.config(text=f"{result}")


window = Tk()
window.title(string='Miles to Km Converter')
window.config(pady=50, padx=70)

blank_label = Label(text='')
blank_label.grid(column=0, row=0)

entry = Entry(width=10)
entry.get()
entry.grid(column=1, row=0)

label_1 = Label(text='Miles', font=('Arial', 10, 'italic'))
label_1.grid(column=2, row=0)

label_2 = Label(text='is equal to', font=('Arial', 10, 'italic'))
label_2.grid(column=0, row=1)

label_output = Label(text='0', font=('Arial', 10, 'italic'))
label_output.grid(column=1, row=1)

label_4 = Label(text='Miles', font=('Arial', 10, 'italic'))
label_4.grid(column=2, row=1)

button = Button(text='Calculate', font=('Arial', 10, 'italic'), command=calculate)
button.grid(column=1, row=2)

window.mainloop()