from Tkinter import *

# create a root window
root = Tk()
root.title("Salut Romania Python!")
root.geometry("280x185")
# create a frame in the window to hold other widgets
app = Frame(root)
app.grid()

lbl = Label(app, text = "Hello World!")
lbl.grid()

bttn1 = Button(app, text = "Die")
bttn1.grid()

root.mainloop()