'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''
'''
Set up variables, then reference back to those variables based on user imput, have reactions based on that
'''
game = True
while game:
    thrst = 0
    drnklft = 2
    dstnce = 0
    speed = 0
    trd = 0
    wins = 0
    playing = True

    while playing:
        print("\n1. Take a drink\n2. Moderate Speed\n3. Full Speed\n4. Full Stop\n5. Status\n6. Quit\n")
        qstn = int(input("What do you want to do? "))
        if qstn == 1:
            thrst = 0
            print("You have taken a drink from your bottle.")
            drnklft -= 1
            print("You have", drnklft, "drinks left in your bottle.")
            continue
        elif qstn == 2:
            speed = 1
            print("You start moving at moderate speed for the day.")
        elif qstn == 3:
            speed = 2
            print("You start moving at full speed for the day.")
        elif qstn == 4:
            speed = 0
            print("You stop for the day.")
            trd = 0
            print("You are fully rested for the next day")
        elif qstn == 5:
            print("\nCurrent speed:", speed, "\nDistance to destination:", 10-dstnce, "\nThirst:", thrst, "\nDrinks left::",
                  drnklft, "\nTiredness:", trd)
            continue
        elif qstn == 6:
            playing = False
            game = False
            continue
        else:
            print("Invalid command")
        ## something to create situations
        thrst += 1
        trd += 1
        dstnce += speed

        if thrst >= 3:
            ans = input("You died of dehydration. Try again? Y or N")
            if ans.lower() == "y":
                continue
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
        elif trd >= 4:
            print("You fell asleep on the journey. You walked right into a ____")
            ans = print("You died. Try again? Y or N")
            if ans.lower() == "y":
                continue
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
        if dstnce == 10:
            print("You got to the destination, congrats!")
            wins += 1
            print("Would you like to go for", wins + 1, "in a row?")
            ans = input("Y or N")
            if ans.lower() == "y":
                continue
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