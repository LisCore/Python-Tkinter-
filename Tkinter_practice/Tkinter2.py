# tkinter1.py

from tkinter import *

#tkinter._test()

root = Tk()

root.title("My First GUI")

clickBelowLabel = Label(root, text="Click below")
helloButton = Button(root, text="Hello,world")

clickBelowLabel.pack()
helloButton.pack()


root.mainloop()


