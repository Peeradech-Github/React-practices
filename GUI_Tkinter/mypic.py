import os
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image

root = Tk()
root.title('Test showing an image')
root.iconbitmap("Iconsmind-Outline-Communication-Tower.ico")



img1 = ImageTk.PhotoImage(Image.open("wp1979971.jpg"))
img2 = ImageTk.PhotoImage(Image.open("wp2531370.jpg"))
img3 = ImageTk.PhotoImage(Image.open("wp2531399.jpg"))

img_lists = [img1,img2,img3]

myLabel = Label(image=img1)
# myLabel.pack()
myLabel.grid(row=0,column=0,columnspan=3)


def forward(image_number):
    global myLabel
    global button_backward
    global button_forward

    myLabel.grid_forget()
    myLabel =Label(image=img_lists[image_number-1])
  
    button_forward =Button(root, text=">",command=lambda: forward(image_number+1))
    button_backward =Button(root,text ="<",command=lambda:backward(image_number-1))

    button_backward.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)
    myLabel.grid(row=0,column=0,columnspan=3)
def backward(image_number):
    global myLabel
    global button_backward
    global button_forward
    

button_backward = Button(root, text="<",command=lambda:backward())
button_forward = Button(root, text= ">",command=lambda:forward(2))
button_quit = Button(root, text="Leave Page", command=root.quit)

button_backward.grid(row=1,column=0)
button_forward.grid(row=1,column=2)
button_quit.grid(row=1,column=1)







root.mainloop()