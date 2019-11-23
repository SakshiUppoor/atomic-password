import tkinter as tk

root= tk.Tk()

root.title("wm min/max")

# this removes the maximize button
root.resizable(0,0)
s = tk.Spinbox(values=("Dark","Mode"))

# # if on MS Windows, this might do the trick,
# # but I wouldn't know:
# root.attributes(toolwindow=1)

# # for no window manager decorations at all:
# root.overrideredirect(1)
# # useful for something like a splash screen
s.pack()
root.mainloop()