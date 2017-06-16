# This program displays the perimeter of a rectangle
#Take input from user
length = input("Enter Length:")
breadth = input("Enter Breadth:")
perimeter = 0
# Check if entered values are not null
if(length!="" and breadth!=""):
    # Exception if entered value if not int.
    # This block is executed when the entered number is Integer
    try:
        length=int(length)
        breadth=int(breadth)
        perimeter = 2*(length + breadth)
        print("Perimeter of Rectangle is:"+str(perimeter))
    except ValueError:
        pass
        # Exception if entered value if not float
        # This block is executed if the entered number is not an Integer and is Float value
        try:
            length=float(length)
            breadth = float(breadth)
            perimeter = round(2*(length + breadth),2)

            print("Perimeter of Rectangle is:" + str(perimeter))
        except ValueError:
            print("Enter Integer or Float value.")
else:
    print("Enter Integer or Float value.")