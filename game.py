import random

#Zuerst werden alle relevanten Klassen angelegt, um später einzelne Objekte diesbezüglich zu erstellen. 

class room:
    def __init__(self, name, width, length, doorletter):
        self.name = name
        self.width = width
        self.length = length 
        self.doorletter = doorletter


class enemy:
    def __init__(self, name, health, attack, armor, expbonus):
        self.name = name
        self.health = int(health)
        self.attack = int(attack)
        self.armor = int(armor)
        self.expbonus = int(expbonus)


class character:
    def __init__(self, name):
        self.name = name
        self.health = int(10)
        self.exp = int(0) 
        self.attack = int(1)
        self.defense = int(1) 
        self.level = int(1) 
        self.offhand = "bare hand"
        self.defhand = "bare hand"
        self.position = "Entry"
       
        if self.health == 0: 
            print("Game over! You lost.")
            game_counter = 0
        elif self.health > 0: 
            print("You did it! Congratulations")
            game_counter = 0
        
#    def myposition(self):
#       print("You are currently in room " + self.position + ".")

#    def levelup(self):
        if self.exp >= 500:
            self.level += 1
            self.attack += 1
            self.defense += 1
            self.health += 5 
            self.exp = 0


#Nach den Klassen erstellen wir die ersten beiden Objekte: Der Eingangsraum sowie der Endboss, welcher dort erscheinen soll, sobald etwas bestimmtes geschehen ist. 

firstroom = room("Entry", 20, 20, "Entry")
monster = enemy("Lettered Guardian", 50, 4, 5, 1000)


#Wir brauchen zudem noch einige Funktionen, um das Navigieren leicht zu gestalten. 

#Mit game_counter und der ersten While-Schleife wird unsere infinite game-loop gestartet. 
game_counter = 0

while game_counter < 1:
    print("\n \n Welcome to this little text-based adventure game. Do you want to start the game? (start / leave) \n")
    select_input = input()
    if select_input == "leave":
        print("Have a nice day.")
        game_counter += 1
    elif select_input == "start":
        print("\n \nWelcome to the mysterious 'Lettered Dungeon'. Search for all the treasure, mighty weapons and defeat all enemies. For glory, loot and letters!")
        print("What is your characters name? \n")

        charname = input()
        char1 = character(charname)


        print(" \nGreat! Your character goes by the name " + char1.name + ". \n")
        print("I wish you all the luck while you are discovering the mysterious 'Lettered Dungeon'. \n")

        print("You are " + char1.name + ", a courageous pathfinder and hero. Your newest quest leads you to the mysterious 'Lettered Dungeon', where monsters stole all the letters.")
        print("The infamous Dungeon awaits you with a large black entry. Fierceless as you are, you are lighting up a torch and take the first steps into the cave. \n")
        print("You enter the first room. In the left you see another door as well as on the right side. Which do you want to take?")
        print("You can either choose door 'A' or door 'B'.")



        counter_entry = 0

        while counter_entry < 1:
            entry_room = input()
            for x in entry_room:
                if x == "A":
                    print("You open the left door with a big 'A' on it.")
                    char1.position = "A"
                    counter_entry += 1
                elif x == "B":
                    print("You open the right door with a big 'B' on it.")
                    char1.position= "B"
                    counter_entry += 1 
                else: 
                    print("Please choose between 'A' and 'B'.")


        # Die Position-Funktion ist vorhanden, ebenso das die Möglichkeit einen Raum zu wechseln. Es fehlen nun alle Räume 
        # und ihre Verbindungen. 


        if entry_room == "A":
            print("As you open the door you hear a strange noise. And you feel the air coming towards you.")
            print("After a few steps, you face a rotten book zombie. With a grunt he starts to attack you")
            print("Do you want to fight or do you run away in the previous room? Type 'run' or 'fight'.")
            bzombie1 = enemy("Book zombie", 5, 1, 0, 60)
        

            dec_counter = 0
            while dec_counter < 1:
                dec1 = input()
                if dec1 == "fight":
                    while bzombie1.health > 0:
                        char1.health -= bzombie1.attack
                        bzombie1.health -= char1.attack
                    dec_counter += 1
                    print("You won the fight! But you lost some health and have " + str(char1.health) + " Hitpoints left.")
                    char1.exp += bzombie1.expbonus
                    print("For you win over the book zombie you earned " + str(bzombie1.expbonus) + " experience points.")
                    print("You have currently " + str(char1.exp) + " experience points and you are level 1.")
                    print("As you plunder the book zombie you find a rusty sword. Do you want to equip it? ('yes'/'no') \n")

                    equip_counter = 0
                    while equip_counter < 1:
                        equip_answer = input()
                        if equip_answer == "yes":
                            print("\nYou open the cold hands of your enemy and grab the sword. It will help you to fight.")
                            char1.attack += 1
                            char1.offhand = "rusty sword"
                            print("Your Attacks have improved due to the new weapon " + char1.offhand + " to " + str(char1.attack) + " attack points.")
                            equip_counter += 1
                        elif equip_answer == "no":
                            print("\nYou let the rusty sword in the cold hands of the book zombie.")
                            equip_counter += 1
                        else:
                            print("\nPlease answer with 'yes' or 'no'.")
                

                    #Input für Waffenausrüstung 
                elif dec1 == "run": 
                    print("You make haste and run back to the previous room.")
                    char1.position = "Entry"
                    dec_counter += 1
                    counter_entry -= 1

                else:
                    print("Please enter a valid command: 'run' or 'fight'.")
                
                
                    
        elif entry_room == "B":
            print("You open the Door with the big B on it. It squeaks a bit.")
            print("As you enter the room, you find a chest on the left side as well as a desk on the right side with a broken chair.")
            print("On the other side of the wall are two further doors with the letters E and F on them.")



    else: 
        print("Please enter a valid answer. (start / leave)")

#Idee: Räume enthalten Waffen und Rüstungsteile, die der Charakter ausrüsten kann. 
#Die einzelnen Gegenstände können abgelegt werden.
#Diese bleiben dann in den Räumen liegen, in denen sie abgelegt wurden. 

#Wenn der Charakter in einen vorherigen Raum zurückkkehrt, soll wieder die While-Schleife für diesen Raum abgefragt werden. 
#Hier muss ich mich erst mal einlesen und informieren.    
#Erster Gedanke: Räume werden doch über Klasse/Objekte abgedeckt und es gibt eine if-else-Funktion, die jedes mal geprüft wird. 
# 

