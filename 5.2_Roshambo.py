'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random
win = 0
games = 0
play = True

print("Welcome to the most epicest game of rock paper scissors ever.")
print("The rules are simple, choose 1 for rock, 2 for paper, and 3 for scissors.")

while play:
    plymv = int(input("\nWhat is your move?\n")) ## 1 = Rock, 2 = Paper, 3 = Scissors 1>3>2>1
    cpumv = random.randint(1,3)
    if plymv == 1:
        print("You played rock")
    elif plymv == 2:
        print("You played paper")
    elif plymv == 3:
        print("You played scissors")
    else:
        print("invalid move, try again")
        continue
    if cpumv == 1:
        print("The cpu chose rock")
    elif cpumv == 2:
        print("The cpu chose paper")
    elif cpumv == 3:
        print("The cpu chose scissors")

    if plymv == 1 and cpumv == 2 or plymv == 2 and cpumv == 3 or plymv == 3 and cpumv == 1:
        print("\nThe computer wins!\n")
        games += 1
    elif plymv == 1 and cpumv == 3 or plymv == 2 and cpumv == 1 or plymv == 3 and cpumv == 2:
        print("\nYou win!\n")
        games += 1
        win += 1
    else:
        print("\nYou tied! Try again!\n")
        continue
    print("1. Play again")
    print("2. Stop playing\n")
    plyagn = int(input("What do you want to do?"))
    if plyagn == 1:
        play = True
    elif plyagn == 2:
        play = False
    else:
        print("Invalid command, quitting game")
        play = False
print("You won", win, "out of", games, "games!")
print("that's a win rate of", (win/games)*100, "%")








