
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
                    if item_pos.items == "red potion":
                        print("As you open the flask you smell a sense of wild berries and a fruity flavor.")
                        print("You drink the red potion and gain + 8 health points.\n")
                        char1.health += 8
                    elif item_pos.items == "blue potion":
                        print("As you open the flask you smell a strong flavor of iron, metal and something between stones and sand.")
                        print("You drink the blue potion and gain + 2 additional attack damage.\n")
                        char1.attack += 2
                    elif item_pos.items == "rusty sword":
                        print("You change your weapons from " + char1.offhand + " to your new rusty sword.")
                        print("With your new weapon you gain additional 2 attack points.\n")
                        char1.attack += 2
                        char1.offhand = "rusty sword"
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
            if roomChoose == Entry.dl1:
                char1.position = Entry.dl1
                print("You choose to open the door to room " + Entry.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == Entry.dl2:
                char1.position = Entry.dl2
                print("You choose to open the door to room " + Entry.dl2 + " and enter it.")
                room_counter += 1
            else: 
                print("Please enter a valid response.")
    elif char1.position == "A":
        print("You can either enter door " + A.dl1+ " or door "+ A.dl2 + " or you could go back to " + A.pre_dl + ". Where do you want to go? (" + A.dl1 + " / " + A.dl2+ " / " + A.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == A.dl1:
                char1.position = A.dl1
                print("You choose to open the door to room "+ A.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == A.dl2:
                char1.position = A.dl2
                print("You choose to open the door to room " + A.dl2 + " and enter it.")
                room_counter += 1
            elif roomChoose == A.pre_dl:
                char1.position = A.pre_dl
                room_counter += 1
                print("You choose to go back to " + A.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "B":
        print("You can either enter door " + B.dl1+ " or door "+ B.dl2 + " or you could go back to " + B.pre_dl + ". Where do you want to go? (" + B.dl1 + " / " + B.dl2+ " / " + B.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == B.dl1:
                char1.position = B.dl1
                print("You choose to open the door to room " + B.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == B.dl2:
                char1.position = B.dl2
                print("You choose to open the door to room " + B.dl2 + " and enter it.")
                room_counter += 1
            elif roomChoose == B.pre_dl:
                char1.position = B.pre_dl
                room_counter += 1
                print("You choose to go back to " + B.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "C":
        print("You can either enter door " + C.dl1+ " or door "+ C.dl2 + " or you could go back to " + C.pre_dl + ". Where do you want to go? (" + C.dl1 + " / " + C.dl2+ " / " + C.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == C.dl1:
                char1.position = C.dl1
                print("You choose to open the door to room " + C.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == C.dl2:
                char1.position = C.dl2
                print("You choose to open the door to room " + C.dl2 + " and enter it.")
                room_counter += 1
            elif roomChoose == C.pre_dl:
                char1.position = C.pre_dl
                room_counter += 1
                print("You choose to go back to " + C.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "D":
        print("You can either enter door " + D.dl1+ " or door "+ D.dl2 + " or you could go back to " + D.pre_dl + ". Where do you want to go? (" + D.dl1 + " / " + D.dl2+ " / " + D.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == D.dl1:
                char1.position = D.dl1
                print("You choose to open the door to room " + D.dl1 +  " and enter it.")
                room_counter += 1
            elif roomChoose == D.dl2:
                char1.position = D.dl2
                print("You choose to open the door to room " + D.dl2 + " and enter it.")
                room_counter += 1
            elif roomChoose == D.pre_dl:
                char1.position = D.pre_dl
                room_counter += 1
                print("You choose to go back to " + D.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "E":
        print("You can either enter door " + E.dl1+ " or door "+ E.dl2 + " or you could go back to " + E.pre_dl + ". Where do you want to go? (" + E.dl1 + " / " + E.dl2+ " / " + E.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == E.dl1:
                char1.position = E.dl1
                print("You choose to open the door to room " + E.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == E.dl2:
                char1.position = E.dl2
                print("You choose to open the door to room " + E.dl2 + " and enter it.")
                room_counter += 1
            elif roomChoose == E.pre_dl:
                char1.position = E.pre_dl
                room_counter += 1
                print("You choose to go back to " + E.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "F":
        print("You can either enter door " + F.dl1+ " or door "+ F.dl2 + " or you could go back to " + F.pre_dl + ". Where do you want to go? (" + F.dl1 + " / " + F.dl2+ " / " + F.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == F.dl1:
                char1.position = F.dl1
                print("You choose to open the door to room " + F.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == F.dl2:
                char1.position = F.dl2
                print("You choose to open the door to room " + F.dl2 +" and enter it.")
                room_counter += 1
            elif roomChoose == F.pre_dl:
                char1.position = F.pre_dl
                room_counter += 1
                print("You choose to go back to " + F.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "G":
        print("You can either enter door " + G.dl1+ " or you could go back to " + G.pre_dl + ". Where do you want to go? (" + G.dl1 + " / " + G.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == G.dl1:
                char1.position = G.dl1
                print("You choose to open the door to room " + G.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == G.pre_dl:
                char1.position = G.pre_dl
                room_counter += 1
                print("You choose to go back to " + G.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "H":
        print("You can either enter door " + H.dl1+ " or you could go back to " + H.pre_dl + ". Where do you want to go? (" + H.dl1 + " / " + H.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == H.dl1:
                char1.position = H.dl1
                print("You choose to open the door to room " + H.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == H.pre_dl:
                char1.position = H.pre_dl
                room_counter += 1
                print("You choose to go back to " + H.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "I":
        print("You can either enter door " + I.dl1+ " or you could go back to " + I.pre_dl + ". Where do you want to go? (" + I.dl1 + " / " + I.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == I.dl1:
                char1.position = I.dl1
                print("You choose to open the door to room " + I.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == I.pre_dl:
                char1.position = I.pre_dl
                room_counter += 1
                print("You choose to go back to " + I.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "J":
        print("You can either enter door " + J.dl1+ " or you could go back to " + J.pre_dl + ". Where do you want to go? (" + J.dl1 + " / " + J.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == J.dl1:
                char1.position = J.dl1
                print("You choose to open the door to room " + J.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == J.pre_dl:
                char1.position = J.pre_dl
                room_counter += 1
                print("You choose to go back to " + J.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "K":
        print("You can either enter door " + K.dl1+ " or you could go back to " + K.pre_dl + ". Where do you want to go? (" + K.dl1 + " / " + K.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == K.dl1:
                char1.position = K.dl1
                print("You choose to open the door to room " + K.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == K.pre_dl:
                char1.position = K.pre_dl
                room_counter += 1
                print("You choose to go back to " + K.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "L":
        print("You can either enter door " + L.dl1+ " or you could go back to " + L.pre_dl + ". Where do you want to go? (" + L.dl1 + " / " + L.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == L.dl1:
                char1.position = L.dl1
                print("You choose to open the door to room " + L.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == L.pre_dl:
                char1.position = L.pre_dl
                room_counter += 1
                print("You choose to go back to " + L.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "M":
        print("You can either enter door " + M.dl1+ " or you could go back to " + M.pre_dl + ". Where do you want to go? (" + M.dl1 + " / " + M.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == M.dl1:
                char1.position = M.dl1
                print("You choose to open the door to room " + M.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == M.pre_dl:
                char1.position = M.pre_dl
                room_counter += 1
                print("You choose to go back to " + M.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "N":
        print("You can either enter door " + N.dl1+ " or you could go back to " + N.pre_dl + ". Where do you want to go? (" + N.dl1 + " / " + N.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == N.dl1:
                char1.position = N.dl1
                print("You choose to open the door to room " + N.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == N.pre_dl:
                char1.position = N.pre_dl
                room_counter += 1
                print("You choose to go back to " + N.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "O":
        print("You can either enter door " + O.dl1+ " or door "+ O.dl2 + " or you could go back to " + O.pre_dl + ". Where do you want to go? (" + O.dl1 + " / " + O.dl2+ " / " + O.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == O.dl1:
                char1.position = O.dl1
                print("You choose to open the door to room " + O.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == O.dl2:
                char1.position = O.dl2
                print("You choose to open the door to room " + O.dl2 +" and enter it.")
                room_counter += 1
            elif roomChoose == O.pre_dl:
                char1.position = O.pre_dl
                room_counter += 1
                print("You choose to go back to " + O.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "P":
        print("You can either enter door " + P.dl1+ " or door "+ P.dl2 + " or you could go back to " + P.pre_dl + ". Where do you want to go? (" + P.dl1 + " / " + P.dl2+ " / " + P.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == P.dl1:
                char1.position = P.dl1
                print("You choose to open the door to room " + P.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == P.dl2:
                char1.position = P.dl2
                print("You choose to open the door to room " + P.dl2 +" and enter it.")
                room_counter += 1
            elif roomChoose == P.pre_dl:
                char1.position = P.pre_dl
                room_counter += 1
                print("You choose to go back to " + P.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "Q":
        print("You can either enter door " + Q.dl1+ " or door "+ Q.dl2 + " or you could go back to " + Q.pre_dl + ". Where do you want to go? (" + Q.dl1 + " / " + Q.dl2+ " / " + Q.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == Q.dl1:
                char1.position = Q.dl1
                print("You choose to open the door to room " + Q.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == Q.dl2:
                char1.position = Q.dl2
                print("You choose to open the door to room " + Q.dl2 +" and enter it.")
                room_counter += 1
            elif roomChoose == Q.pre_dl:
                char1.position = Q.pre_dl
                room_counter += 1
                print("You choose to go back to " + Q.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "R":
        print("You can either enter door " + R.dl1+ " or door "+ R.dl2 + " or you could go back to " + R.pre_dl + ". Where do you want to go? (" + R.dl1 + " / " + R.dl2+ " / " + R.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == R.dl1:
                char1.position = R.dl1
                print("You choose to open the door to room " + R.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == R.dl2:
                char1.position = R.dl2
                print("You choose to open the door to room " + R.dl2 +" and enter it.")
                room_counter += 1
            elif roomChoose == R.pre_dl:
                char1.position = R.pre_dl
                room_counter += 1
                print("You choose to go back to " + R.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "S":
        print("You can either enter door " + S.dl2 + " or you could go back to " + S.dl1 + ". Where do you want to go? (" + S.dl2+ " / " + S.dl1 + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == S.dl1:
                char1.position = S.dl1
                print("You choose to go back to " + S.dl1 + ".")
                room_counter += 1
            elif roomChoose == S.dl2:
                char1.position = S.dl2
                print("You choose to open the door to room " + S.dl2 +" and enter it.")
                room_counter += 1
            else: 
                print("Please enter a valid response.")
    elif char1.position == "T":
        print("You can either enter door " + T.dl2 + " or you could go back to " + T.dl1 + ". Where do you want to go? (" + T.dl2+ " / " + T.dl1 + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == T.dl1:
                char1.position = T.dl1
                print("You choose to go back to " + T.dl1 + ".")
                room_counter += 1
            elif roomChoose == T.dl2:
                char1.position = T.dl2
                print("You choose to open the door to room " + T.dl2 +" and enter it.")
                room_counter += 1
            else: 
                print("Please enter a valid response.")
    elif char1.position == "U":
        print("You can either enter door " + U.dl2 + " or you could go back to " + U.dl1 + ". Where do you want to go? (" + U.dl2+ " / " + U.dl1 + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == U.dl1:
                char1.position = U.dl1
                print("You choose to go back to " + U.dl1 + ".")
                room_counter += 1
            elif roomChoose == U.dl2:
                char1.position = U.dl2
                print("You choose to open the door to room " + U.dl2 +" and enter it.")
                room_counter += 1
            else: 
                print("Please enter a valid response.")
    elif char1.position == "V":
        print("You can either enter door " + V.dl2 + " or you could go back to " + V.dl1 + ". Where do you want to go? (" + V.dl2+ " / " + V.dl1 + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == V.dl1:
                char1.position = V.dl1
                print("You choose to go back to " + V.dl1 + ".")
                room_counter += 1
            elif roomChoose == V.dl2:
                char1.position = V.dl2
                print("You choose to open the door to room " + V.dl2 +" and enter it.")
                room_counter += 1
            else: 
                print("Please enter a valid response.")
    elif char1.position == "W":
        print("You can either enter door " + W.dl1+ " or door "+ W.dl2 + " or you could go back to " + W.pre_dl + ". Where do you want to go? (" + W.dl1 + " / " + W.dl2+ " / " + W.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == W.dl1:
                char1.position = W.dl1
                print("You choose to open the door to room " + W.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == W.dl2:
                char1.position = W.dl2
                print("You choose to open the door to room " + W.dl2 +" and enter it.")
                room_counter += 1
            elif roomChoose == W.pre_dl:
                char1.position = W.pre_dl
                room_counter += 1
                print("You choose to go back to " + W.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "X":
        print("You can either enter door " + X.dl1+ " or door "+ X.dl2 + " or you could go back to " + X.pre_dl + ". Where do you want to go? (" + X.dl1 + " / " + X.dl2+ " / " + X.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == X.dl1:
                char1.position = X.dl1
                print("You choose to open the door to room " + X.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == X.dl2:
                char1.position = X.dl2
                print("You choose to open the door to room " + X.dl2 +" and enter it.")
                room_counter += 1
            elif roomChoose == X.pre_dl:
                char1.position = X.pre_dl
                room_counter += 1
                print("You choose to go back to " + X.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "Y":
        print("You can either enter door " + Y.dl1+ " or door "+ Y.dl2 + " or you could go back to " + Y.pre_dl + ". Where do you want to go? (" + Y.dl1 + " / " + Y.dl2+ " / " + Y.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == Y.dl1:
                char1.position = Y.dl1
                print("You choose to open the door to room " + Y.dl1 + " and enter it.")
                room_counter += 1
            elif roomChoose == Y.dl2:
                char1.position = Y.dl2
                print("You choose to open the door to room " + Y.dl2 +" and enter it.")
                room_counter += 1
            elif roomChoose == Y.pre_dl:
                char1.position = Y.pre_dl
                room_counter += 1
                print("You choose to go back to " + Y.pre_dl + ".")
            else: 
                print("Please enter a valid response.")
    elif char1.position == "Z":
        print("You can can go back to " + F.pre_dl + ". Where do you want to go? (" + F.pre_dl + ")")
        room_counter = 0
        while room_counter < 1:
            roomChoose = input()
            if roomChoose == F.pre_dl:
                char1.position = F.pre_dl
                room_counter += 1
                print("You choose to go back to " + F.pre_dl + ".")
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
            chooseRoom()
        elif char1.position == "B":
            check_enemy(B)
            fight(B)
            check_items(B)
            chooseRoom()
        elif char1.position == "C":
            check_enemy(C)
            fight(C)
            check_items(C)
            chooseRoom()
        elif char1.position == "D":
            check_enemy(D)
            fight(D)
            check_items(D)
            chooseRoom()
        elif char1.position == "E":
            check_enemy(E)
            fight(E)
            check_items(E)
            chooseRoom()
        elif char1.position == "F":
            check_enemy(F)
            fight(F)
            check_items(F)
            chooseRoom()
        elif char1.position == "G":
            check_enemy(G)
            fight(G)
            check_items(G)
            chooseRoom()
        elif char1.position == "H":
            check_enemy(H)
            fight(H)
            check_items(H)
            chooseRoom()
        elif char1.position == "I":
            check_enemy(I)
            fight(I)
            check_items(I)
            chooseRoom()
        elif char1.position == "J":
            check_enemy(J)
            fight(J)
            check_items(J)
            chooseRoom()
        elif char1.position == "K":
            check_enemy(K)
            fight(K)
            check_items(K)
            chooseRoom()
        elif char1.position == "L":
            check_enemy(L)
            fight(L)
            check_items(L)
            chooseRoom()
        elif char1.position == "M":
            check_enemy(M)
            fight(M)
            check_items(M)
            chooseRoom()
        elif char1.position == "N":
            check_enemy(N)
            fight(N)
            check_items(N)
            chooseRoom()
        elif char1.position == "O":
            check_enemy(O)
            fight(O)
            check_items(O)
            chooseRoom()
        elif char1.position == "P":
            check_enemy(P)
            fight(P)
            check_items(P)
            chooseRoom()
        elif char1.position == "Q":
            check_enemy(Q)
            fight(Q)
            check_items(Q)
            chooseRoom()
        elif char1.position == "R":
            check_enemy(R)
            fight(R)
            check_items(R)
            chooseRoom()
        elif char1.position == "S":
            check_enemy(S)
            fight(S)
            check_items(S)
            chooseRoom()
        elif char1.position == "T":
            check_enemy(T)
            fight(T)
            check_items(T)
            chooseRoom()
        elif char1.position == "U":
            check_enemy(U)
            fight(U)
            check_items(U)
            chooseRoom()
        elif char1.position == "V":
            check_enemy(V)
            fight(V)
            check_items(V)
            chooseRoom()
        elif char1.position == "W":
            check_enemy(W)
            fight(W)
            check_items(W)
            chooseRoom()
        elif char1.position == "X":
            check_enemy(X)
            fight(X)
            check_items(X)
            chooseRoom()
        elif char1.position == "Y":
            check_enemy(Y)
            fight(Y)
            check_items(Y)
            chooseRoom()
        elif char1.position == "Z":
            check_enemy(Z)
            fight(Z)    
            check_items(Z)
            pushButton()
            chooseRoom()
        elif char1.position == "Entry":
            check_enemy(Entry)
            fight(Entry)
            check_items(Entry)
            chooseRoom()
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

    print("You are currently in the " + char1.position + ". You can see two doors with an A and a B on it. Which one do you want to open? (A / B)")

    #Schleife muss überarbeitet werden, um die Räume nach und nach zu prüfen. 
    while char1.health > 0:

        loop_rooms()

    #Eine neue Funktion muss gebaut werden, um die Position des Characters mit dem jeweiligen Raum zu verbinden. Link für eine Möglichkeit wurde abgespeichert. 