from random import *

#A function to compare the weapons to decide the winner of that round.
def compareWeapons(comp_w, user_w, weapons, winning_weapons):
    if comp_w == user_w:
        print("tie - no one wins")
        return 0
    else:
        # find the index of comp_w
        for idx_comp in range(len(weapons)):
            if weapons[idx_comp] == comp_w:
                break
        # find the index of user_w
        for idx_user in range(len(weapons)):
            if winning_weapons[idx_user] == user_w:
                break
        # if those indices are the same --> user wins
        if idx_comp == idx_user:
            print(user_w, "beats", comp_w, "- user wins")
            return 1
        else:
            print(comp_w, "beats", user_w, "- computer wins")
            return 2
        

# main part

#Two lists, first one is the regular list to choose the weapon from and the second one is to make the comparison in order to decide on the winner.
weapons = ["rock", "paper", "scissors"]
winning_weapons = ["paper", "scissors", "rock"]

#Scores
user_count = 0
comp_count = 0

#So-called, "Game loop"
while user_count != 3 and comp_count != 3:
    #Choose the weapon of computer randomly.
    comp_w = weapons[randint(0,2)]
    #Users chooses a weapon until a valid input is entered.
    user_w = input("Please enter your weapon: ")
    while user_w not in weapons:
        user_w = input("Please enter your weapon: ")

    # 0: tie, 1: user, 2: comp
    winner = compareWeapons(comp_w, user_w, weapons, winning_weapons)
    if winner == 1:
        user_count += 1
    elif winner == 2:
        comp_count += 1

# The last score is printed after the game is over i.e one of the players has reached 3 in terms of score.
print("User won", user_count, "time(s) and computer won", comp_count, "time(s)")

#Winner is decided by comparing the last scores of either side.
if user_count == 3:
    print("User has won the game!")
else:
    print("Computer has won the game!")
