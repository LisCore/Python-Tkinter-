#entryBoxGetinput.py

from tkinter import *

window = Tk()
window.title("Entry Box")
window.geometry('400x250')

instructLabel = Label(window, text="Enter your name below")
instructLabel.grid(column=0, row=0)

nameBox = Entry(window, width=35)
nameBox.grid(column=0, row=1)

def clicked():  #concatenate = stick things together
    result = "Welcome to Python GUI, " + nameBox.get() + "!"
    finalLabel.configure(text=result)

btn = Button(window, text="Click me to see message",
             command=clicked)
btn.grid(column=0, row=2)

finalLabel = Label(window, text="")
finalLabel.grid(column=0, row=3)

