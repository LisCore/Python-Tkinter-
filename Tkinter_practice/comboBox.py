#comboBox.py

from tkinter import *
from tkinter.ttk import *

#subdirectory
#app = object of Tk 
app = Tk()
app.geometry('400x400')
app.title("Combo Box")

comboValues = ["Duck", "Cow", "Toad"]
mainCombo = Combobox(app, values=comboValues)
mainCombo.grid(column=0, row=0)

secondValue = ["Fly", "Walk", "Jump"]
secondValue = Combobox(app, values=secondValue)
secondValue.grid(column=1, row=0)

def soundBtnClick():
    if mainCombo.current() ==0:
        soundLabel.configure(text="QUACK")
    elif mainCombo.current() ==1:
        soundLabel.configure(text="MOO!")
    elif mainCombo.current() ==2:
        soundLabel.configure(text="RIBBIT!")
        

soundBtn = Button(app, text="What Do I say",
                     command=soundBtnClick)
soundBtn.grid(column=1, row=2)

soundLabel = Label(app, text="")
soundLabel.grid(column=2, row=1)

app.mainloop()

