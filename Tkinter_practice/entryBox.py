#entryBox.py

from tkinter import *

window = Tk()
window.title("Entry Box")
window.geometry('400x250')

instructLabel = Label(window, text="Enter your name below")
instructLabel.grid(column=0, row=0)

nameBox = Entry(window, width=15)
nameBox.grid(column=0, row=1)

