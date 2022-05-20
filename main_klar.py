from random import randrange 
# Här importeras randrange från biblioteket random 
from resources_klar import Pet
# Här importeras klassen Pet från resources_klar.py

def main():
    """ Huvudfunktionen
    """    
    
    """Detta är huvudfunktionen, det är i main som själva spelet körs i och kallar på 
    funktionerna skapade i resources med hjälp av de importerade biblioteken."""
    
    name = input("\nVälkommen till TimaJotchi Programet!\nVad ska ditt husdjur heta?\nSvar: ")
    breed = input("\nVad för djur-ras är ditt husdjur?\nSvar: ")

    pet = Pet(name, breed) 
    # Skapar nytt husdjur

    input("\nHej! Jag heter " + pet.name + "." + "\nKlicka på enter-knappen för att ta mig hem!")
    
    choice = None

    while choice !=0:
        print(
            """
            ***INTERAGERA MED DITT HUSDJUR***

            
            1 - Mata ditt husdjur
            2 - Prata med ditt Husdjur
            3 - Lär ditt husdjur ett nytt ord
            4 - Lek med ditt husdjur
            5 - Kolla husdjurets humör

            0 - Lämna
            """
        )
        choice = input("Svar: ")    

        if choice == "0":
            print("Hejdå!")
            quit()
        elif choice == "1":
            pet.feed()
        elif choice == "2":
            pet.talk()
        elif choice == "3":
            new_word = input("Vilket ord vill du lära dig?  ")
            pet.teach(new_word)
        elif choice == "4":
            pet.play()
        elif choice == "5":
            pet.mood()
        else:
            print("Skrev du fel? Det är inte ett alternativ.")

if __name__ == "__main__":
    main()