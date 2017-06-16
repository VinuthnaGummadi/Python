number = int(input("Enter the count of words to find longest word"))

count =0
longWord = ""
while number!=0:
    word = input("Enter word %d :"%(number))
    count1 = len(word)
    if(count1>count):
        count = count1
        longWord = word
    number = number -1
print("longest word is:%s"%(longWord))

