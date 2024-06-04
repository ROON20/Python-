import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    length = int(length_entry.get())
    char_types = [letters_var.get(), numbers_var.get(), symbols_var.get()]
    chars = ""
    if char_types[0]:
        chars += string.ascii_letters
    if char_types[1]:
        chars += string.digits
    if char_types[2]:
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "No character types selected. Please select at least one type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_var.set(password)

def copy_to_clipboard():
    pyperclip.copy(result_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

letters_var = tk.BooleanVar()
tk.Checkbutton(root, text="Letters", variable=letters_var).grid(row=1, column=0, sticky='w', padx=10)

numbers_var = tk.BooleanVar()
tk.Checkbutton(root, text="Numbers", variable=numbers_var).grid(row=2, column=0, sticky='w', padx=10)

symbols_var = tk.BooleanVar()
tk.Checkbutton(root, text="Symbols", variable=symbols_var).grid(row=3, column=0, sticky='w', padx=10)

tk.Button(root, text="Generate", command=generate_password).grid(row=4, column=0, columnspan=2, pady=10)
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Helvetica", 14))
result_label.grid(row=5, column=0, columnspan=2, pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
