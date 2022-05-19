#radioBtn.py

from tkinter import *
from tkinter.ttk import *

app = Tk()
app.geometry('400x400')
app.title("Radio Button")

genreLabel = Label(app, text="What kind of book do you like to read?")
genreLabel.grid(column=0, row=0)

choice = IntVar()
scifiRb = Radiobutton(app, text="Science Fiction", value=1, variable=choice)
fantasyRb = Radiobutton(app, text="Fantasy", value=2, variable=choice)
nonfiRb = Radiobutton(app, text="Non-Fiction", value=3, variable=choice)

scifiRb.grid(column=0, row=1)
fantasyRb.grid(column=0, row=2)
nonfiRb.grid(column=0, row=3)


def choiceClick():
    if choice.get() ==1:
        recommendLabel.configure(text="Have you read Issav Asimov?")
    elif choice.get() ==2:
        recommendLabel.configure(text="Have you read J.R. Tolkien?")
    elif choice.get() ==3:
        recommendLabel.configure(text="Have you read Loren Eiseley?")

choiceBtn = Button(app,text="Click Here",
                   command=choiceClick)
choiceBtn.grid(column=1, row=2)
recommendLabel = Label(app, text="")
recommendLabel.grid(column=1, row=4)
                   


app.mainloop()
