import collections
#Dictionaries doesn't maintain order.

print ('Normal dictionary:')
dict = {}
dict['1'] = 'A'
dict['2'] = 'B'
dict['3'] = 'C'
dict['4'] = 'D'
dict['5'] = 'E'

for key, value in dict.items():
    print (key, value)

# Make dictionaries ordered

print ('\nOrdered Dictionary:')
dict = collections.OrderedDict()
dict['1'] = 'A'
dict['2'] = 'B'
dict['3'] = 'C'
dict['4'] = 'D'
dict['5'] = 'E'

for key, value in dict.items():
    print (key, value)