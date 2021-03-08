"""
Rock Papper Sccissor
_________________________________________
"""

import random
import os
import re

from click._compat import raw_input

os.system('cls' if os.name=='nt' else 'clear')
while(1<2):
    print("Rock, Papper, Scissors - Shoot!")
    userChoice = raw_input("Make your choice [R]ock, [P]apper, [S]cissors: ")
    if not re.match("[SsRrPp]",userChoice):
        print("Pleae choose a letter: ")
        print("[R]ock, [S]cissors or [P]apper.")
        continue

    #Echo the user's choice
    print("You choose :", userChoice)
    choices = ['R','S','P']
    opponentChoice = random.choice(choices)
    print("I choose :", opponentChoice)
    if opponentChoice == str.upper(userChoice):
        print("-- It's a Tie! --")
    elif opponentChoice=='R' and userChoice=='S':
        print("Rock beats Scissors, I win! ")
        continue
    elif opponentChoice=='S' and userChoice=='P':
        print("Scissors beats Papper, I win! ")
        continue
    elif opponentChoice=='P' and userChoice=='R':
        print("Papper beats Rock, I win! ")
        continue
    else:
        print("You win!")