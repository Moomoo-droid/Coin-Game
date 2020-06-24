from tkinter import *
import random

root = Tk()

def cmd():
    num = random.randint(1, 3)

    if num == 1:
        lbl.config(text="[Heads]")

def game():
    global lbl, e

    done = 1

    while done:
        e = Entry(root)
        e.pack

        btn = Button(root, command=cmd, text="Submit Bet").pack()

        lbl = Label(root, text="")

mainloop()