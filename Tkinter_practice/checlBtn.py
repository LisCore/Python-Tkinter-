#checkBtn.py

from tkinter import *
from tkinter.ttk import *

app = Tk()
app.title("Check Button")
app.geometry('400x400')

pizza = IntVar()
steak = IntVar()
soup = IntVar()
salad = IntVar()

entreeLabel = Label(app, text="Choose your entree(s):")
sideLabel = Label(app, text="Choose your side(s):")
entireOrderLabel = Label(app, text=" ")

pizzaCK = Checkbutton(app, text="Pizza", variable=pizza)
steakCK = Checkbutton(app, text="Steak", variable=steak)
soupCK = Checkbutton(app, text="Soup", variable=soup)
saladCK= Checkbutton(app, text="Salad", variable=salad)

entreeLabel.grid(column=0, row=0)
pizzaCK.grid(column=0, row=1)
steakCK.grid(column=0, row=2)
sideLabel.grid(column=0, row=3)
soupCK.grid(column=0, row=4)
saladCK.grid(column=0, row=5)  

def order():
    wholeOrder = StringVar()
    wholeOrder = "Order\n"
    if pizza.get() ==1:
        wholeOrder = wholeOrder + "pizza\n"
    if steak.get() ==1:
        wholeOrder = wholeOrder + "steak\n"
    if soup.get() ==1:
        wholeOrder = wholeOrder + "soup\n"
    if salad.get() ==1:
        wholeOrder = wholeOrder + "salad\n"

    entireOrderLabel.configure(text=wholeOrder)
    
showOrderBtn = Button(app, text="Show Order", command=order)
showOrderBtn.grid(column=0, row=6)
entireOrderLabel.grid(column=0, row=7)




app.mainloop()
