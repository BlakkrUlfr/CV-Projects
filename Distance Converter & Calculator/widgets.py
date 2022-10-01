from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is old text")
label['text'] = 'This is new text'
label.config(text="This is new text")
label.pack()


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

# Entries
entry = Entry(width=30)

# Add some text to begin with
entry.insert(END, string="Some text to begin with.")

# Gets text in entry
print(entry.get())
entry.pack()

# Textbox
textbox = Text(height=5, width=30)

# Puts Cursor In Textbox.
textbox.focus()

# Adds some text to begin with.
textbox.insert(END, "Example of multi-line text entry.")

# Gets current value in textbox at line 1, character 0
print(textbox.get("1.0", END))
textbox.pack()


# Spinbox
def spinbox_used():
    # Gets the Current Value In Spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called With Current Scale Value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():

    # Prints 1 if On Checkbutton is Checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked_state, 0 is Off, 1 is On.
checked_state = IntVar()

checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# variable to hold on to which Radiobutton value is Checked.
radio_state = IntVar()

radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)

radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()


def button_clicked():
    print("I got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
print(user_input.get())
user_input.grid(column=3, row=2)


window.mainloop()

