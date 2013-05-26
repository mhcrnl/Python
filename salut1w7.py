import Tkinter
 
class App:
   def __init__(self, master):
      button = Tkinter.Button(master, text="I'm a Button.")
      button.pack()
 
if __name__ == '__main__':
   root = Tkinter.Tk()
   root.title("SalutPythonRomania!")
   root.geometry("280x285")
   app = App(root)
   root.mainloop()
