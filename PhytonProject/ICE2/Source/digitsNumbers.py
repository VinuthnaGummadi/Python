word = input("Enter the word to find number of digits and albhabets")

alfaCount=0
digitCount=0
for c in word:
    if(c.isalpha()):
        alfaCount = alfaCount +1
    elif(c.isdigit()):
        digitCount = digitCount +1

print("Number of alphabets:%d \n"%alfaCount)
print("Number of digits:%d"%digitCount)