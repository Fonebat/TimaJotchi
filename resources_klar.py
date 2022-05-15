from random import randrange

"""
Klassen för husdjuret, denna klass innehåller statistik för när djuret kräver olika saker, olika funktioner samt kopplar djurets vokabulär till den externa vocab.txt filen
"""
class Pet(object):
    happiness_reduce = 2
    happiness_maximum = 10
    happiness_warning = 3
    happiness_bottom = 0
    hunger_reduce = 2
    hunger_maximum = 10
    hunger_warning = 3
    hunger_bottom = 0
    vocabulary = open('vocab.txt').readlines()

    """
    Denna funktion bestämmer de olika basvärdena man får när man startar programmet, hungern och humöret randomiseras medan Namnet och djurrasen har spelaren bestämt innan.
    """
    def __init__(self, Name, Breed):
        self.Name = Name
        self.Breed = Breed
        self.hunger = randrange(self.hunger_maximum)
        self.happiness = randrange(self.happiness_maximum)
        self.vocabulary = self.vocabulary[:] #Ord som djuret lär sig under spelets gång lagras här, och kan använda dessa ord tillsammans med orden i vocab.txt

    """
    Denna funktion är det som drar ner på hunger och humöret när varje rundar passerar, precis som att tiden passerar. 
    Funktionen ser också till att hunger och humöret inte går under 0.
    """
    def __clock_tick(self):
        self.hunger -= 1
        self.happiness -= 1
        if self.hunger < self.hunger_bottom:
            self.hunger = 0
        if self.happiness < self.happiness_bottom:
            self.happiness = 0

    """
    Funktionen lägger till ett ord i listan vocabulary, eftersom det är append som lägger till ordet i slutet av listan. Detta innebär att man kan lära djuret oändligt många nya ord
    (eller tills det inte finns plats kvar). Funktionen passerar därefter tiden ett steg.
    """
    def teach(self, word):
        self.vocabulary.append(word)
        self.__clock_tick()

    """
    Denna funktion kallas när man vill prata med sitt husdjur, funktionen ger tillbaka ett värde för humöret och hungern.
    """
    def talk(self):
        print("Jag heter", self.Name, " och är en ", self.Breed, ".", "Just nu är jag ungefär", self.happiness,"/10 glad och ", self.hunger,"/10 hungrig")
        print(self.vocabulary[randrange(len(self.vocabulary))])
        self.__clock_tick()
    
    """
    Funktionen kallas när man matar sitt husdjur, först printar den ut en fras som visar för användaren att djuret äter, därefter kommer värdet för hungern att öka.
    Men hunger-värdet ökar bara om nivån är under 10, vilket är maximala värdet.
    """
    def feed(self):
        print("""
        ***Knaster***
        Gott, tack!
        """)
        if self.hunger < self.hunger_maximum:
            meal = randrange(self.hunger, self.hunger_maximum)
            self.hunger += meal
        self.__clock_tick()
        if self.hunger > self.hunger_maximum:
            self.hunger = 10
    
    """
    Funktionen kallas när man leker med sitt husdjur, funktionen printar ut en fras för att visa att användaren leker med sitt husdjur och ökar därefter en randomiserad mängd humör-poäng.
    Humör-värdet ökar bara om nivån är under 10, vilket är maximala värdet. Precis som funktionen över.
    """
    def play(self):
        print("Wohoo!")
        if self.happiness < self.happiness_maximum:
            fun = randrange(self.happiness, self.happiness_maximum)
            self.happiness += fun
        self.__clock_tick()
        if self.happiness > self.happiness_maximum:
            self.happiness = 10

    """
    Denna funktion ger ett resultat om man använder alternativ 5, dvs att funktionen förklarar djurets humör genom att välja en av tre alternativ beroende på humör-värdet.
    """
    def mood(self):
        if self.happiness == self.happiness_maximum:
            print ("Jag är Glad!")
        elif self.happiness < self.happiness_warning:
            print ("Jag är uttråkad.")
        else:
            print ("Jag har inget att klaga på")
        self.__clock_tick()