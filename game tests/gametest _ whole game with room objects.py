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
        self.position = "none"
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
bookzombieA = enemy("Book Zombie", 5, 1, 1, 35)
bookzombieJ = enemy("Book Zombie", 5, 1, 1, 35)

inkvampireC = enemy("Ink Vampire", 10, 2, 0, 60)
inkvampireH = enemy("Ink Vampire", 10, 2, 0, 60)
flyingscrollD = enemy("Flying Scroll", 3, 3, 2, 40)
flyingscrollF = enemy("Flying Scroll", 3, 3, 2, 40)
undeadstudentG = enemy("Undead Student", 5, 2, 0, 35)
undeadstudentI = enemy("Undead Student", 5, 2, 0, 35)
darkmageZ = enemy("Dark Mage", 10, 3, 2, 150)


#Nun werden die relevanten Objekte erstellt. Zuerst kommen alle Räume, danach der Endboss, welcher in Raum Entry erscheinen soll, nachdem der Spieler
#in Raum Z angekommen ist. Am Ende wird dann auch der Charakter selbst als Objekt erstellt. 

Entry = room("Entry", "none", "none", "A", "B", "none")
A = room("A", "none", bookzombieA, "C", "D", Entry)
B = room("B", "red potion", "none", "E", "F", Entry)
C = room("C", "none", inkvampireC, "G", "H", A)
D = room("D", "none", flyingscrollD, "I", "J", A)
E = room("E", "none", "none", "K", "L", B)
F = room("F", "none", flyingscrollF, "M", "N", B)
G = room("G", "none", undeadstudentG, "O", "none", C)
H = room("H", "none", inkvampireH, "O", "none", C)
I = room("I", "none", undeadstudentI, "P", "none", D)
J = room("J", "none", bookzombieJ, "P", "none", D)
K = room("K", "none", "none", "Q", "none", E)
L = room("L", "none", "none", "Q", "none", E)
M = room("M", "none", "none", "R", "none", F)
N = room("N", "none", "none", "R", "none", F)
O = room("O", "none", "none", G, H, "S")
P = room("P", "none", "none", I, J, "T")
Q = room("Q", "none", "none", K, L, "U")
R = room("R", "none", "none", M, N, "V")
S = room("S", "none", "none", O, "W", "none")
T = room("T", "none", "none", P, "W", "none")
U = room("U", "none", "none", Q, "X", "none")
V = room("V", "none", "none", R, "X", "none")
W = room("W", "none", "none", S, T, "Y")
X = room("X", "none", "none", V, U, "Y")
Y = room("Y", "none", "none", X, W, "Z")
Z = room("Z", "none", "dark mage", "none", "none", Y)

Entry.dl1 = A
Entry.dl2 = B
A.dl1 = C
A.dl2 = D
B.dl1 = E
B.dl2 = F
C.dl1 = G
C.dl2 = H
D.dl1 = I
D.dl2 = J
E.dl1 = K
E.dl2 = L
F.dl1 = M
F.dl2 = N
G.dl1 = O
H.dl1 = O
I.dl1 = P
J.dl1 = P
K.dl1 = Q
L.dl1 = Q
M.dl1 = R
N.dl1 = R
O.pre_dl = S
P.pre_dl = I
Q.pre_dl = U
R.pre_dl = V
S.dl2 = W
T.dl2 = W
U.dl2 = X
V.dl2 = X
W.pre_dl = Y
X.pre_dl = Y
Y.pre_dl = Z




#Nachfolgend kommen wichtige Prüf-Funktionen, wenn Räume betreten werden. 
#Die Check-Funktion für items ist allgemeingültig und soweit fertig. Muss später noch implementiert werden. 
#Die Check-Funktion für Gegner muss noch allgemeingültig werden.  


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

#Die fight-Funktion wird immer dann aufgerufen, wenn der Charakter einen neuen Raum betritt und dort ein Monster ist. 
#Alternativ kann er Charakter in den vorherigen Raum rennen. 

def fight(fight_enemy):
    if char1.position.monster != "none":
        print("Do you want to fight the monster? (Y / N)")
        fight_counter = 0
        fight_check = input()
        while fight_counter < 1:
            if fight_check == "Y":
                print("You attack your enemy with your " + char1.offhand + " while dealing " + str(char1.attack) + " damage per round.")
                print("The " + char1.position.monster + " attacks you with 1 attackpoint per round.")
                while char1.health > 0 or fight_enemy.health > 0:
                    char1.position.monster.health -= char1.attack
                    char1.health -= fight_enemy.attack
                    if char1.health == 0:
                        print("You died in the fight versus the " + char1.position.monster + ".")
                        print("You have " + str(char1.health) + " health points left.")
                    elif fight_enemy.health == 0:
                        print("You won the fight against " + char1.position.monster + ".")
                fight_counter += 1
            elif fight_check == "N":
                print("You make haste and run back to the previous room. ")
                char1.position = char1.prepos[:-1]
                fight_counter += 1
                #Möglichkeit die vorherige char1.position speichern?! Aktuell wird lediglich ein String gespeichert...

#check_enemy dient der Überprüfung, ob es im aktuellen Raum Monster gibt. Diese Funktion soll beim jedem Betreten eines Raums durchgeführt werden. 
def check_enemy():
    if char1.position.monster == "none":
        print("There is no enemy in the current room.")
    elif char1.position.monster != "none":
        fight(char1.position.monster)


#Die visitroom-Funktion wird so oft durchgeführt, bis der Charakter in Raum Z. angekommen ist. 
#Sie beinhaltet die check_enemy und die check_items Funktionen. 
def visitroom():
    print("You open the door and enter the room " + str(char1.position) + ".")
    check_enemy()
    check_items()
    print("Which door do you want to take next? " + str(char1.position.dl1) + " or " + str(char1.position.dl2) + ".")
    decision_counter = 0
    while decision_counter < 1:
        decision_room = input()
        if decision_room == str(char1.position.dl1):
            print("You choose to open the door with the letter " + str(char1.position.dl1 + " on it."))
            decision_counter += 1
        elif decision_room == str(char1.position.dl2):
            print("You choose to open the door with the letter " + str(char1.position.dl2 + " on it."))
            decision_counter += 1
        else:
            print("Please enter a valid response. (" + str(char1.position.dl1) + " / " + str(char1.position.dl2) + ")")

#Die pushbutton-Funktion kann durch den Charakter in Raum Z aktiviert werden. Damit öffnet sich die Eingangstür wieder und der Endboss erscheint im Raum "Entry"
def pushbutton():
    push_counter = 0
    print("You see an antique interface with a round button on it. It has a label on top of it which says 'Door'. Do you want to push it? (Y / N) \n")
    while push_counter < 1:
        push_answer = input()
        if push_answer == "Y":
            print("You press the big button and hear a distant sound of an opening door.")
            Entry.monster = endboss
            push_counter += 1
        elif push_answer == "N":
            print("You let the button where it is to discover more of the dungeon.")
            push_counter += 1
        else:
            print("Please enter a valid response (Y /N).")


#Hier beginnt nun der Quelltext für das richtige Spiel: 

char1.position = Entry

game_counter = 0

while game_counter == 0:
    print("\n\nWelcome to the game. \n")
    print("How do you want to call your character? \n")
    charname = input()
    char1.name = charname
    print("\nAlright. Your character goes by the name " + char1.name + ". \n")
    print("Let's get started. \n")

    print("You are currently in the room " + str(char1.position) + ".")
    print("In the room you see further doors with the letters " + str(char1.position.dl1) + " and " + str(char1.position.dl2) + " on them.")
    print("Which one do you want to enter? (" + str(char1.position.dl1) + " / " + str(char1.position.dl2) + ") \n")

    first_dec = input()
    first_dec_counter = 0
    while first_dec_counter < 1:
        if first_dec == str(char1.position.dl1):
            char1.position = char1.position.dl1
        elif first_dec == str(char1.position.dl2):
            char1.position = char1.position.dl2

    while char1.health > 0: 
        visitroom()

