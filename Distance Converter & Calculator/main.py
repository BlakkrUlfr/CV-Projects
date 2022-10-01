from tkinter import *


def button_clicked():
    label.config(text=an_input.get())


window = Tk()

window.title(string='My First GUI Programme')
window.minsize(width=500, height=300)

window.config(padx=70, pady=70)


# Labels (Label Objects)

label = Label(text='Label', font=('Arial', 14, 'italic'))
label.config(text='New Label', padx=10, pady=10)
label.grid(column=0, row=0)

# Buttons (Button Objects)

button_1 = Button(text='Click Me', command=button_clicked)
button_1.config(padx=15, pady=15)
button_1.grid(column=1, row=1)

button_2 = Button(text='No, Click Me', command=button_clicked)
button_2.config(padx=20, pady=20)
button_2.grid(column=2, row=0)

# Entry (Entry Object)

an_input = Entry(width=10)
an_input.get()
an_input.grid(column=3, row=2)


window.mainloop()
