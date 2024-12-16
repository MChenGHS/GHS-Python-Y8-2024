import random
options = ["rock", "paper", "scissor"]
computer_choice = random.choice(options)
player_choice = input("Choose rock, paper or scissor: ")
winner = ""
if computer_choice == "rock" and player_choice == "rock":
    winner = "none"
elif computer_choice == "rock" and player_choice == "paper":
    winner = "player"
elif computer_choice == "rock" and player_choice == "scissor":
    winner = "computer"
elif computer_choice == "paper" and player_choice == "rock":
    winner = "computer"
elif computer_choice == "paper" and player_choice == "paper":
    winner = "none"
elif computer_choice == "paper" and player_choice == "scissor":
    winner = "player"
elif computer_choice == "scissor" and player_choice == "rock":
    winner = "player"
elif computer_choice == "scissor" and player_choice == "paper":
    winner = "computer"
elif computer_choice == "scissor" and player_choice == "scissor":
    winner = "none"

print("The winner is ", winner)