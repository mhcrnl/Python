class AgendaTelefonica:
    #variabilele clasei
    nrAbonati = 0
    #constructorul
    def __init__ (self, nume="", prenume="", telefon=""):
        self.nume = nume
        self.prenume = prenume
        self.telefon = telefon
        AgendaTelefonica.nrAbonati +=1

    #methode statice

    #metode de instanta
    def afiseaza(self):
        print "Nume: " + self.nume
        print "Prenume: " + self.prenume
        print "Telefon: " + self.telefon

def main():
    ab1 = AgendaTelefonica("mihai", "cornel", "0722270796")
    ab1.afiseaza()
    ab2 = AgendaTelefonica("mihai", "Irina", "0789567987")
    ab2.afiseaza()
    

if __name__ == '__main__':
    main()
            
    
