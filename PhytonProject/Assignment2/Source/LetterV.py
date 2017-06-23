## Program to print letter V with *
letter="";
## taking row range of 5
for row in range(0,5):
    ## taking column range of 7
    for column in range(0,7):
        ## logic to print the *
        if (((column == 1 or column == 5) and row < 3)
            or (row == 4 and column == 3)
            or (row == 3 and (column == 2 or column == 4))):
            letter=letter+"*"
        else:
            letter=letter+" "
    letter=letter+"\n"
print(letter);