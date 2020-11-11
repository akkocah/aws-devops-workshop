import random
comp_score= 0
user_score= 0
while True:   
    weapons=("Rock", "Paper", "Scissors")
    comp_weapon= random.choice(weapons)
    user_weapon= input("Please select weapon and write: Rock, Paper and Scissors: \n").strip().capitalize()


    if user_weapon == "Rock" and comp_weapon== "Scissors" or\
        user_weapon == "Scissors" and comp_weapon== "Paper" or\
        user_weapon == "Paper" and comp_weapon == "Rock":
        user_score += 1
        print (f"{user_weapon} beats {comp_weapon} - User wins")
        print(f"User score: {user_score} Computer score: {comp_score}")
        
    elif comp_weapon == "Rock" and user_weapon== "Scissors" or\
        comp_weapon == "Scissors" and user_weapon== "Paper" or\
        comp_weapon == "Paper" and user_weapon == "Rock":
        comp_score += 1
        print (f"{comp_weapon} beats {user_weapon} - Computer wins")
        print(f"User score: {user_score} Computer score: {comp_score}")
        
    elif comp_weapon == user_weapon:
        print(f"{user_weapon} and {comp_weapon} tie- no one wins")
        print(f"User score: {user_score} Computer score: {comp_score}")
        
    if user_score == 3 or comp_score== 3:
        if user_score == 3:
            print(f"User won {user_score} time(s) and Computer won {comp_score} time(s)\nUser has won the game! Good Bye...")
        else:
            print(f"User won {user_score} time(s) and Computer won {comp_score} time(s)\nComputer has won the game! Good Bye...")
        break
        
