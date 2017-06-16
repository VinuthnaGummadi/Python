# This program is to guess the randomly generated number
from random import randint

# Generate random Integer between 0 and 9
number = randint(0,9)

# Infinite loop exits when user guesses the number right
while True:
    guess = input("Guess Digit:")

    # Check if guess if not empty
    if(guess!=""):
        # Exception block if the entered guess is not Integer
        try:
            guess=int(guess)
            if(guess>=0 and guess<=9):
                if(guess==number):
                    print("Your answer is PERFECT!! Congratulations!!")
                    break
                elif(guess<number):
                    print("Your answer is high than required")
                elif(guess>number):
                    print("Your answer is low than required")
            else:
                print("Enter between 0 and 9")

        except ValueError:
            print("Enter Integer value.")
    else:
        print("Enter Integer value.")