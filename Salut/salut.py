"""
Limbaj Programare: Python 2.7.3 / Python 2.7.5
Sistem Operare (OS): Kubuntu 12.10 / Windows 7, Vista
Ropo(depozit cod): https://github.com/mhcrnl/Python
Programator: MihaiC
E-mail: mhcrnl@gmail.com
Data: 28.05.2013    File: salut.py

"""
import os
import sys
from Tkinter import *

fereastra = Tk()

def inchide():
    fersec = Toplevel(fereastra)
    bt = Button(fersec, text="Inchide")
    bt.pack()
    #fereastra.quit()
    
def nimic():
    filewin = Toplevel(fereastra)
    button = Button(filewin, text="Nicio operatie!")
    button.pack()

def about():
    var = StringVar()
    w = Message(fereastra, text="Autor: MihaiC./n Data: 28.05.2013", bg="red", relief=RAISED)
    #w.geometry("100x100")
    #var.set("Autor: Mihaic.")
    w.pack()

def quitWindow(root):
    root.destroy()

menubar = Menu(fereastra)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=nimic)
filemenu.add_command(label="Open", command=inchide)
filemenu.add_command(label="Save", command=inchide)
filemenu.add_command(label="Save as...", command=inchide)
filemenu.add_command(label="Close", command=inchide)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=quitWindow)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=inchide)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=inchide)
editmenu.add_command(label="Copy", command=inchide)
editmenu.add_command(label="Paste", command=inchide)
editmenu.add_command(label="Delete", command=inchide)
editmenu.add_command(label="Select All", command=inchide)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=inchide)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

Label(fereastra, text="Nume").grid(row=0)
Label(fereastra, text="Prenume").grid(row=1)

e1 = Entry(fereastra) 
e2 = Entry(fereastra)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
"""
rbt = Radiobutton(fereastra, text="Inchide")
rbt.pack()
"""
fereastra.title("Salut din Python!")
fereastra.geometry("450x450")
fereastra.config(menu=menubar)
fereastra.mainloop()

