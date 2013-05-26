from Tkinter import *

class App:

    def __init__(self, master):

         frame = Frame(master)
         frame.pack()
    
     self.lbl = Label(frame, text = "Hello World!\n")
     self.lbl.pack()

         self.button = Button(frame, text="Quit", fg="red", command=frame.quit)
         self.button.pack(side=LEFT)

         self.hi_there = Button(frame, text="Say hi!", command=self.say_hi)
         self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "Hello!"

root = Tk()
root.title("Hai")
root.geometry("200x85")
app = App(root)
root.mainloop()
