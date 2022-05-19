#Application for website

from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Create Your Own Account!")
window.geometry('700x700')


headerLabel =  Label(window, text="Create Your Account",
                     font=('Arial Bold', 30))
headerLabel.grid(column=3, row=0, columnspan=10)

blankLabel1 = Label(window, text=" ")
blankLabel1.grid(column=0, row=1)

nameLabel = Label(window, text="Enter Your Name")
nameLabel.grid(column=3, row=2)

firstnameLabel = Label(window, text="First Name:")
firstnameLabel.grid(column=2, row=4)
lastnameLabel = Label(window, text="Last Name:")
lastnameLabel.grid(column=2, row=6)

firstnameBox = Entry(window, width=40)
firstnameBox.grid(column=3, row=4)
lastnameBox = Entry(window, width=40)
lastnameBox.grid(column=3, row=6)

blankLabel2 = Label(window, text=" ")
blankLabel2.grid(column=0, row=7)

dobLabel = Label(window, text="Enter Your DOB")
dobLabel.grid(column=3, row=10)

monthLabel = Label(window, text="Month:")
monthLabel.grid(column=2, row=11)
monthEntry = Entry(window, width=40, justify=LEFT)
monthEntry.grid(column=3, row=11)

dayLabel = Label(window, text="Day:")
dayLabel.grid(column=2, row=12)
dayEntry = Entry(window, width=40)
dayEntry.grid(column=3, row=12)

yearLabel = Label(window, text="Year:")
yearLabel.grid(column=2, row=13)
yearEntry = Entry(window, width=40)
yearEntry.grid(column=3, row=13)

blankLabel3 = Label(window, text=" ")
blankLabel3.grid(column=0, row=14)

genderLabel = Label(window, text="Gender:")
genderLabel.grid(column=2, row=15)
comboValues = ["Male", "Female", "Prefer Not To Say"]
mainCombo = Combobox(window, values=comboValues)
mainCombo.grid(column=3, row=15)

blankLabel4 = Label(window, text=" ")
blankLabel4.grid(column=0, row=16)

ethnicityLabel = Label(window, text="Ethnicity?")
ethnicityLabel.grid(column=2, row=17)
choice = IntVar()
caucasianRb = Radiobutton(window, text="Caucasian", value=1, variable=choice)
aaRb = Radiobutton(window, text="African American", value=2, variable=choice)
asianRb = Radiobutton(window, text="Asian", value=3, variable=choice)
hispanicRb = Radiobutton(window, text="Hispanic", value=4, variable=choice)
caucasianRb.grid(column=2, row=18)
aaRb.grid(column=3, row=18)
asianRb.grid(column=2, row=19)
hispanicRb.grid(column=3, row=19)

blankLabel5 = Label(window, text=" ")
blankLabel5.grid(column=0, row=20)

termsLabel = Label(window, text="By agreeing to the terms and services," "\n" \
                   "you give rights to open your own account." "\n" \
                   "To learn more, please visit us at this website." "\n" \
                   "that is not linked on here.")
termsLabel.grid(column=3, row=21)

blankLabel6 = Label(window, text=" ")
blankLabel6.grid(column=0, row=22)

accept = IntVar()
decline = IntVar()

acceptBox = Checkbutton(window, text="Accept", variable=accept)
acceptBox.grid(column=3, row=24)
declineBox = Checkbutton(window, text="Decline", variable=decline)
declineBox.grid(column=3, row=25)

blankLabel7 = Label(window, text=" ")
blankLabel7.grid(column=0, row=26)


def order():
    if mainCombo.current() ==2:
        resultLabel.configure(text="PREFER NOT TO SAY")
    elif mainCombo.current() ==0:
        resultLabel.configure(text="MALE")
    elif mainCombo.current() ==1:
        resultLabel.configure(text="FEMALE")   

    result = "Hello " + firstnameBox.get() + lastnameBox.get() + "!" "\n" \
            "The birthday you input is " + monthEntry.get() + dayEntry.get() + yearEntry.get() +"!" "\n" \
            "For your gender, you chose " + mainCombo.get() + "." "\n" \

    choice = IntVar()
    if choice.get() ==1:
        choice = "The ethnicity you chose was CAUCASIAN"
    elif choice.get() ==2:
        choice = "The ethnicity you chose was AFRICAN AMERICAN"
    elif choice.get() ==3:
        choice = "The ethnicity you chose was ASIAN"
    elif choice.get() ==4:
        choice = "The ethnicity you chose was HISPANIC"
        
    terms = StringVar()
    if accept.get() ==1:
        terms = "Thank you for joining our community! We hope you have fun!"
    elif decline.get() ==1:
        terms = "Please Accept the Terms of Conditions"
        
    resultLabel.configure(text=result)
    resultLabel2.configure(text=choice)
    resultLabel3.configure(text=terms)

submitBtn = Button(window, text="Submit", command=order)
submitBtn.grid(column=3, row=27)

resultLabel = Label(window, text="")
resultLabel.grid(column=3, row=28)
resultLabel2 = Label(window, text="")
resultLabel2.grid(column=3, row=29)
resultLabel3 = Label(window, text="")
resultLabel3.grid(column=3, row=30)


window.mainloop()
