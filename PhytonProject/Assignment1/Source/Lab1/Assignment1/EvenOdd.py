# This program displays if the entered number is even or odd
#Take input from user
num = input("Enter Number:")

#Check number entered is null
if(num!=""):
    #Exception handler if entered number is not Integer
    try:
        number=int(num)
        # if entered number is divisible by 2 then it is even else it is odd
        if (number % 2 == 0):
            print("Entered number is even number.")
        else:
            print("Entered number is odd number.")
    except ValueError:
        print("Enter Integer value.")
else:
    print("Enter Integer value.")