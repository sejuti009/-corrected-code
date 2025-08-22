# import necessary modules
import random
import time

# pick a number between 1 to 100
number = random.randint(1, 100)
name = 0

def intro():
    print("May I ask your name please?")
    # declaring name varriable golbal so it can be accessed outside the function gobal name
    global name
    name = input() # ask for the name
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 100")
    if (number %2 == 0):
        x = 'even'
    else:
        x = 'odd'
    print("\nThis is and {} number".format(x))
    time.sleep(.5)
    print("Go ahead. Guess!")

def pick():
    guesstaken = 0

    # if the number of guesses is less then 6
    while guesstaken < 6:
        time.sleep(.25)
        # insert the place to enter guess
        enter = input("Guess : ")

        # check if a number was entered 
        try:

            # stores the guess as an integer instead of a string
            guess = int(enter)
            if guess <= 100 and guess>=1: # if they are in range
                guesstaken += 1
                # add one guess each time the player is wrong
                if guesstaken < 6:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    if guess > number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(.5)
                        print("Try Again mate!")

            # if the guess is right, then we are going to jump out of the while block
            if guess == number:
                    break
            if guess > 100 or guess < 1:
                print("Silly guess! That number isn't in the range!")

                time.sleep(.25) 
                print("Please enter a number between 1 and 100")

        except:
            print("I don't think that "+enter+" is a number. Sorry")

    if guess == number:
        guesstaken = str(guesstaken)            
        print("Good job, {}! You have guesses my number in {} guesses!".format(name, guesstaken))
        
    if guess != number:
        print("Nope, the number I was thinking was" + str(number)) 

playagain="yes"
while playagain == "yes" or playagain == "y" or playagain == "Yes" or playagain == "YES":
        intro()
        pick()
        print("DO you want to play again?")
        playagain=input()
