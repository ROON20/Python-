from tkinter import *
import tkinter.messagebox

window = Tk()

tkinter.messagebox.showinfo("Info", "running out time") # showwarning, showerror
question = tkinter.messagebox.askyesno("Weather", "Will it rain?") #askokcancel

if question == True:
    print("Take an Umbrella")
else:
    print("Okay")

window.mainloop()
