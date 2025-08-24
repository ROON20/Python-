from tkinter import *

window = Tk()

window.title("Label")
window.geometry("300x300")

lable1 = Label(window, text="mail")
lable2 = Label(window, text="password")


e1 = Entry(window, width=40, borderwidth=5)         # Create entry point
e2 = Entry(window, width=40, borderwidth=5)

lable1.grid(row=0, column=1)
lable2.grid(row=1, column=1)

e1.grid(row=0, column=2)                            # combine thoose point
e2.grid(row=1, column=2)


window.mainloop()
