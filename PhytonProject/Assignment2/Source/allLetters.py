## This program is to find if all alphabets are present in the string

inputString = input("Enter the statement:")

alphabetsListCap="A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
allLetters=True;
for alphabet in alphabetsListCap.split(","):
    if(alphabet not in inputString and alphabet.lower() not in inputString):
        allLetters = False
        break
if allLetters:
    print("All alphabets are present in the statement.")
else:
    print("All alphabets are not present in the statement.")
