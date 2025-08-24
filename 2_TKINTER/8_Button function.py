from tkinter import *

window = Tk()

window.title("Button function")
window.geometry("500x500")


def login():
    print("Logged in")

button = Button(window, text="Login", command=login, width=12, bg="red", fg="white", font=("bold",12), activebackground="black", activeforeground="white")
button.pack()

window.mainloop()
