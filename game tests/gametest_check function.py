#Funktion, um beim Betreten eines Raumes zu prüfen, ob Gegner o.ä. anwesend sind. 

class room:
    def __init__(self, name, monster, items):
        self.name = name
        self.monster = monster
        self.items = items

A = room("A", "none", "none")
B = room("B", "book zombie", "none")
C = room("C", "none", "red potion")

print("You are in Room A. Do you want to enter room B or room C? (B / C)")

def check_enemy(user_answer):
    if user_answer == "C":
        if C.monster == "none":
            print("There is no enemy in the room.")
        elif C.monster != "none":
            print("As you enter the room, you are attacked by a " + C.monster + ".")
    elif user_answer == "B":
        if B.monster == "none":
            print("There is no enemy in the room.")
        elif B.monster != "none":
            print("As you enter the room, you are attacked by a " + B.monster + ".")
            print("You fight the enemy until it is dead. ")
            B.monster = "none"

#Testlauf für check_enemy
asd = input()
check_enemy(asd)


#Ausgabe gefixt. user_answer ist ein string, aber es soll das 
#Objekt-Äquivalent ("B" --> B) geprüft werden. 

def check_items(item_input):
    if item_input == "check items":
        if A.items == "none":
            print("There are no items on the floor.")
        elif A.items != "none":
            print("As you observe the room for some loot, you find a " + A.items + ".")
            print("Do you want to take it? (Y / N)")
            select_counter = 0

            while select_counter < 1:
                choice = input()
                if choice == "Y":
                    print("You take the " + A.items + " with you.")
                    select_counter += 1
                    A.items = "none"
                elif choice == "N":
                    print("You let the " + A.items + "in the room.")
                    select_counter += 1
                else:
                    print("Please enter a valid response.")



deg = input()
check_items(deg)