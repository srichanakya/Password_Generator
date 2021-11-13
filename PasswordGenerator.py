from tkinter import *
import string
import random


def generateRandom():
    ran = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    label.config(text=ran)


Window = Tk()
Window.title("Password generator")
Window.minsize(width=350,height=150)
Window.config(padx=50,pady=40)


button = Button(text="Generate",width=30,command=generateRandom)
button.grid(column=0,row=0)


label = Label(text="newPassword",width=30)
label.config(pady=30)
label.grid(column=0,row=1)



Window.mainloop()

