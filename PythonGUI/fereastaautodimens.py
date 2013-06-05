
from Tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(sticky=N+S+E+W)
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.quit = Button(self, text="Quit", activebackground="red",
                           cursor="heart", command=self.quit)
        self.quit.grid(row=0, column=0, sticky=N+S+E+W)

app = Application()
app.master.title("Fereastra cu auto dimensionare")
app.master.geometry("270x270")
app.mainloop()
