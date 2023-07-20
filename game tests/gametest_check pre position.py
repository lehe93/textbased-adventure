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
        self.prepos = []
        
        if self.exp >= 500:
            self.level += 1
            self.attack += 1
            self.defense += 1
            self.health += 5 
            self.exp = 0

class room:
    def __init__(self, name, items, monster, dl1, dl2, pre_dl):
        self.name = name
        self.monster = monster
        self.items = items
        self.dl1 = dl1
        self.dl2 = dl2
        self.pre_dl = pre_dl


Entry = room("Entry", "none", "none", "A", "B", "none")
A = room("A", "none", "book zombie", "C", "D", "Entry")
B = room("B", "red potion", "none", "E", "F", "Entry")


char1 = character("Jasper")


#Testdatei, um die Liste für die vorherigen Charakterpositionen zu prüfen. 

print(" \nGreat! Your character goes by the name " + char1.name + ". \n")
print("I wish you all the luck while you are discovering the mysterious 'Lettered Dungeon'. \n")

print("\nYou are " + char1.name + ", a courageous pathfinder and hero. Your newest quest leads you to the mysterious 'Lettered Dungeon', where monsters terrorize near villages.")
print("The infamous Dungeon awaits you with a large black entry. Fierceless as you are, you are lighting up a torch and take the first steps into the cave. \n")
print("You enter the first room and you hear the sound of a boulder blocking the entrance. You sigh, since you have to find a way out of this dungeon. ") 
print("In the left you see another door as well as on the right side. Which do you want to take?")
print("You can either choose door 'A' or door 'B'.")

counter_entry = 0

while counter_entry < 1:
    entry_room = input()
    for x in entry_room:
        if x == "A":
            print("You open the left door with a big 'A' on it.")
            char1.position = A
            char1.prepos.append(char1.position.pre_dl)
            counter_entry += 1
        elif x == "B":
            print("You open the right door with a big 'B' on it.")
            char1.position= B
            char1.prepos.append(char1.position.pre_dl)
            counter_entry += 1 
        else: 
            print("Please choose between 'A' and 'B'.")

char1.prepos.append("A")
char1.prepos.append("B")

print(char1.prepos)

print(char1.prepos[-1:])