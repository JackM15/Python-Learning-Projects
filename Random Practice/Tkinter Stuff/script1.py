#first import tkinter (built in to python), import all!!
from tkinter import *

#tkinter made up of 2 things, windows and widgets
#first create a window (empty)
window = Tk()

#----------------------------------------------------------------------------

#Functions
def km_to_miles():
    miles = float(entry1_value.get()) * 1.6
    text1.insert(END,miles)

#-----------------------------------------------------------------------------
#create widget variables

#button first, first parameter = window its bound to, second = text to label button, command is what function to execute (without brackets!)
b1 = Button(window,text="Execute",command=km_to_miles)
#next pack/grid the button so it appears on the window and tell it where to appear.
b1.grid(row=0,column=0)

#more widgets!
#entry is an entry area, bind it to the window.
entry1_value=StringVar()
entry1 = Entry(window,textvariable=entry1_value)
entry1.grid(row=0,column=1)

#text entry, bind to window, height in cells and width in cells
text1=Text(window, height=1,width=20)
text1.grid(row=0,column=2)

#-----------------------------------------------------------------------------

#this will open the window and should always be at the end of the code
window.mainloop()
