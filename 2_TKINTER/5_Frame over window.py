from tkinter import *

window = Tk()

window.title("1st program")
window.geometry("500x500")
window.config(bg="white")

frame1 = Frame(window, bg="gray", width=200, height=200, cursor="dot")
frame2 = Frame(window, bg="black", width=200, height=200, cursor="dotbox")

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)

window.mainloop()
