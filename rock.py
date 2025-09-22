import random

def getChoices():
    options = ["rock", "paper", "scissors"]

    player_choice = input("Enter a choice (rock, paper, scissors): ")
    computer_choice = random.choice(options)

    choices = {
    "player": player_choice,
    "computer": computer_choice
    }

    return choices

def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")

    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scisors! You win!"
        else:
            return "Paper covers rock, you lose :("
    elif player == "paper": 
        if computer == "rock":
            return "Paper covers rock, you win!"
        else:
            return "Scissors cut paper, you lose :("
    elif player == "scissors": 
        if computer == "rock":
            return "Rock smashes scisors!, you lose :("
        else:
            return "Scissors cuts paper, you win!"
    
choices = getChoices()
result = check_win(choices["player"], choices["computer"])
print(result)


