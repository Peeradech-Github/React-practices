from tkinter import *

root=Tk()
e = Entry(root,width="50")
e.pack()
e.insert(0,"Enter your name here: ")

def myClick():
    mylabel = Label(root,text=e.get())
    mylabel.pack()

Button = Button(root,text='Please enter your name',command=myClick)
Button.pack()

root.mainloop()
