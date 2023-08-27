import itertools

class room:
    def __init__(self, name, items, monster, dl1, dl2, pre_dl):
        self.name = name
        self.monster = monster
        self.items = items
        self.dl1 = dl1
        self.dl2 = dl2
        self.pre_dl = pre_dl

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
Z = room("Z", "none", "Ink Vampire", "none", "none", "Y")



#Reminder: Dictionairies haben stets einen Key zu dem ein Value gehört: z.B. Key "A" mit Value A. 

room_dict = {"A": A.name, "B": B.name, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H, "I": I, "J": J, "K": K, "L": L, "M": M, "N": N, "O": O, "P": P, "Q": Q, "R": R,
             "S": S, "T": T, "U": U, "V": V, "W": W, "X": X, "Y": Y, "Z": Z}

def iter_room():
    i = input()
    if i in room_dict:
        print(room_dict[str(i)])
    else:
        print("Your Answer is not available.")

print("Please enter a tall letter.")
iter_room()

