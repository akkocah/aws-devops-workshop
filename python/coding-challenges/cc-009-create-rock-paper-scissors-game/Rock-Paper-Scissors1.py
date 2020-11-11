from random import randint
from termcolor import colored, cprint
print("Let's start the game")
lst = ['rock', 'paper', 'scissors']
computer_score = 0
user_score = 0
while True:
    if computer_score == 3 or user_score == 3:
        break
    computer = lst[randint(0,2)]
    user = input("Please enter your weapon (Rock, Paper, Scissors):  ").lower()
    if computer == user:
        print("tie - no one wins")
    elif user == "rock":
        if computer == "paper":
            print("paper beats rock - computer wins")
            computer_score += 1
        else:
            print("rock beats scissors - user wins")
            user_score += 1
    elif user == "paper":
        if computer == "scissors":
            print("scissors beats paper - computer wins")
            computer_score += 1
        else:
            print("paper beats rock - user wins")
            user_score += 1
    elif user == "scissors":
        if computer == "rock":
            print("rock beats scissors - computer wins")
            computer_score += 1
        else:
            print("scissors beats paper - user wins")
            user_score += 1
    else:
            print("That's not a valid input.")
print(f"\nUser won {user_score} time(s) and computer won {computer_score} time(s)")
if computer_score == 3:
    print("\nand the winner is ")
    winsound.Beep(99, 9999)
    cprint('\nComputer has won the game!', 'red', attrs=['blink'])
else:
    print("\nand the winner is ")
    winsound.Beep(99, 9999)
    cprint('\nUser has won the game!', 'red', attrs=['blink'])