#ReplaceDictionary values

#creating dictionaries
dict1 = {}
dict1['course'] = 'python'
dict1['LastGPA'] = 90
dict1['CurrentGPA'] = 80

dict2 = {}
dict2['course'] = 'python'
dict2['LastGPA'] = 95
dict2['CurrentGPA'] = 85

dict3 = {}
dict3['course'] = 'python'
dict3['LastGPA'] = 100
dict3['CurrentGPA'] = 100

#adding dictionaries to a list
listdict = [dict1,dict2,dict3]

print("Created Dictionary is:")
print(listdict)

# iterate the list and modify the dictionary, remove the dictionary element if values are integers and add average of those values
for dic in listdict:
    sum = 0
    average = 0
    newKey = ''
    count = 0
    removeList = []
    for key, value in dic.items():
        if isinstance(value,(int,float)):
            if(count!=0):
                newKey = newKey + "+" + key
            else:
                newKey = key
            sum = sum + value
            count = count +1
            removeList.append(key)
    average = sum/count
    for lis in removeList:
        dic.pop(lis)
    dic.update({newKey:average})

#print updated dictionary
print("Updated Dictionary is:")
print(listdict)