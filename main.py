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

def main():
    game = RockScissorspaper()
    print("Welcome to Rock-Scissors-Paper!")

    while True:
        player_choice = input("Enter your choice (rock, scissors, paper): ").lower()

        if player_choice not in game.choices:
            print("Invalid choice. Please choose 'rock', 'scissors', or 'paper'.")
            continue

        computer_choice = game.computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = game.determine_winner(player_choice, computer_choice)

        if result == "tie":
            print("It's a tie! Try again.")
        elif result == "player":
            print("You win!")
            break
        else:
            print("Computer wins!")
            break

if __name__ == "__main__":
    main()
