inputStr = input("Enter string:")

strArr=[]
countArr=[]
for strn in inputStr:
    if(strn not in strArr):
        strArr.append(strn)
        countArr.append(1)
    else:
        index = strArr.index(strn)
        countArr[index] = countArr[index]+1
print("Character frequency in given string is : \n")
count = 0;
for val in strArr:
    print( "%s : %d" %(val,countArr[count]))
    count = count + 1
