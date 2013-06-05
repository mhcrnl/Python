"""
Limbaj Programare: Python 2.7.3 / Python 2.7.5
Sistem Operare (OS): Kubuntu 12.10 / Windows 7, Vista
Ropo(depozit cod): https://github.com/mhcrnl/Python
Programator: MihaiC
E-mail: mhcrnl@gmail.com
Data: 02.06.2013    File: person.py

"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

lista=[]
p1 = Person("Mihai", 34)
p2 = Person("cornel", 37)
lista.append(p1)
lista.append(p2)
p = lista[0]
print p.get_name()+" "+str(p.get_age())

    
