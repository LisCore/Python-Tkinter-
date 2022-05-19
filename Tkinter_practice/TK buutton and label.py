from tkinter import *

window = Tk()
window.title("Color Game")
window.geometry('700x300')

def clickedBlue():
    lbl.configure(text = "Try again!")
def clickedRed():
    lbl.configure(text = "YAY!")


topLabel = Label(window, text="Pick the RED button", font=("Atrial", 25))
topLabel.grid(column=0, row=0)

btnBlue = Button(window, text="Click me", bg="blue",
                font=("Arial", 25), command=clickedBlue)
btnBlue.grid(column=0, row=1)

btnRed = Button(window, text="Click me", bg="red",
                font=("Arial", 25), command=clickedRed)
btnRed.grid(column=2, row=1)

lbl = Label(window, text="                 ", font=("Arial", 25))
lbl.grid(column=1, row=2)


window.mainloop()
