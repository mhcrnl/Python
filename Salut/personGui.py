"""
Limbaj Programare: Python 2.7.3 / Python 2.7.5
Sistem Operare (OS): Kubuntu 12.10 / Windows 7, Vista
Ropo(depozit cod): https://github.com/mhcrnl/Python
Programator: MihaiC
E-mail: mhcrnl@gmail.com
Data: 02.06.2013    File: personGui.py

"""
from Tkinter import *
from person import *

def savePers():
    #import Person
    content = enume.get() +" "+ eage.get()
    #content1 = eage.get()
    #print content 
    #p1 = Person(get(enume),get(eage))
    listapersoane = []
    listapersoane.append(content)
    for x in listapersoane:
        print x
    filalistapersoane = open("listapersoane.txt", "wb")
    print filalistapersoane.name
    filalistapersoane.write(content)

    filalistapersoane.close()
                             
    
root = Tk()
root.title("Inregistrare Persoane")
root.geometry("250x250")

nume = Label(root, text="Nume")
nume.pack()
enume = Entry(root, bd=12)
enume.pack()

lage = Label(root, text="Varsta", fg="red")
lage.pack()
eage = Entry(root, bd = 4)
eage.pack()

bsave = Button(root, text="Save", command=savePers)
bsave.pack()

root.mainloop()
