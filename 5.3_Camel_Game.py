'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
'''
Set up variables, then reference back to those variables based on user imput, have reactions based on that
'''

print("\nYou see the impostor jump into a vent!")
print("As you dash to the button you see him chasing you!")
print("Make sure you get to it and call a meeting before he catches you.")
print("Since you are a dutiful crewmate you will do tasks as you run to the button, but be careful, do 3 tasks and he "
      "will catch you.")
print("Watch for your hydration and tiredness levels though, you can take a drink or a break if you need.")
print("DO NOT PRESS ENTER WITHOUT PUTTING IN AN ANSER, IT WILL BREAK THE GAME DUMMY")

game = True
wins = 0
while game:
    thrst = 0
    drnklft = 5
    dstnce = 0
    trd = 0
    impdst = 0
    tskrnd = 0
    playing = True
    while playing:
        print("\n1. Take a drink\n2. Move 5 meters\n3. Move 10 meters\n4. Rest\n5. Status\n6. Quit\n")
        qstn = input("What do you want to do? ")
        if qstn == "1":
            if drnklft > 0:
                thrst = 0
                print("You have taken a drink from your bottle.")
                drnklft -= 1
                print("You have", drnklft, "drinks left in your bottle.")
                continue
            else:
                print("You have no more water in your bottle.")
        elif qstn == "2":
            dstnce += 5
            print("You move 5 meters.")
            tskrnd = 0
        elif qstn == "3":
            dstnce += 10
            print("You move 10 meters.")
            tskrnd = 0
        elif qstn == "4":
            speed = 0
            print("You stop for the day.")
            trd = 0
            print("You are fully rested for the next day")
        elif qstn == "5":
            print("\n\033[94mDistance Traveled:", dstnce, "\nDistance to destination:", 75-dstnce, "meters",
                  "\nThirst:", thrst, "/5", "\nDrinks left:", drnklft, "\nTiredness:", trd, "/6\033[0m")
            continue
        elif qstn == "6":
            playing = False
            game = False
            continue
        else:
            print("Invalid command")
            continue
                                                                                            # Situations
        if tskrnd == 0:
            if dstnce == 10:
                print("You came across a wiring panel, the wires were all jumbled up an broke, you stopped for"
                      " a minute to fix them")
                impdst += 1
                tskrnd = 1
            elif dstnce == 25:
                print("As you were walking along, you saw a med bay scanner you needed to use to get on the escape "
                      "pod, you stopped and completed the scan")
                impdst += 1
                tskrnd = 1
            elif dstnce == 40:
                print("You noticed the garbage chute was full, you paused for a moment to empty it")
                impdst += 1
                tskrnd = 1
            elif dstnce == 55:
                print("The door closed on you right as you were about to go through it! You had to swipe your "
                      "card to get through, but the reader is a bit tricky, it took you a few tries.")
                impdst += 1
                tskrnd = 1
            elif dstnce == 65:
                print("Right as you were about to hop in the escape pod, you noticed an astroid field that the pod was "
                      "going to hit. You jumped in the cannon seat and destroyed them.")
                impdst += 1
                tskrnd = 1

                                                                            # End game conditions
        thrst += 1
        trd += 1

        if thrst >= 5:                                                      # Losing conditions
            ans = input("You died of dehydration. Try again? Y or N")
            if ans.lower() == "y":
                break
            elif ans.lower() == "n":
                playing = False
                game = False
                continue
            else:
                print("Invalid Input")
                print("The game will close, if you wish to continue, just restart the program")
                playing = False
                game = False
                continue
        elif trd >= 6:
            print("You fell asleep on the journey. The impostor decided to not kill you, but you were voted off "
                  "anyways. Your team thought you were AFK stratting again")
            ans = input("You died. Try again? Y or N")
            if ans.lower() == "y":
                break
            elif ans.lower() == "n":
                playing = False
                game = False
                continue
            else:
                print("Invalid Input")
                print("The game will close, if you wish to continue, just restart the program")
                playing = False
                game = False
                continue
        elif impdst == 3:
            print("The impostor caught you and beheaded you!")
            print("Better luck next round!")
            ans = input("Play again? Y or N")
            if ans.lower() == "y":
                break
            elif ans.lower() == "n":
                playing = False
                game = False
                continue
            else:
                print("Invalid Input")
                print("The game will close, if you wish to continue, just restart the program")
                playing = False
                game = False
                continue
        if dstnce == 75:                                                    # Winning condition
            print("You got to the button and voted off Ted, I mean the impostor. Congrats!")
            wins += 1
            print("Would you like to go for", wins + 1, "in a row?")
            ans = input("Y or N")
            if ans.lower() == "y":
                break
            elif ans.lower() == "n":
                playing = False
                game = False
                continue
            else:
                print("Invalid Input")
                print("The game will close, if you wish to continue, just restart the program")
                playing = False
                game = False
                continue