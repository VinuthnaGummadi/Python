def main():
    fileName = input("Enter file name:")

    fileRead = open(fileName,'r')

    line = fileRead.readline()
    sum = 0
    count = 0
    while line != "":
        for str in line.split(","):
            sum = sum + eval(str)
            count = count+1
        line = fileRead.readline()
    print("\nThe average of numbers is",sum/count)

main()