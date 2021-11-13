from tkinter import *
import string
import random


def generateRandom():
    PassLength = int(input.get())
    if PassLength > 3 and PassLength <= 18:
        ran = ''.join(random.choices(string.ascii_letters + string.digits, k=PassLength))
        label.config(text=ran)
    elif PassLength < 4:
        label.config(text="Please enter minmum lenght 4")
    else:
        label.config(text="Password Length exceeded")






Window = Tk()
Window.title("Password generator")
Window.minsize(width=400,height=150)
Window.config(padx=50,pady=40)

label = Label(text="Length of Password :")
label.config(padx=0,pady=30)
label.grid(column=0,row=0)


input = Entry(width=15)
input.insert(END,"0")
input.grid(column=1,row=0)

button = Button(text="Generate",width=30,command=generateRandom)
button.grid(column=0,row=1,columnspan=2)


label = Label(text="newPassword",width=30)
label.config(pady=30)
label.grid(column=0,row=2,columnspan=2)



Window.mainloop()

