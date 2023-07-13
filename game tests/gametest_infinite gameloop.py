print("Welcome to the game.")
print("please select, if you want to start the game. (start / leave)")

select_counter = 0

while select_counter < 1: 
    start = input()
    if start == "start":
        print("Have fun playing the game!")
        game_counter = 1
        while game_counter > 0:
            print("Game is on")
            #Spiel startet jetzt

            print("Welcome to the game")
            print("you are in the entry now. Which door do you want to open? A or B?")
            entry_counter = 0
            while entry_counter < 1:
                entry_input = input()
                if entry_input == "A":
                    print("You open the door A.")
                    entry_counter += 1
                elif entry_input =="B":
                    print("You open the door B.")
                    entry_counter += 1
                else: 
                    print("Please enter a valid answer.")
                

    #Spiel wird beendet mit "leave" oder mit select_counter >= 1
    elif start =="leave":
        print("Have a nice day")
        select_counter += 1

    else: 
        print("Please give a possible input. (start / leave)")

