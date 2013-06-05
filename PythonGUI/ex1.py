#!/usr/local/bin/python
from Tkinter import *

class Application(Frame):               #mostenirea clasei Frame din Tkinter
    def __init__(self, master=None):
        Frame.__init__(self, master)    #Apelarea constructorului clasei parinte
        self.grid()                     #face sa apara fereastra
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.grid()
        
#if __name__ == "__main__"
app = Application()
app.master.title("Sample application")
app.master.geometry("300x300")
app.mainloop()


#print "eu sunt Python"
#print 100+400

