# This program converts each character in the string to a item in list and tuple.
#Take input from user
word = input("Enter a word:")

#Check number entered is null
if(word!=""):
    list_word=[]
    tuple_word=()
    #Exception handler if any exception occurs in converstion
    try:
        for char in word:
            list_word.append(char)
            tuple_word+=(char,)
        print(list_word)
        print(tuple_word)
    except ValueError:
        print("Error Occured")
else:
    print("Enter a word.")