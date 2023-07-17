import random

#Zuerst werden alle relevanten Klassen angelegt, um später einzelne Objekte diesbezüglich zu erstellen. 

class room:
    def __init__(self, name, items, monster, dl1, dl2, pre_dl):
        self.name = name
        self.monster = monster
        self.items = items
        self.dl1 = dl1
        self.dl2 = dl2
        self.pre_dl = pre_dl


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
        self.defense = int(0) 
        self.level = int(1) 
        self.offhand = "bare hand"
        self.defhand = "bare hand"
        self.position = Entry
        
        if self.exp >= 500:
            self.level += 1
            self.attack += 1
            self.defense += 1
            self.health += 5 
            self.exp = 0


#Nun werden die relevanten Objekte erstellt. Zuerst kommen alle Räume, danach der Endboss, welcher in Raum Entry erscheinen soll, nachdem der Spieler
#in Raum Z angekommen ist. Am Ende wird dann auch der Charakter selbst als Objekt erstellt. 

Entry = room("Entry", "none", "none", "A", "B", "none")
A = room("A", "none", "book zombie", "C", "D", "Entry")
B = room("B", "red potion", "none", "E", "F", "Entry")
C = room("C", "none", "none", "G", "H", "A")
D = room("D", "none", "none", "I", "J", "A")
E = room("E", "none", "none", "K", "L", "B")
F = room("F", "none", "none", "M", "N", "B")
G = room("G", "none", "none", "O", "none", "C")
H = room("H", "none", "none", "O", "none", "C")
I = room("I", "none", "none", "P", "none", "D")
J = room("J", "none", "none", "P", "none", "D")
K = room("K", "none", "none", "Q", "none", "E")
L = room("L", "none", "none", "Q", "none", "E")
M = room("M", "none", "none", "R", "none", "F")
N = room("N", "none", "none", "R", "none", "F")
O = room("O", "none", "none", "G", "H", "S")
P = room("P", "none", "none", "I", "J", "T")
Q = room("Q", "none", "none", "K", "L", "U")
R = room("R", "none", "none", "M", "N", "V")
S = room("S", "none", "none", "O", "W", "none")
T = room("T", "none", "none", "P", "W", "none")
U = room("U", "none", "none", "Q", "X", "none")
V = room("V", "none", "none", "R", "X", "none")
W = room("W", "none", "none", "S", "T", "Y")
X = room("X", "none", "none", "V", "U", "Y")
Y = room("Y", "none", "none", "X", "W", "Z")
Z = room("Z", "none", "dark mage", "none", "none", Y)


monster = enemy("Lettered Guardian", 50, 4, 5, 1000)
char1 = character("none")


#Nachfolgend kommen wichtige Prüf-Funktionen, wenn Räume betreten werden. 
#Die Check-Funktion für items ist allgemeingültig und soweit fertig. Muss später noch implementiert werden. 
#Die Check-Funktion für Gegner muss noch allgemeingültig werden.  
#check_enemy dient der Überprüfung, ob es im aktuellen Raum Monster gibt. 
def check_enemy(user_answer):
    if user_answer == "C":
        char1.position = C
        if C.monster == "none":
            print("There is no enemy in the room.")
        elif C.monster != "none":
            print("As you enter the room, you are attacked by a " + C.monster + ".")
    elif user_answer == "B":
        char1.position = B
        if B.monster == "none":
            print("There is no enemy in the room.")
        elif B.monster != "none":
            print("As you enter the room, you are attacked by a " + B.monster + ".")
            print("You fight the enemy until it is dead. ")
            B.monster = "none"

#check_items dient der Überprüfung, ob es im aktuellen Raum Items gibt, bzw. ob diese herumliegen. 
def check_items(item_input):
    if item_input == "check items":
        if char1.position.items == "none":
            print("There are no items on the floor.")
        elif char1.position.items != "none":
            print("As you observe the room for some loot, you find a " + char1.position.items + ".")
            print("Do you want to take it? (Y / N)")
            select_counter = 0

            while select_counter < 1:
                choice = input()
                if choice == "Y":
                    print("You take the " + char1.position.items + " with you.")
                    select_counter += 1
                    char1.position.items = "none"
                elif choice == "N":
                    print("You let the " + char1.position.items + "in the room.")
                    select_counter += 1
                else:
                    print("Please enter a valid response.")



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
        char1.name = charname
        while char1.health > 0:

            print(" \nGreat! Your character goes by the name " + char1.name + ". \n")
            print("I wish you all the luck while you are discovering the mysterious 'Lettered Dungeon'. \n")

            print("\nYou are " + char1.name + ", a courageous pathfinder and hero. Your newest quest leads you to the mysterious 'Lettered Dungeon', where monsters stole all the letters.")
            print("The infamous Dungeon awaits you with a large black entry. Fierceless as you are, you are lighting up a torch and take the first steps into the cave. \n")
            print("You enter the first room. In the left you see another door as well as on the right side. Which do you want to take?")
            print("You can either choose door 'A' or door 'B'.")



            counter_entry = 0

            while counter_entry < 1:
                entry_room = input()
                for x in entry_room:
                    if x == "A":
                        print("You open the left door with a big 'A' on it.")
                        char1.position = A
                        counter_entry += 1
                    elif x == "B":
                        print("You open the right door with a big 'B' on it.")
                        char1.position= B
                        counter_entry += 1 
                    else: 
                        print("Please choose between 'A' and 'B'.")


            # Die Position-Funktion ist vorhanden, ebenso die Möglichkeit einen Raum zu wechseln. Es fehlen nun alle Räume 
            # und ihre Verbindungen. 


            if char1.position == A:
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
                        A.monster = "none"
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
                        char1.position = Entry
                        dec_counter += 1
                        counter_entry -= 1

                    else:
                        print("Please enter a valid command: 'run' or 'fight'.")
                    
                    
                        
            elif char1.position == B:
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

