"""
Limbaj Programare: Python 2.7.3 / Python 2.7.5
Sistem Operare (OS): Kubuntu 12.10 / Windows 7, Vista
Ropo(depozit cod): https://github.com/mhcrnl/Python
Programator: MihaiC
E-mail: mhcrnl@gmail.com
Data: 28.05.2013    File: salut.py

"""
from Tkinter import *

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        menubar = Menu(frame)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=frame.quit)
        filemenu.add_command(label="Open", command=frame.quit)
        filemenu.add_command(label="Save", command=frame.quit)
        filemenu.add_command(label="Save as...", command=frame.quit)
        filemenu.add_command(label="Close", command=frame.quit)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=frame.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=frame.quit)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=frame.quit)
        editmenu.add_command(label="Copy", command=frame.quit)
        editmenu.add_command(label="Paste", command=frame.quit)
        editmenu.add_command(label="Delete", command=frame.quit)
        editmenu.add_command(label="Select All", command=frame.quit)

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=frame.quit)
        helpmenu.add_command(label="About...", command=frame.quit)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "Salut sunt aici!"


root = Tk()
app = App(root)

root.geometry("450x450")
root.mainloop()
root.destroy()
