import random
import string
import time
from tkinter import *
import tkinter as tk
from tkinter.ttk import *

#----------FUNCTIONS--------------
def lightMode():
    window.configure(bg="#f4f4f4")
    greeting.configure(bg="#f4f4f4")
    pass_length_label.configure(bg="#f4f4f4")
    pass_word.configure(bg="#f4f4f4")
    refresh_button.configure(bg="#f4f4f4")
    frame_for_greeting.configure(bg="#f4f4f4")
    frame_for_pass.configure(bg="#f4f4f4")
    pass_length.configure(bg="#f4f4f4")
    frame_for_length.configure(bg="#f4f4f4")
    refresh_button.configure(image=refresh_image)
    greeting.configure(fg="#686868")
    strength.configure(bg="#f4f4f4")
    frame_for_info.configure(bg="#f4f4f4")
    frame_for_line.configure(bg="#f4f4f4")
    Line.configure(bg="#686868",height=4)
    copy_button.configure(image=copy3,bg="#f4f4f4")

def darkMode():
    window.configure(background="#1c1c1c")
    greeting.configure(bg="#1c1c1c")
    pass_length_label.configure(bg="#1c1c1c")
    pass_word.configure(bg="#1c1c1c")
    refresh_button.configure(bg="#1c1c1c")
    frame_for_greeting.configure(bg="#1c1c1c")
    frame_for_pass.configure(bg="#1c1c1c")
    pass_length.configure(bg="#1c1c1c")
    frame_for_length.configure(bg="#1c1c1c")
    refresh_button.configure(image=refresh_image_2)
    greeting.configure(fg="#e5e5e5")
    strength.configure(bg="#1c1c1c")
    frame_for_info.configure(bg="#1c1c1c")
    frame_for_line.configure(bg="#1c1c1c")
    Line.configure(bg="#e5e5e5",height=0.5)
    copy_button.configure(image=copy_image,bg="#1c1c1c")

def change(x):
    if x =="Dark Mode":
        darkMode()
    else:
        lightMode()

def pass_strength(password):
    colours = ['#FF5412','#FFA500','#20B422']
    if (len(password)<10):
        colour = colours[0]
        strength.configure(image=rf,text=" Weak password",fg=colour)
    elif(len(password)==10):
        colour = colours[1]
        strength.configure(image=yf,text=" Fairly strong password",fg=colour)
    else:
        colour = colours[2]
        strength.configure(image=gf,text=" Strong password",fg=colour)
    pass_word.configure(fg=colour)
    
def generate(string_length):
    string_length = int(string_length)
    random_source = string.ascii_letters + string.digits + string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for i in range(string_length-4):
        password += random.choice(random_source)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    pass_word.configure(text=password)
    pass_strength(password)
    passwordcopy.delete(0,END)
    passwordcopy.insert(0,password)

def copy():
    window.clipboard_clear()
    window.clipboard_append(passwordcopy.get())
    if mode.get()=="Dark Mode":
        copy_button.configure(image=copied_image,bg="#1c1c1c")
        window.after(1500, lambda: copy_button.configure(image=copy_image))
    else:
        copy_button.configure(image=copy4,bg="#f4f4f4")
        window.after(1500, lambda: copy_button.configure(image=copy3))
    

#----------WINDOW DETAILS--------------
window = tk.Tk()
window.title("Atomic")
window.configure(bg="#1c1c1c")
window.state("zoomed")
'''w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))'''

#----------FRAME--------------
frame_for_greeting = tk.Frame(padx=200,pady=10)
frame_for_pass = tk.Frame(padx=325,width=750)
frame_for_length = tk.Frame(padx=10,pady=10)
status = tk.Frame(bg="#00638e",height=25)
frame_for_line = tk.Frame()
frame_for_info = tk.Frame(pady=30,padx=350)

#----------OTHER WIDGETS--------------
var = StringVar(window)
var.set("11")
pass_length = tk.Spinbox(frame_for_length,from_=6,to=72,bd=0,fg="#686868",width=10,command= lambda:generate(pass_length.get()),font=("Consolas",18),justify="right",textvariable=var)
refresh_image_2 = tk.PhotoImage(file="refresh2.png")
refresh_image = tk.PhotoImage(file="refresh.png")
copy_image = tk.PhotoImage(file="copy1.png")
copied_image = tk.PhotoImage(file="copy2.png")
copy3 = tk.PhotoImage(file="copy3.png")
copy4 = tk.PhotoImage(file="copy4.png")
yf = tk.PhotoImage(file="yellow.png")
rf = tk.PhotoImage(file="red.png")
gf = tk.PhotoImage(file="green.png")
combostyle = Style()
combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'blue',
                                       'fieldbackground': '#00638e',
                                       'relief':'flat',
                                       'foreground':'white',
                                       'bd':'0',
                                       'state':'readonly'
                                       }}})
combostyle.theme_use('combostyle') 
mode = Spinbox(status,state='readonly',command=lambda: change(mode.get()))
mode['values']=("Dark Mode","Light Mode")
#mode.current(0)
Line = Canvas(frame_for_line,width=700,height=0.5,bd=0)

#----------MESSAGE & LABELS--------------
greeting = tk.Message(frame_for_greeting,text="Generate cryptographically\nsecure passwords with\nAtomic",font=("Consolas",38,"bold"),bg="#f4f4f4",width=750)

pass_length_label = tk.Label(frame_for_length,text="LENGTH:",fg="#686868",font=("Consolas",15,"bold"))

pass_word = tk.Message(frame_for_pass,width="600",font=("Consolas",40))

strength = tk.Label(frame_for_info,compound='left',font=("Consolas",15))

#----------ENTRY BOX--------------
passwordcopy = Entry()

#----------BUTTONS--------------
generate(11)
refresh_button = tk.Button(frame_for_pass,text="Refresh",command = lambda:generate(pass_length.get()),fg='#686868',bg='#f4f4f4',font=('Consolas',20),relief="flat",image=refresh_image)

copy_button = tk.Button(frame_for_info,text="Copy",command=lambda:copy(),relief="flat",bg="#1c1c1c",highlightbackground="#1c1c1c")


#----------GRIDS AND PACKING--------------
if (mode.get()=="Dark Mode"):
   darkMode()
if (mode.get()=="Light Mode"):
    lightMode()
frame_for_greeting.pack(fill=X)
greeting.pack()
frame_for_pass.pack(fill='x')
pass_word.pack(side="left",anchor="w")
refresh_button.pack(side="right",anchor='e')
frame_for_line.pack()
Line.pack(side="top")
copy_button.pack(side="right")
frame_for_info.pack(fill="x")
strength.pack(anchor="w",side="left")
copy_button.pack()
frame_for_length.pack()
pass_length_label.pack(side="left")
pass_length.pack(side="right")
status.pack(side="bottom",fill=X)
mode.pack(side="right")
window.mainloop()