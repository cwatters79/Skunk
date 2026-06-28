# Skunk
Skunk  is a Python command-line dice game where a human player competes against the computer. The goal is to reach the winning score before the opponent.

Game Rules
The game uses two six-sided dice.
If no 1s are rolled, the dice total is added to the round score.
If one die rolls a 1, the player loses their round score and their turn ends.
If both dice roll 1, it is a double skunk and the player’s total score is reset.
If doubles are rolled, except double 1s, 100 points are added to the round score.
The human player may hold once the round score reaches 20 or more.
The computer holds automatically when its round score reaches 20 or more.
The human player wins by reaching 300 or more points while ahead of the computer.
The computer wins by reaching 1000 or more points while ahead of the human player.
Features
Object-oriented design using a SkunkGame class
Random dice rolls using Python’s random module
Human and computer turns
Score tracking
Round score tracking
Skunk and double-skunk rules
Quit option for the human player
