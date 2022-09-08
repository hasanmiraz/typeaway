from cProfile import label
from turtle import left
from files.wordlist import word
from tkinter import *
from tkinter import ttk
import random

def get_random_word():
    return str(random.choice(word))

def get_20_random_word():
    return random.sample(word, 20)

def loop_word(word_list=[]):
    if len(word_list)==0:
        word_list = get_20_random_word()
    else:
        word_list.append(get_random_word())
    print(len(word_list))
    line = ""
    line = " ".join(word_list)

    print(word_list)
    label.config(text=line)
    window.after(500, loop_word, word_list)

window = Tk()
window.geometry("1000x600")
frame = Frame(window, width=800, height=200, bg="yellow")
frame.pack()
label = Label(frame, wraplength=700)

label.pack(side=LEFT)
loop_word()

window.mainloop()
