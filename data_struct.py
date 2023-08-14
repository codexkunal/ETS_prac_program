#list

ls =[1 , 2 , 5 , 8 ,'harry' , True , 33,32]
ls.remove('harry')
print(ls)
"""""""""ls[1] = 9
print(ls)""""""

for i in range(7):
    print(ls[i])
"""


# list methods

"""lst = [11,25,6,2,4,5,6]
print(lst)"""
#lst.append(99)
#lst.sort(reverse=True)
#lst.reverse()
#print(lst.index(6))
"""lst.pop()
lst.remove"""
#print(lst.count(6))
"""lst.insert(1,222)
print(lst)"""
"""

#tuple

tup = (1, 2, 5, 6, 3, 'hello')
print(tup[2])
print(tup)

if 9 in tup:
    print(f'{6} is present in tuple')
else:
    print(f'{9} is not present in tuple')


#methods in tuples

""""""tups = ('russia', 'india', 'america', 'china')
temp = list(tups)
temp.append('japan')
temp.insert(1, 'sri lanka')
temp[2] = 'canada'
tups = tuple(temp)
print(tups)"""
"""

# dictionary

dic = {1:'kunal' 'kuals', 2:'singh', 3:'sengsr', 4:'name'}
print(dic[1])
print(dic)

print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

print([x for x in range(50) if x%2==0])

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['jack']
tel['kunal'] = 2251
print(tel)"""""