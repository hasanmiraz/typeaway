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

#adding words
# def loop_word(word_list=[]):
#     if len(word_list)==0:
#         word_list = get_20_random_word()
#     else:
#         word_list.append(get_random_word())
#     print(len(word_list))
#     line = ""
#     line = " ".join(word_list)

#     print(word_list)
#     label.config(text=line)
    # window.after(500, loop_word, word_list)

def string_coloring():
    pass

def key_pressed(event):
    w=Label(window,text="Key Pressed:"+event.char)
    w.place(x= 500, y= 400)



window = Tk()
window.geometry("1000x600")

line_list = get_20_random_word()
letter_list = list(line_list[0])
line_list.pop(0)
print(letter_list)
line_string = " ".join(line_list)
label = Label(window, text= line_string, wraplength= 700)
label.pack(side= TOP)

#adding words
# loop_word()

#key press event
window.bind("<Key>",key_pressed)

window.mainloop()
