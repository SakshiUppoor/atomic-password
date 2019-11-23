#HELLO WORLD
'''
from tkinter import *

root = Tk()

label1 = Label(root, text ="Hello World")

label1.pack()

root.mainloop()
'''

#USING FRAMES
'''
from tkinter import *

root = Tk()

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="Click Here", fg="Red")

button2 = Button(otherframe, text="Click Here", fg="Blue")

button1.pack()
button2.pack()

root.mainloop()
'''

#GRID LAYOUT
'''
from tkinter import *

root = Tk()

label1 = Label(root,text="Firstname")
label2 = Label(root,text="Lastname")

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row=0,column=0)
label2.grid(row=1,column=0)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

root.mainloop()
'''

#SELF ADJUSTING WIDGETS
'''
from tkinter import *

root = Tk()

label1 = Label(root, text="First",bg="Red",fg="white")


label2 = Label(root, text="First",bg="Blue",fg="white")
label2.pack(fill=Y,side=RIGHT)
label1.pack(fill=X,side=BOTTOM)
root.mainloop()
'''

#HANDLING BUTTON CLICKS
'''
from tkinter import *

root = Tk()

def dosomething():
    print("You clicked the button!")

button1 = Button(root,text = "Click Here", command = dosomething)
button1.pack()
root.mainloop()
'''

#USING CLASSES
'''
from tkinter import *

class MyButtons:

    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame,text="Click here",command = self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame,text="Exit",command=frame.quit)
        self.quitbutton.pack(side=BOTTOM)

    def printmessage(self):
        print("Button Clicked")


root = Tk()
b = MyButtons(root)
root.mainloop()
'''

#DROP DOWNS
'''
from tkinter import *

def function1():
    print("Menu Clicked")

root = Tk()

mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="File",menu=submenu)

submenu.add_command(label="Project",command=function1)
submenu.add_command(label="Save",command=function1)

submenu.add_separator()
submenu.add_command(label="Exit",command=function1)

newmenu = Menu(mymenu)

mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="Undo",command=function1)

root.mainloop()
'''

#PRACTICE &  TOOLBAR & STATUS BAR

'''
from tkinter import *

def dosomething():
    print("Menu Clicked")

root = Tk()

mymenu = Menu(root)

root.config(menu = mymenu)

filemenu = Menu(mymenu)

mymenu.add_cascade(label = "File",menu = filemenu)

filemenu.add_command(label = "New File",command = dosomething)
filemenu.add_command(label = "New Window",command = dosomething)
filemenu.add_separator()
filemenu.add_command(label = "Open File...",command = dosomething)
filemenu.add_command(label = "Open Window...",command = dosomething)
filemenu.add_command(label = "Open Workspace...",command = dosomething)
recent = Menu(filemenu)
filemenu.add_cascade(label="Open Recent",menu=recent)
recent.add_command(label="Reopen closed editor",command=dosomething)

editmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit" , menu=editmenu)
editmenu.add_command(label = "Undo",command = dosomething)
editmenu.add_command(label = "Redo",command = dosomething)
editmenu.add_separator()
editmenu.add_command(label = "Cut",command = dosomething)
editmenu.add_command(label = "Copy",command = dosomething)
editmenu.add_command(label = "Paste",command = dosomething)
editmenu.add_separator()
editmenu.add_command(label = "Find",command = dosomething)
editmenu.add_command(label = "Replace",command = dosomething)

toolbar = Frame(root, bg="Black")
insertbutton = Button(toolbar,text="Insert File",command = dosomething)
insertbutton.pack(side=LEFT,padx=2,pady=3)

printbutton = Button(toolbar,text="Print",command=dosomething)
printbutton.pack(side=LEFT,padx=7,pady=8)
toolbar.pack(side=TOP,fill=X)

status = Label(root,text="This is the status",relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM,fill=X)
root.mainloop()
'''

#MESSAGE BOX
'''
from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Title","This is awesome")

response = tkinter.messagebox.askquestion("Question","Do you like coffee?")

if response:
    print("Here is some coffee")

root.mainloop()
'''

#DRAWING

from tkinter import *

root = Tk()

canvas = Canvas(root,width=200,height=100)
canvas.pack()

newline = canvas.create_line(0,0,50,100)
otherline  = canvas.create_line(10,10,100,200,fill="green")

root.mainloop()