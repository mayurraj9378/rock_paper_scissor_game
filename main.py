import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor): ")
    options = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def win_choice(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissor') or \
            (player_choice == 'paper' and computer_choice == 'rock') or \
            (player_choice == 'scissor' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Get player and computer choices
choices = get_choices()

# Determine the winner
result = win_choice(choices["player"], choices["computer"])

# Print the result
print(result)
