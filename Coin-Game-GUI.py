from tkinter import *
import random

root = Tk()
root.geometry("400x400")

def cmd(event):
    num = random.randint(1, 3)
    e.delete(0, END)

    if num == 1 and e.get().lower() == "heads":
        lbl.config(text="[Heads] You betted right")
    
    if num == 1 and e.get().lower() != "heads":
        lbl.config(text="[Heads] You betted wrong")

    if num == 2 and e.get().lower() == "tails":
        lbl.config(text="[Tails] You betted right")
    
    if num == 2 and e.get().lower() != "tails":
        lbl.config(text="[Tails] You betted wrong")

def game():
    global lbl, e

    done = 1
    
    e = Entry(root)
    e.pack()
    e.bind("<Return>", cmd)

#    btn = Button(root, command=cmd, text="Submit Bet").pack()

    lbl = Label(root, text"Put bet in box (heads/tails)")

    lbl = Label(root, text="")
    lbl.pack()

    done -= 1

game()

mainloop()