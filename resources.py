from random import randrange

"""
Klassen för husdjuret, denna klass innehåller statistik för när djuret kräver olika saker, olika funktioner samt kopplar djurets vokabulär till den externa vocab.txt filen
"""
class Pet(object):
    happiness_reduce = 2
    happiness_maximum = 10
    happiness_warning = 3
    hunger_reduce = 2
    hunger_maximum = 10
    hunger_warning = 3
    vocabulary = open('vocab.txt').readlines()

    """
    Denna funktion definierar de olika 
    """
    def __init__(self, Name, Breed):
        self.Name = Name
        self.Breed = Breed
        self.hunger = randrange(self.hunger_maximum)
        self.happiness = randrange(self.happiness_maximum)
        self.vocabulary = self.vocabulary[:]

    """
    Denna funktion är det som drar ner på hunger och humöret när varje rundar passerar, precis som att tiden passerar. 
    """
    def __clock_tick(self):
        self.hunger -= 1
        self.happiness -= 1

    """Detta returnerar en introduktion med """
    def __str__(self):
        return "\nHej! Jag heter" + self.Name + "." + "\nJag är" + self.happiness() + "."

    def teach(self, word):
        self.vocabulary.append(word)
        self.__clock_tick()

    def talk(self):
        print("Jag heter", self.Name, " och är en ", self.Breed, ".", "Just nu är jag ungefär", self.happiness,"/10 glad och ", self.hunger,"/10 hungrig")
        print(self.vocabulary[randrange(len(self.vocabulary))])
        self.__clock_tick()
    
    def feed(self):
        print("""
        ***Knaster***
        Gott, tack!
        """)
        måltid = randrange(self.hunger, self.hunger_maximum)
        self.hunger += måltid
    
        if self.hunger < 0:
            self.hunger = 0
            print("Jag är fortfarande hungrig, ge mig mer mat!")
        elif self.hunger > self.hunger_maximum:
            self.hunger = self.hunger_maximum
            print("Jag är mätt nu :)")
        self.__clock_tick()
    
    def play(self):
        print("Wohoo!")
        fun = randrange(self.happiness, self.happiness_maximum)
        self.happiness += fun
        self.__clock_tick
