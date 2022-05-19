from tkinter import *

window = Tk()
window.title("Welcome to CS 160!")
window.geometry('800x400')
window.configure(bg="aqua")

lbl = Label(window, text="Hello!", font=("Times New Roman", 50), bg="red", fg="blue")
lbl.grid(column=0, row=0)

lbl2 = Label(window, text="Coding is fun!", bg="yellow", fg="green")
lbl2.grid(column=0, row=1)


btn = Button(window, text="Click me!", font=("Times New Roman", 25), bg="red", fg="green")
btn.grid(column=0, row=5)

window.mainloop()

