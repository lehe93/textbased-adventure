# Erster Versuch die Wiederbesichtigung von Räumen mit einer eigenen Play-Funktion zu lösen. 
# Es müsste auch über stark verschachtelte if-else-Anweisungen gehen können. 
# Im nächsten Schritt sollte für die ersten drei Räume (A C und D) ein Plan aufgezeichnet werden
# Was soll passieren, wenn der Charakter den jeweiligen Raum das erste mal betritt? 
# Check-Abläufe, ob z.B. Monster besiegt sind, oder Waffen auf dem Boden liegen. 

class room:
    def __init__(self, name, monster, items):
        self.name = name
        self.monster = monster
        self.items = items

A = room("A", "none", "none")
B = room("B", "book zombie", "none")
C = room("C", "none", "red potion")


#Einbauen einer permanenten Schleife, um Räume B und C durchzutesten. 

x = 0
while x < 1:
    select = 0

    print("Welcome to room A")
    print("You see two doors to room B and room C. Which one do you want to open? (B / C)")

    while select < 1:
        answer = input()
        if answer == "B":
            print("You open the door to room B.")
            if B.monster == "book zombie":
                print("A book zombie is attacking you as you enter the new room.")
                print("Do you want to attack it? (yes / no)")
                B_select = 0
                while B_select < 1:
                    B_fight = input()
                    if B_fight == "yes":
                        print("You attack the book zombie and kill it with your sword.")
                        B.monster = "none"
                        B_select += 1
                    elif B_fight == "no":
                        print("You make haste and run back to room A.")
                        B_select += 1
                    else: 
                        print("Please enter a valid response. (yes / no)")

            elif B.monster =="none":
                print("You enter the new room and see the remnants of a book zombie on the ground.")

        elif answer == "C":
            print("You open the door to room C")
            if C.items == "red potion":
                print("you see a table with a red potion on it. Do you want to drink it? (yes / no)")
                C_select = 0
                while C_select < 1:
                    c_input = input()
                    if c_input == "yes":
                        print("You dring the flask and feel the energy of life going through your veins.")
                        print("You get + 2 Hitpoints.")
                        C.items = "none"
                        C_select += 1
                    elif c_input == "no":
                        print("You don't trust the shiny red flask and let it where it is. ")
                        C_select += 1
                    else: 
                        print("Please enter a valid response. (yes / no)")
                select += 1
            elif C.items == "none":
                print("you see a table with an empty flask on it and remember the refreshening liquid. ")

            