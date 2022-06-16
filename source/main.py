from files.wordlist import word
from tkinter import *
from tkinter import ttk
import random
from time import sleep

window = Tk()

while( True):
    random_word = random.choice(word)
    print(random_word)
    sleep(2)
lable = Label(window, text=random_word)
lable.pack()
window.mainloop()
