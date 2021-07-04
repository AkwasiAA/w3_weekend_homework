class Game():

    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def single_game(self, player_1, player_2):
        if player_1.choice == "rock" and player_2.choice == "rock":
            return None
        elif player_1.choice == "rock" and player_2.choice == "paper":
            return "Player 2 wins!"
        elif player_1.choice == "rock" and player_2.choice == "scissors":
            return "Player 1 wins!"

        elif player_1.choice == "paper" and player_2.choice == "paper":
            return None
        elif player_1.choice == "paper" and player_2.choice == "rock":
            return "Player 1 wins!"
        elif player_1.choice == "paper" and player_2.choice == "scissors":
            return "Player 2 wins!"

        elif player_1.choice == "scissors" and player_2.choice == "scissors":
            return None
        elif player_1.choice == "scissors" and player_2.choice == "rock":
            return "Player 2 wins!"
        elif player_1.choice == "scissors" and player_2.choice == "paper":
            return "Player 1 wins!"


