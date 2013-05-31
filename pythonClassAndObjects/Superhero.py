 
class Superhero:
    #class variabile
    __superhero_count = 0
    #constructor
    def __init__(self, name = "", hungry = False, tired = False):
        #instance variables
        self.__name = name
        self.__hungry = hungry
        self.__tired = tired
        Superhero.__superhero_count +=1
        
    #static methods
    @staticmethod
    def get_superhero_count():
        return Superhero.__superhero_count
    
    #instance methods
    def mowGrass(self):
        print (self.__name + " is mowing the grass.")
        self.__tired = True
        self.__hungry = True

    def nap(self):
        print (self.__name + " is taking a nap.")
        self.__tired = False
               
def main():
    sup1 = Superhero("Cornel", True, False)
    print sup1
    sup1.mowGrass()
    sup1.nap()

if __name__ == '__main__':
    main()
