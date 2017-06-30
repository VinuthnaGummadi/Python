## tictac toe game
size = int(input("Enter game board size:"))
w, h = size, size;
Matrix = [[0 for x in range(w)] for y in range(h)]

#prints horizontal line
def print_horiz_line():
    print("--- ", sep=' ', end='', flush=True)

#prints vertical line
def print_vert_line():
    print("|  ", sep=' ', end='', flush=True)

#prints vertical line with value
def print_vert_lineValue(value):
    print("| "+value, sep=' ', end='', flush=True)

#computes the cordinates and places the values in that coordinate
def takeInputX():
    while(True):
        coord = input("Enter which coordinate you want to place:\n")
        valueXx=int(coord.split(",")[0])
        valueXy=int(coord.split(",")[1])
        if(checkCell(valueXx,valueXy)):
            Matrix[valueXx][valueXy]="X"
            printMatrix()
            break
        else:
            print("Cell is full, enter other coordinates:\n")

#computes the cordinates and places the values in that coordinate
def takeInputO():
    while(True):
        coord = input("Enter which coordinate you want to place:\n")
        valueOx=int(coord.split(",")[0])
        valueOy=int(coord.split(",")[1])
        if(checkCell(valueOx,valueOy)):
            Matrix[valueOx][valueOy]="O"
            printMatrix()
            break
        else:
            print("Cell is full, enter other coordinates:\n")

#check if cell is empty or not
def checkCell(valueXx,valueXy):
    if(Matrix[valueXx][valueXy]!='X' and Matrix[valueXx][valueXy]!='O'):
        return True
    else:
        return False

#print the matrix
def printMatrix():
    rowCount=0
    for row in Matrix:
        print("")
        for horiz in range(size):
            print_horiz_line()
        print("")
        colCount = 0
        for elem in row:
            if(elem!=0):
                print_vert_lineValue(elem)
            else:
                print_vert_line()
            colCount = colCount +1
        rowCount = rowCount +1
    print("")
    for horiz in range(size):
        print_horiz_line()
    print("\n")

#main method
def main():
    for index in range(size):
        print("")
        for horiz in range(size):
            print_horiz_line()
        print("")
        for vert in range(size+1):
            print_vert_line()
    print("")
    for horiz in range(size):
        print_horiz_line()

    print("\n")
    count =1
    while(True):
        if(count%2==0):
            takeInputO()
        else:
            takeInputX()
        count = count +1
main()