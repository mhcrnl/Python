import Tkinter


class App():
   def __init__(self):
       self.root = Tkinter.Tk()
       button = Tkinter.Button(self.root, text = 'root quit', command = self.quit)# I know this way: command = self.root.destroy
       button.pack()
       self.root.mainloop()
   def quit(self):
       self.root.destroy #This way is not work, why? Can you make this function to close 'root' window?
app = App()
