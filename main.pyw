#!/usr/bin/env python3

from tkinter import Tk, Text, Menu
import os
import re

def spanish():
    saved = gui.get('1.0', 'end')
    printed = open('in.txt', 'w', encoding="utf-8")
    printed.write(saved)
    printed.close()
    file = open('in.txt', 'r', encoding="utf-8")
    out = open('out.txt', 'w', encoding="utf-8")
    for text in file:
        dict = open('spanish.txt', 'r', encoding="utf-8")
        for new in dict:
            x = new.split(':')
            x[1] = x[1].strip()
            if x[0] in text:
                text = re.sub(r'\b' + x[0] + r'\b', x[1], text)
        dict.close()
        out.write(text)
    out.close()
    file.close()
    writeto = open('out.txt', 'r', encoding="utf-8")
    gui.delete('1.0', 'end')
    gui.insert('1.0', writeto.read())

def english():
    saved = gui.get('1.0', 'end')
    printed = open('in.txt', 'w', encoding="utf-8")
    printed.write(saved)
    printed.close()
    file = open('in.txt', 'r', encoding="utf-8")
    out = open('out.txt', 'w', encoding="utf-8")
    for text in file:
        dict = open('english.txt', 'r', encoding="utf-8")
        for new in dict:
            x = new.split(':')
            x[1] = x[1].strip()
            if x[0] in text:
                text = re.sub(r'\b' + x[0] + r'\b', x[1], text)
        dict.close()
        out.write(text)
    out.close()
    file.close()
    writeto = open('out.txt', 'r', encoding="utf-8")
    gui.delete('1.0', 'end')
    gui.insert('1.0', writeto.read())

root = Tk()
root.geometry("850x400")
root.title("TransRender")
menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar)
file_menu.add_command(
    label='To Spanish',
    command=spanish,
)
file_menu.add_command(
    label='To English',
    command=english,
)
menubar.add_cascade(
    label="Translate",
    menu=file_menu,
    underline=0
)
gui = Text(root, height=850, width=400)
gui.pack()

root.mainloop()
os.remove('in.txt')
os.remove('out.txt')
