from tkinter import Tk, Text, Menu
from tkinter import filedialog as fd
from os.path import exists
import os
import re
import tkinter as tk
import subprocess, sys


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

def fileopen():
    filename = fd.askopenfilename()
    opened = open(filename, 'r', encoding="utf-8")
    gui.delete('1.0', 'end')
    gui.insert('1.0', opened.read())

def filesave():
    text = gui.get('1.0', 'end')
    file = fd.asksaveasfilename(
        filetypes=[("*.txt", ".txt")],
        defaultextension=".txt")
    fw = open(file, 'w')
    fw.write(text)
    fw.close()

root = Tk()
root.geometry("850x400")
root.title("TransRender")
root.iconbitmap(r'C:\\Users\\stree\\PycharmProjects\\pythonProject2\\dist\\chili-pepper.ico')
v=tk.Scrollbar(root, orient='vertical')
v.pack(side='right', fill='y')
menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar)
trans_menu = Menu(menubar)
file_menu.add_command(
    label='Open',
    command=fileopen,
)

file_menu.add_command(
    label='Save',
    command=filesave,
)

trans_menu.add_command(
    label='To Spanish',
    command=spanish,
)
trans_menu.add_command(
    label='To English',
    command=english,
)
menubar.add_cascade(
    label="File",
    menu=file_menu,
    underline=0
)
menubar.add_cascade(
    label="Translate",
    menu=trans_menu,
    underline=0
)
gui = Text(root, height=850, width=400, yscrollcommand=v.set)
v.config(command=gui.yview)
gui.pack()
root.mainloop()
if exists('in.txt'):
    os.remove('in.txt')
if exists('out.txt'):
    os.remove('out.txt')
