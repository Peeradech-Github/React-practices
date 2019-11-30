from tkinter import *

root=Tk()
def myClick():
    mylabel = Label(root,text="Test Button!")
    mylabel.pack()

Button = Button(root,text='Click Me!',command=myClick(),fg="red",bg="yellow")
Button.pack()

root.mainloop()
