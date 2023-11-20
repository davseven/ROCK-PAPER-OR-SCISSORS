#ROCK PAPER SCISSORS (piedra, papel o tijéra en Inglés)
print ("Do you dare to play ROCK PAPER SCISSORS against THE MATRIX?")

import random

options = ("rock", "paper", "scissors")
playing = True

while playing: 
    player1 = 0 
    matrix = random.choice (options)

    while player1 not in options:
        player1 = input ("Enter a choice: (rock, paper, scissors): ")

    print (f"Player1: {player1}")
    print (f"The Matrix: {matrix} ")

    if player1 == matrix:
        print ("IT'S A TIE!")
    elif player1 == "rock" and matrix == "scissors":
        print ('YOU WIN!')
    elif player1 == 'paper' and matrix == "rock":
        print ('YOU WIN!')
    elif player1 == 'scissors' and matrix == "paper":
        print ('YOU WIN!')
    else:
        print ("YOU LOSE!")
    if not input ('Play again? (y/n): ').lower () == 'y':
        playing = False
print ("Thanks for playing! Hope you had fun!")
