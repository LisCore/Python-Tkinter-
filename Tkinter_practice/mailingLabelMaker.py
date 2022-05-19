#mailingLabelMaker.py

from tkinter import *

window = Tk()
window.title("Mailing Label")
window.geometry('450x300')

#topLabel - app title, large and centered
#nameLabel -----------> nameBox
#streetLabel ---------> streetBox -----> createLabelBtn
#cityStLabel ---------> cityStBox
#blank space
#show addressLabel

topLabel = Label(window, text="Mailing Label Maker",
                 font=('Arial Bold', 20))
topLabel.grid(column=0, row=0, columnspan=4)

nameLabel = Label(window, text="Name")
nameLabel.grid(column=1, row=1)
nameBox = Entry(window, width=25)
nameBox.grid(column=2, row=1)

streetLabel = Label(window, text="Street")
streetLabel.grid(column=1, row=2)
streetBox = Entry(window, width=25)
streetBox.grid(column=2, row=2)

cityStLabel = Label(window, text="City & State")
cityStLabel.grid(column=1, row=3)
cityStBox = Entry(window, width=25)
cityStBox.grid(column=2, row=3)

blankLabel = Label(window, text="")
blankLabel.grid(column=2, row=4)

addressLabel = Label(window, text="", justify=LEFT)
addressLabel.grid(column=2, row=5)

def clicked():
    result = nameBox.get() +"\n" + \
             streetBox.get() + "\n" + \
             cityStBox.get()
    addressLabel.configure(text=result, borderwidth=2,
                           relief="sunken", padx=6, pady=6)

createLabelBtn = Button(window, text="Make Address Label",
                        command=clicked)
createLabelBtn.grid(column=4, row=2)



