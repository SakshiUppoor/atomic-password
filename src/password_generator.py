import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import random
import string

#style = tk.Style()
#style.configure("DarkMode",foreground="White",background="#3A3A3A")

def generate(string_length):
    string_length = int(string_length)
    random_source = string.ascii_letters + string.digits + "!@#$%^&"
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice("!@#$%^&")

    for i in range(string_length-3):
        password += random.choice(random_source)

    password_list = list(password)
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    pass_word.configure(state='normal')
    pass_word.delete(0,'end')
    pass_word.insert(0,password)
    pass_word.configure(state='disabled',font=('Sans Serif',20),width=string_length)
  
#----------WINDOW DETAILS--------------
window = tk.Tk()
window.title("Password Generator")
window.configure(background="#111111")
window.geometry('500x500')


#----------LABELS--------------
pass_length_label = tk.Label(window,text="Password length",font=("Consolas",30),bg="#111111",fg="#fff")

#----------COMBOBOX--------------
pass_length = Combobox(window)
pass_length['values'] = (6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,512,1024,"Text")
pass_length.current(7)

#----------ENTRY BOX-------------- 
pass_word = tk.Entry(window,state='disabled')
generate(pass_length.get())

#----------BUTTONS--------------
refresh_button = tk.Button(window,text="↺",command = lambda:generate(pass_length.get()),fg='#b7f731',bg='#000000',font=('Consolas',20))


#----------GRIDS AND PACKING--------------
pass_length_label.pack()
pass_length.pack()
#generate_button.grid(row=1,column=0)
pass_word.pack()
refresh_button.pack()

window.mainloop()