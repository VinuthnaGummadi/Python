number=int(input("Enter number"))
reverse = 0
while(number!=0):
    remainder = number % 10
    number = number // 10
    reverse = (reverse * 10) + remainder

print(reverse)