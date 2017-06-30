# This program sorts tuple in increasing order
import operator
new_list = [(1, 6), (1, 7), (4, 5), (2, 2), (1, 3)]

#function to validate if input is list
def validate(lst):
    if isinstance(lst,list):
        return True
    else:
        return False

if(validate(new_list)):
    #sorting using lambda
    print(sorted(new_list,key=lambda x:(x[1],-x[0])))
    #sorting using operator
    new_list.sort(key = operator.itemgetter(1))
    print(new_list)
else:
    print("Input is not list")


