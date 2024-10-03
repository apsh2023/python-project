import random

class RockScissorspaper:
    def __init__(self):
        self.choices = ['rock', 'scissors', 'paper']
            def computer_choice(self):
        return random.choice(self.choices)
            def determine_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "tie"
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'scissors' and computer_choice == 'paper') or \
             (player_choice == 'paper' and computer_choice == 'rock'):
            return "player"
        else:
            return "computer"

