#Rock, Paper, Scissors Game
print("WELCOME TO THE GAME OF ROCK, PAPER,  SCISSORS")
import random

#moves for the player
moves = ["'R'  for Rock, 'P' for Paper, 'S' for Scissors"]

while True:
    computer = random.choice(["rock", "paper", "scissors"])
    player = input("What's your choice? 'R'  for Rock, 'P' for Paper, 'S' for Scissors (or end the game)").lower()
    if player == "end the game":
        print("The game is ended.")
        break
    elif player == computer:
        print("It is a Tie!{user}", player,"{CPU}", computer)
    elif player == "rock":
        if computer == "scissors":
            print("You win! {user}", player, "beats {CPU}", computer)
        else:
             print("You lose! {CPU}", computer, "beats {user}", player)
    elif player == "paper":
        if computer == "scissors":
            print("You lose! {CPU}", computer, "beats {user}", player)
        else:
            print("You win! {user}", player, "beats {CPU}", computer)
    elif player == "scissors":
        if computer == "paper":
            print("You win! {user}", player, "beats {CPU}", computer)
        else:
            print("You lose! {CPU}", computer, "beats {user}", player)
    




        
        
        
            
              
