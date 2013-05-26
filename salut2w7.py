
import Tkinter  #importam toate modulele Tkinter
class Greeter (Frame):
	def__init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
	
	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.quit
		self.QUIT.pack({"side" : "left"})
		
		self.Hello = Button(self)
		self.Hello["text"] = "Hello"
		self.Hello["command"] = self.say_hello
		self.Hello.pack({"side":"left"})
	
	def say_hello(self):
		greet = Tk()
		greet.geometry("110x75+350+70")
		greeting = Label(greet, text = "Hello, Python!")
		button = Button(greet, text = "Ok", command = greet.quit)
		greeting.pack()
		button.pack()
		greet.mainloop()
		
	def main():
		root = Tk()
		app = Greeter(master=root)
		app.mainloop()
		root.destroy()
		
if__name__=="__main__":
    main()
	
