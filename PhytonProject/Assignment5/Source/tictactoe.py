## tictac toe game

class TictacToe():
    def __init__(self):
        self.size = 3
        w, h = self.size, self.size;
        TictacToe.Matrix = [[0 for x in range(w)] for y in range(h)]

    #prints horizontal line
    def print_horiz_line(self):
        print("--- ", sep=' ', end='', flush=True)

    #prints vertical line
    def print_vert_line(self):
        print("|  ", sep=' ', end='', flush=True)

    #prints vertical line with value
    def print_vert_lineValue(self,value):
        print("| "+value, sep=' ', end='', flush=True)

    #computes the cordinates and places the values in that coordinate
    def takeInputX(self):
        while(True):
            coord = input("Enter which coordinate you want to place:\n")
            valueXx=int(coord.split(",")[0])
            valueXy=int(coord.split(",")[1])
            if(self.checkCell(valueXx,valueXy)):
                self.Matrix[valueXx][valueXy]="X"
                self.printMatrix()
                break
            else:
                print("Cell is full, enter other coordinates:\n")
    #computes the cordinates and places the values in that coordinate
    def takeInputO(self):
        while(True):
            coord = input("Enter which coordinate you want to place:\n")
            valueOx=int(coord.split(",")[0])
            valueOy=int(coord.split(",")[1])
            if(self.checkCell(valueOx,valueOy)):
                self.Matrix[valueOx][valueOy]="O"
                self.printMatrix()
                break
            else:
                print("Cell is full, enter other coordinates:\n")

    #check if cell is empty or not
    def checkCell(self,valueXx,valueXy):
        if(TictacToe.Matrix[valueXx][valueXy]!='X' and TictacToe.Matrix[valueXx][valueXy]!='O'):
            return True
        else:
            return False

    #print the matrix
    def printMatrix(self):
        rowCount=0
        for row in TictacToe.Matrix:
            print("")
            for horiz in range(self.size):
                self.print_horiz_line()
            print("")
            colCount = 0
            for elem in row:
                if(elem!=0):
                    self.print_vert_lineValue(elem)
                else:
                    self.print_vert_line()
                colCount = colCount +1
            rowCount = rowCount +1
        print("")
        for horiz in range(self.size):
            self.print_horiz_line()
        print("\n")

    def checkWinningCondition(self,value):
        if((TictacToe.Matrix[0][0]==value and TictacToe.Matrix[0][1]==value and TictacToe.Matrix[0][2]==value) or
               (TictacToe.Matrix[1][0] == value and TictacToe.Matrix[1][1] == value and TictacToe.Matrix[1][
                   2] == value) or
               (TictacToe.Matrix[2][0] == value and TictacToe.Matrix[2][1] == value and TictacToe.Matrix[2][
                   2] == value) or
               (TictacToe.Matrix[0][0] == value and TictacToe.Matrix[1][0] == value and TictacToe.Matrix[2][
                   0] == value) or
               (TictacToe.Matrix[0][1] == value and TictacToe.Matrix[1][1] == value and TictacToe.Matrix[2][
                   1] == value) or
               (TictacToe.Matrix[0][1] == value and TictacToe.Matrix[1][1] == value and TictacToe.Matrix[2][
                   1] == value) or
               (TictacToe.Matrix[0][2] == value and TictacToe.Matrix[1][2] == value and TictacToe.Matrix[2][
                   2] == value) or
               (TictacToe.Matrix[0][0] == value and TictacToe.Matrix[1][1] == value and TictacToe.Matrix[2][
                   2] == value)):
            return True
        else:
            return False

    #main method
    def play(self):
        for index in range(self.size):
            print("")
            for horiz in range(self.size):
                self.print_horiz_line()
            print("")
            for vert in range(self.size+1):
                self.print_vert_line()
        print("")
        for horiz in range(self.size):
            self.print_horiz_line()

        print("\n")
        count =1
        while(True):
            if(count%2==0):

                if self.checkWinningCondition("X"):
                    if count % 2 == 0:
                        print("Congratulations X, you won the game! ")
                    else:
                        print("Congratulations O, you won the game! ")
                    break
                self.takeInputO()
            else:
                if self.checkWinningCondition("O"):
                    if count % 2 == 0:
                        print("Congratulations X, you won the game! ")
                    else:
                        print("Congratulations O, you won the game! ")
                    break
                self.takeInputX()
            count = count +1

tictactoe = TictacToe()
tictactoe.play()