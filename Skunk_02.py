# Chris watters
# Skunk Ver02
import random


class SkunkGame:
    def __init__(self):
        """ A class that represents a game of Skunk.

     Rules:
    - The game is played with two dice.
    - On each turn, the player rolls the dice and adds the values.
    - If a 1 is rolled on either die, the player's turn is over and the round score is reset to 0.
    - If two 1s are rolled, the player's turn is over and their total score is reset to 0.
    - If the two dice show the same non-1 value, the player's round score is increased by 100.
    - If the player's round score reaches 20 or more, they can choose to hold and add the round score to their total score.
    - The game continues until one player reaches a score of 1000 or more, or the human player reaches a score of 300 or more
      and has a higher score than the computer player.

        """
        self.human_score = 0
        self.computer_score = 0
        self.current_round_score = 0
        self.current_player = "human"

    def roll_dice(self):
        """Initializes a new instance of the SkunkGame class

        :return:None
        """
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        return die1, die2

    def play_game(self):
        """Plays a game of Skunk

        :return:None
        """
        while True:
            # Display current scores, round score, and current player.
            print("=" * 30)
            print(f"Current scores: Human - {self.human_score}, Computer - {'???'}")
            print(f"Current round score: {self.current_round_score}")
            print(f"It's {self.current_player}'s turn.")

             #Handle human player's turn.
            if self.current_player == "human":
                user_input = input("Press enter to roll dice, or Q to quit: ")
                if user_input.lower() == "q":
                    print("Quitting game.")
                    break
                die1, die2 = self.roll_dice()
                print(f"You rolled: {die1}, {die2}")

                # Handle different outcomes of rolling the dice.
                if die1 == 1 or die2 == 1:
                    print("Skunk! Round score reset to 0.")
                    self.current_round_score = 0
                    self.current_player = "computer"
                elif die1 == die2 == 1:
                    print("Double skunk! You lose the game.")
                    self.human_score = 0
                    break
                elif die1 == die2:
                    print("Doubles! Adding 100 points to round score.")
                    self.current_round_score += 100
                else:
                    self.current_round_score += die1 + die2
                    print(f"Round score is now {self.current_round_score}")

                # Handle decision to hold or roll again.
                if self.current_round_score >= 20:
                    user_input = input("Press enter to hold, or R to roll again: ")
                    if user_input.lower() == "r":
                        continue
                    else:
                        self.human_score += self.current_round_score
                        self.current_round_score = 0
                        self.current_player = "computer"

            # Handle computer player's turn.
            else:
                die1, die2 = self.roll_dice()
                print(f"Computer rolls: {die1}, {die2}")
                # Handle different outcomes of rolling the dice.
                if die1 == 1 or die2 == 1:
                    print("Computer skunked! Round score reset to 0.")
                    self.current_round_score = 0
                    self.current_player = "human"
                elif die1 == die2 == 1:
                    print("Computer double skunked! You win the game.")
                    self.computer_score = 0
                    break
                elif die1 == die2:
                    print("Computer gets doubles! Adding 100 points to round score.")
                    self.current_round_score += 100
                else:
                    self.current_round_score += die1 + die2
                    if self.current_round_score >= 20:
                        self.computer_score += self.current_round_score
                        print(f"Computer holds. Round score of {self.current_round_score} added to score.")
                        self.current_round_score = 0
                        self.current_player = "human"
            # Check if either player has won
            if self.human_score >= 300 and self.human_score > self.computer_score:
                print(f"You win! Final score: Human - {self.human_score}, Computer - {self.computer_score}")
                break
            elif self.computer_score >= 1000 and self.computer_score > self.human_score:
                print(f"Computer wins. Final score:")


def main():

    game = SkunkGame()
    game.play_game()


if __name__ == '__main__':
    main()
