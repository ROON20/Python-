from tkinter import *

window = Tk()

window.title("2nd program")
window.geometry("500x500")
window.config(bg="white")


frame1 = Frame(window, bg="gray", width=200, height=200, cursor="dot")
frame1.pack_propagate(False)                # Prevant to sink


frame2 = Frame(window, bg="black", width=200, height=200, cursor="dotbox")


button1 = Button(frame1, text="Button", bg="red", width=5, height=2)

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)

button1.pack(side=TOP, pady=10)

window.mainloop()
