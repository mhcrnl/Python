import pygtk
pygtk.require('2.0')
import gtk

class Whc:
def __init__(self):
self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
self.window.connect("destroy", self.destroy)
self.window.set_title("Hello World!")
self.window.set_default_size(200,100);

self.label = gtk.Label("Hello World!")
self.window.add(self.label)
self.label.show()
self.window.show()

def destroy(self, widget, data=None):
gtk.main_quit()

def main(self):
gtk.main()

if __name__ == "__main__":
base = Whc()
base.main()
