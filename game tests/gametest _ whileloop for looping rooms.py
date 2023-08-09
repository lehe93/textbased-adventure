
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
        self.health = int(20)
        self.exp = int(0) 
        self.attack = int(2)
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
bookzombie = enemy("Book Zombie", 5, 1, 0, 70)
inkvampire = enemy("Ink Vampire", 10, 2, 0, 120)
flyingscroll = enemy("Flying Scroll", 3, 3, 1, 80)
undeadstudent = enemy("Undead Student", 5, 2, 0, 75)


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
K = room("K", "none", "Book Zombie", "Q", "none", "E")
L = room("L", "none", "Book Zombie", "Q", "none", "E")
M = room("M", "none", "Ink Vampire", "R", "none", "F")
N = room("N", "none", "Undead Student", "R", "none", "F")
O = room("O", "none", "Undead Student", "G", "H", "S")
P = room("P", "none", "Flying Scroll", "I", "J", "T")
Q = room("Q", "none", "Flying Scroll", "K", "L", "U")
R = room("R", "none", "Ink Vampire", "M", "N", "V")
S = room("S", "none", "Ink Vampire", "O", "W", "none")
T = room("T", "none", "none", "P", "W", "none")
U = room("U", "none", "Undead Student", "Q", "X", "none")
V = room("V", "none", "Book Zombie", "R", "X", "none")
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
        print("As you enter the room, you are attacked by a " + pos.monster + ".\n")


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
        print("You grab your Weapons and start the fight versus the " + str(fight_pos.monster) + ".\n")
        if fight_pos.monster == "Book Zombie":
            while bookzombie.health > 0:
                bookzombie.health -= char1.attack
                print("You hit your enemy for " + str(char1.attack) + " damage. It has " + str(bookzombie.health) + " hitpoints left.")
                char1.health -= bookzombie.attack
                print("You got hit by your enemy for " + str(bookzombie.attack) + " damage. You have " + str(char1.health) + " hitpoints left.")
                if bookzombie.health <= 0:
                    print("\nYou won the fight versus the Book Zombie and earned " + str(bookzombie.expbonus) + " experience points.")
                    char1.exp += bookzombie.expbonus
                    fight_pos.monster = "none"
                    print("You have " + str(char1.exp) + " experience points and need " + str(500 - char1.exp) + " more points for the next character level.")
                elif char1.health <= 0: 
                    print("You died in the fight versus the Book Zombie. Please restart the game. ")
                    game_counter += 1
        elif fight_pos.monster == "Ink Vampire":
            while inkvampire.health > 0:
                inkvampire.health -= char1.attack
                print("You hit your enemy for " + str(char1.attack) + " damage. It has " + str(inkvampire.health) + " hitpoints left.")
                char1.health -= inkvampire.attack
                print("You got hit by your enemy for " + str(inkvampire.attack) + " damage. You have " + str(char1.health) + " hitpoints left.")
                if inkvampire.health <= 0:
                    print("\nYou won the fight versus the Ink Vampire and earned " + str(inkvampire.expbonus) + " experience points.")
                    char1.exp += inkvampire.expbonus
                    fight_pos.monster = "none"
                    print("You have " + str(char1.exp) + " experience points and need " + str(500 - char1.exp) + " more points for the next character level.")
                elif char1.health <= 0: 
                    print("You died in the fight versus the Ink Vampire. Please restart the game. ")
                    game_counter += 1
        elif fight_pos.monster == "Flying Scroll":
            while flyingscroll.health > 0:
                flyingscroll.health -= char1.attack
                print("You hit your enemy for " + str(char1.attack) + " damage. It has " + str(flyingscroll.health) + " hitpoints left.")
                char1.health -= flyingscroll.attack
                print("You got hit by your enemy for " + str(flyingscroll.attack) + " damage. You have " + str(char1.health) + " hitpoints left.")
                if flyingscroll.health <= 0:
                    print("\nYou won the fight versus the Flying Scroll and earned " + str(flyingscroll.expbonus) + " experience points.")
                    char1.exp += flyingscroll.expbonus
                    fight_pos.monster = "none"
                    print("You have " + str(char1.exp) + " experience points and need " + str(500 - char1.exp) + " more points for the next character level.")
                elif char1.health <= 0: 
                    print("You died in the fight versus the Flying Scroll. Please restart the game. ")
                    game_counter += 1
        elif fight_pos.monster == "Undead Student":
            while undeadstudent.health > 0:
                undeadstudent.health -= char1.attack
                print("You hit your enemy for " + str(char1.attack) + " damage. It has " + str(undeadstudent.health) + " hitpoints left.")
                char1.health -= undeadstudent.attack
                print("You got hit by your enemy for " + str(undeadstudent.attack) + " damage. You have " + str(char1.health) + " hitpoints left.")
                if undeadstudent.health <= 0:
                    print("\nYou won the fight versus the Undead Student and earned " + str(undeadstudent.expbonus) + " experience points.")
                    char1.exp += undeadstudent.expbonus
                    fight_pos.monster = "none"
                    print("You have " + str(char1.exp) + " experience points and need " + str(500 - char1.exp) + " more points for the next character level.")
                elif char1.health <= 0: 
                    print("You died in the fight versus the Undead Student. Please restart the game. ")
                    game_counter += 1
        elif fight_pos.monster == "Lettered Guardian":
            while endboss.health > 0:
                endboss.health -= char1.attack
                print("You hit your enemy for " + str(char1.attack) + " damage. It has " + str(endboss.health) + " hitpoints left.")
                char1.health -= endboss.attack
                print("You got hit by your enemy for " + str(endboss.attack) + " damage. You have " + str(char1.health) + " hitpoints left.")
                if endboss.health <= 0:
                    print("\nYou won the fight versus the Lettered Guardian and earned " + str(endboss.expbonus) + " experience points.")
                    char1.exp += endboss.expbonus
                    fight_pos.monster = "none"
                    print("You have " + str(char1.exp) + " experience points and need " + str(500 - char1.exp) + " more points for the next character level.")
                elif char1.health <= 0: 
                    print("You died in the fight versus the Lettered Guardian. Please restart the game. ")
                    game_counter += 1

#chooseRoom-Funktion wird gebaut, um den Wechsel zwischen den Räumen zu vereinfachen. 
def chooseRoom():
    print("You are currently in the room " + str(char1.position) + ".")
    if char1.position == "Entry":
        print("You can either enter door " + Entry.dl1 + " or door "+ Entry.dl2 + ". Where do you want to go? (" + Entry.dl1 + " / " + Entry.dl2 + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == "A":
                char1.position = "A"
                print("You choose to open the door to room A and enter it.")
                room_counter += 1
            elif roomChoose == "B":
                char1.position = "B"
                print("You choose to open the door to room B and enter it.")
                room_counter += 1
            else: 
                print("Please enter a valid response.")
    elif char1.position == "A":
        print("You can either enter door " + A.dl1+ " or door "+ A.dl2 + " or you could go back to " + A.pre_dl + ". Where do you want to go? (" + A.dl1 + " / " + A.dl2+ " / " + A.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == "C":
                char1.position = "C"
                print("You choose to open the door to room C and enter it.")
                room_counter += 1
            elif roomChoose == "D":
                char1.position = "D"
                print("You choose to open the door to room D and enter it.")
                room_counter += 1
            elif roomChoose == "Entry":
                char1.position = "Entry"
                room_counter += 1
                print("You choose to go back to Entry.")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "B":
        print("You can either enter door " + B.dl1+ " or door "+ B.dl2 + " or you could go back to " + B.pre_dl + ". Where do you want to go? (" + B.dl1 + " / " + B.dl2+ " / " + B.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == "E":
                char1.position = "E"
                print("You choose to open the door to room E and enter it.")
                room_counter += 1
            elif roomChoose == "F":
                char1.position = "F"
                print("You choose to open the door to room F and enter it.")
                room_counter += 1
            elif roomChoose == "Entry":
                char1.position = "Entry"
                room_counter += 1
                print("You choose to go back to Entry.")
            else: 
                print("Please enter a valid response.")


#Die pushButtonFunktion soll erst ausgelöst werden, wenn der Charakter sich in Raum Z befindet. Er wird dann gefragt, ob er den großen Knopf drücken will.
#Falls der Knopf gedrückt wird, öffnet sich die verschlossene Tür am Eingang und der Endboss erscheint dort. 

def pushButton():
    print("As you enter room Z you see an old mechanical device with a round button on it. Do you want to press the button? (Yes / No) \n")
    button_counter = 0
    while button_counter < 1:
        button_choice = input()
        if button_choice == "Yes":
            print("You press the button and hear the distant sound of opening the entry gate.")
            Entry.monster = "Lettered Guardian"
            print("Right after that you hear a loud monstrous growling coming from the entrance.\n")
            button_counter += 1
        elif button_choice == "No":
            print("You think that it is not a wise choice to press an old button without knowing what it does.\n")
            print("Since you are in the last room, you start noticing, that you have to figure out a way how you get out of the 'Lettered Dungeon'.\n")
            button_counter += 1
        else: 
            print("Please enter a valid response.")


#Erster Versuch eine Loop-Funktion für das Durchsuchen der Räume zu bauen. Diese soll dann entsprechend oft geprüft werden in der Hauptschleife. 
#Entscheidungs-Funktion um neue Räume zu betreten muss noch eingebaut werden. 

#char1.position ist angepasst. 

def loop_rooms ():
    select_counter = 0
    while select_counter < 1:
        select_choice = input()
        char1.position = select_choice
        print("You choose to enter the room " + select_choice + ".\n")
        if char1.position == "A":
            check_enemy(A)
            fight(A)
            check_items(A)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(A.pre_dl) + " or to rooms " + str(A.dl1) + " or " + str(A.dl2) + ".\n")
        elif char1.position == "B":
            check_enemy(B)
            fight(B)
            check_items(B)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(B.pre_dl) + " or to rooms " + str(B.dl1) + " or " + str(B.dl2) + ".\n")
        elif char1.position == "C":
            check_enemy(C)
            fight(C)
            check_items(C)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(C.pre_dl) + " or to rooms " + str(C.dl1) + " or " + str(C.dl2) + ".\n")
        elif char1.position == "D":
            check_enemy(D)
            fight(D)
            check_items(D)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(D.pre_dl) + " or to rooms " + str(D.dl1) + " or " + str(D.dl2) + ".\n")
        elif char1.position == "E":
            check_enemy(E)
            fight(E)
            check_items(E)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(E.pre_dl) + " or to rooms " + str(E.dl1) + " or " + str(E.dl2) + ".\n")
        elif char1.position == "F":
            check_enemy(F)
            fight(F)
            check_items(F)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(F.pre_dl) + " or to rooms " + str(F.dl1) + " or " + str(F.dl2) + ".\n")
        elif char1.position == "G":
            check_enemy(G)
            fight(G)
            check_items(G)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(G.pre_dl) + " or to room " + str(G.dl1) + ".\n")
        elif char1.position == "H":
            check_enemy(H)
            fight(H)
            check_items(H)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(H.pre_dl) + " or to room " + str(H.dl1) + ".\n")        
        elif char1.position == "I":
            check_enemy(I)
            fight(I)
            check_items(I)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(I.pre_dl) + " or to room " + str(I.dl1) + ".\n")
        elif char1.position == "J":
            check_enemy(J)
            fight(J)
            check_items(J)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(J.pre_dl) + " or to room " + str(J.dl1) + ".\n")
        elif char1.position == "K":
            check_enemy(K)
            fight(K)
            check_items(K)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(K.pre_dl) + " or to room " + str(K.dl1) + ".\n")
        elif char1.position == "L":
            check_enemy(L)
            fight(L)
            check_items(L)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(L.pre_dl) + " or to room " + str(L.dl1) + ".\n")
        elif char1.position == "M":
            check_enemy(M)
            fight(M)
            check_items(M)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(M.pre_dl) + " or to room " + str(M.dl1) + ".\n")
        elif char1.position == "N":
            check_enemy(N)
            fight(N)
            check_items(N)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(N.pre_dl) + " or to room " + str(N.dl1) + ".\n")
        elif char1.position == "O":
            check_enemy(O)
            fight(O)
            check_items(O)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(O.pre_dl) + " or to rooms " + str(O.dl1) + " or " + str(O.dl2) + ".\n")
        elif char1.position == "P":
            check_enemy(P)
            fight(P)
            check_items(P)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(P.pre_dl) + " or to rooms " + str(P.dl1) + " or " + str(P.dl2) + ".\n")
        elif char1.position == "Q":
            check_enemy(Q)
            fight(Q)
            check_items(Q)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(Q.pre_dl) + " or to rooms " + str(Q.dl1) + " or " + str(Q.dl2) + ".\n")
        elif char1.position == "R":
            check_enemy(R)
            fight(R)
            check_items(R)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(R.pre_dl) + " or to rooms " + str(R.dl1) + " or " + str(R.dl2) + ".\n")
        elif char1.position == "S":
            check_enemy(S)
            fight(S)
            check_items(S)
            print("You are currently in the room " + str(char1.position) + ". You can go to rooms " + str(S.dl1) + " or " + str(S.dl2) + ".\n")
        elif char1.position == "T":
            check_enemy(T)
            fight(T)
            check_items(T)
            print("You are currently in the room " + str(char1.position) + ". You can go to rooms " + str(T.dl1) + " or " + str(T.dl2) + ".\n")
        elif char1.position == "U":
            check_enemy(U)
            fight(U)
            check_items(U)
            print("You are currently in the room " + str(char1.position) + ". You can go to rooms " + str(U.dl1) + " or " + str(U.dl2) + ".\n")
        elif char1.position == "V":
            check_enemy(V)
            fight(V)
            check_items(V)
            print("You are currently in the room " + str(char1.position) + ". You can go to rooms " + str(V.dl1) + " or " + str(V.dl2) + ".\n")
        elif char1.position == "W":
            check_enemy(W)
            fight(W)
            check_items(W)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(W.pre_dl) + " or to rooms " + str(W.dl1) + " or " + str(W.dl2) + ".\n")
        elif char1.position == "X":
            check_enemy(X)
            fight(X)
            check_items(X)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(X.pre_dl) + " or to rooms " + str(X.dl1) + " or " + str(X.dl2) + ".\n")
        elif char1.position == "Y":
            check_enemy(Y)
            fight(Y)
            check_items(Y)
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(Y.pre_dl) + " or to rooms " + str(Y.dl1) + " or " + str(Y.dl2) + ".\n")
        elif char1.position == "Z":
            check_enemy(Z)
            fight(Z)    
            check_items(Z)
            pushButton()
            print("You are currently in the room " + str(char1.position) + ". You can go back to " + str(Z.pre_dl) + ".\n")
        elif char1.position == "Entry":
            check_enemy(Entry)
            fight(Entry)
            check_items(Entry)
            print("You are currently in the room " + str(char1.position) + ". You can go to rooms " + str(Entry.dl1) + " or " + str(Entry.dl2) + ".\n")
        else:
            print("Please enter a valid response")
#Game_Counter zum starten des Spiels
game_counter = 0

while game_counter < 1:
    print("Welcome to the game!")
    print("What is your character's name?\n")
    charname = input()
    char1.name = charname


    print("\nGreat! Your character has the name " + str(char1.name) + ".")
    print("Let's get started.")

    chooseRoom()
    print(char1.position)

    #Schleife muss überarbeitet werden, um die Räume nach und nach zu prüfen. 
    while char1.health > 0:
        chooseRoom()
        loop_rooms()

    #Eine neue Funktion muss gebaut werden, um die Position des Characters mit dem jeweiligen Raum zu verbinden. Link für eine Möglichkeit wurde abgespeichert. 