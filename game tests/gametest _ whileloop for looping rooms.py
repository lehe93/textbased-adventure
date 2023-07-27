
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
        self.position = "Entry"
        self.prepos = []
        
        if self.exp >= 500:
            self.level += 1
            self.attack += 1
            self.defense += 1
            self.health += 5 
            self.exp = 0


#Zuerst werden die Gegner-Objekte sowie der Charakter und der Endboss angelegt. 
#Main persons/characters
endboss = enemy("Lettered Guardian", 50, 4, 3, 1000)
char1 = character("none")

#simple enemies
bookzombie = enemy("Book Zombie", 5, 1, 1, 35)
inkvampire = enemy("Ink Vampire", 10, 2, 0, 60)
flyingscroll = enemy("Flying Scroll", 3, 3, 2, 40)
undeadstudent = enemy("Undead Student", 5, 2, 0, 35)


#Nun werden die relevanten Objekte erstellt. Zuerst kommen alle Räume, danach der Endboss, welcher in Raum Entry erscheinen soll, nachdem der Spieler
#in Raum Z angekommen ist. Am Ende wird dann auch der Charakter selbst als Objekt erstellt. 

Entry = room("Entry", "none", "none", "A", "B", "none")
A = room("A", "none", "Book Zombie", "C", "D", "Entry")
B = room("B", "red potion", "none", "E", "F", "Entry")
C = room("C", "none", "Ink Vampire", "G", "H", "A")
D = room("D", "none", "Flying Scroll", "I", "J", "A")
E = room("E", "none", "none", "K", "L", "B")
F = room("F", "none", "Flying Scroll", "M", "N", "B")
G = room("G", "none", "Undead Student", "O", "none", "C")
H = room("H", "none", "Ink Vampire", "O", "none", "C")
I = room("I", "none", "Undead Student", "P", "none", "D")
J = room("J", "none", "Book Zombie", "P", "none", "D")
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
Z = room("Z", "none", "dark mage", "none", "none", "Y")



#Nachfolgend kommen wichtige Prüf-Funktionen, wenn Räume betreten werden. 
#Die Check-Funktion für items ist allgemeingültig und soweit fertig. Muss später noch implementiert werden. 
#Die Check-Funktion für Gegner muss noch allgemeingültig werden.  
#check_enemy dient der Überprüfung, ob es im aktuellen Raum Monster gibt. Diese Funktion soll beim jedem Betreten eines Raums durchgeführt werden. 
def check_enemy(pos):
    if pos.monster == "none":
        print("\nThere is no enemy in the current room.")
    elif pos.monster != "none":
        print("As you enter the room, you are attacked by a " + pos.monster + ".")


#check_items dient der Überprüfung, ob es im aktuellen Raum Items gibt, bzw. ob diese herumliegen. 
def check_items(item_pos):
        if item_pos.items == "none":
            print("\nThere are no items on the floor.")
        elif item_pos.items != "none":
            print("As you observe the room for some loot, you find a " + item_pos.items + ".")
            print("Do you want to take it? (Y / N)")
            select_counter = 0

            while select_counter < 1:
                choice = input()
                if choice == "Y":
                    print("You take the " + item_pos.items + " with you.")
                    select_counter += 1
                    item_pos.items = "none"
                elif choice == "N":
                    print("You let the " + item_pos.items + "in the room.")
                    select_counter += 1
                else:
                    print("Please enter a valid response.")


#Fight-Funktion muss überarbeitet werden. Der Defense-Bonus von char und enemy muss noch eingebaut werden. 

def fight(fight_pos):
    if fight_pos.monster != "none":
        print("You grab your Weapons and start the fight versus the " + str(fight_pos.monster) + ".")
        if fight_pos.monster == "Book Zombie":
            while bookzombie.health > 0 and char1.health > 0:
                bookzombie.health -= char1.attack
                print("You hit your enemy for " + str(char1.attack) + " damage. It has " + str(bookzombie.health) + " hitpoints left.")
                char1.health -= bookzombie.attack
                print("You got hit by your enemy for " + str(bookzombie.attack) + "damage. You have " + str(char1.health) + " hitpoints left.")
                if bookzombie.health == 0:
                    print("\nYou won the fight versus the Book Zombie and earned " + str(bookzombie.expbonus) + " experience points.")
                    char1.exp += bookzombie.expbonus
                    print("You have " + str(char1.exp) + " experience points and need " + str(500 - char1.exp) + " more points for the next character level.")
                elif char1.health == 0: 
                    print("You died in the fight versus the Book Zombie. Please restart the game. ")
                    game_counter += 1
        elif fight_pos.monster == "Ink Vampire":
            while char1.health > 0 or inkvampire.health > 0:
                inkvampire.health -= char1.attack
                char1.health -= inkvampire.health


#Erster Versuch eine Loop-Funktion für das Durchsuchen der Räume zu bauen. Diese soll dann entsprechend oft geprüft werden in der Hauptschleife. 
#Entscheidungs-Funktion um neue Räume zu betreten muss noch eingebaut werden. 

def loop_rooms ():
    if char1.position == "A":
        check_enemy(A)
        fight(A)
        check_items(A)
    elif char1.position == "B":
        check_enemy(B)
        fight(B)
        check_items(B)
    elif char1.position == "C":
        check_enemy(C)
        fight(C)
        check_items(C)
    elif char1.position == "D":
        check_enemy(D)
        fight(D)
        check_items(D)
    elif char1.position == "E":
        check_enemy(E)
        fight(E)
        check_items(E)
    elif char1.position == "F":
        check_enemy(F)
        fight(F)
        check_items(F)
    elif char1.position == "G":
        check_enemy(G)
        fight(G)
        check_items(G)
    elif char1.position == "H":
        check_enemy(H)
        fight(H)
        check_items(H)        
    elif char1.position == "I":
        check_enemy(I)
        fight(I)
        check_items(I)
    elif char1.position == "J":
        check_enemy(J)
        fight(J)
        check_items(J)
    elif char1.position == "K":
        check_enemy(K)
        fight(K)
        check_items(K)
    elif char1.position == "L":
        check_enemy(L)
        fight(L)
        check_items(L)
    elif char1.position == "M":
        check_enemy(M)
        fight(M)
        check_items(M)
    elif char1.position == "N":
        check_enemy(N)
        fight(N)
        check_items(N)
    elif char1.position == "O":
        check_enemy(O)
        fight(O)
        check_items(O)
    elif char1.position == "P":
        check_enemy(P)
        fight(P)
        check_items(P)
    elif char1.position == "Q":
        check_enemy(Q)
        fight(Q)
        check_items(Q)
    elif char1.position == "R":
        check_enemy(R)
        fight(R)
        check_items(R)
    elif char1.position == "S":
        check_enemy(S)
        fight(S)
        check_items(S)
    elif char1.position == "T":
        check_enemy(T)
        fight(T)
        check_items(T)
    elif char1.position == "U":
        check_enemy(U)
        fight(U)
        check_items(U)
    elif char1.position == "V":
        check_enemy(V)
        fight(V)
        check_items(V)
    elif char1.position == "W":
        check_enemy(W)
        fight(W)
        check_items(W)
    elif char1.position == "X":
        check_enemy(X)
        fight(X)
        check_items(X)
    elif char1.position == "Y":
        check_enemy(Y)
        fight(Y)
        check_items(Y)
    elif char1.position == "Z":
        check_enemy(Z)
        fight(Z)    
        check_items(Z)

#Game_Counter zum starten des Spiels
game_counter = 0

while game_counter < 1:
    print("Welcome to the game!")
    print("What is your character's name?\n")
    charname = input()
    char1.name = charname


    print("\nGreat! Your character has the name " + str(char1.name) + ".")
    print("Let's get started.")

    #Schleife muss überarbeitet werden, um die Räume nach und nach zu prüfen. 
    while char1.health > 0:
        print("Your current position is " + str(char1.position) + ".")
        print("Where do you want to go next? Do you want to open door A or door B? (A / B)")
        select_counter = 0
        while select_counter < 1:
            select_choice = input()
            if select_choice == "A":
                char1.position = "A"
                select_counter += 1
            elif select_choice == "B":
                char1.position = "B"
                select_counter += 1
            else:
                print("Please enter a valid response. (A / B)")
        loop_rooms()

    #Eine neue Funktion muss gebaut werden, um die Position des Characters mit dem jeweiligen Raum zu verbinden. Link für eine Möglichkeit wurde abgespeichert. 