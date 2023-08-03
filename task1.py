a = 'z', 1, 5, 6, 4, 9, 'b', 'e', 'w', 'z', 'm', 'kunal'

ls = []
lst = []

ls = [i for i in a  if type(i) == int]
lst =[i for i in a  if type(i) == str]

print(f'Seperated list of the integers: {ls}')
print(f'Seperated list of the Strings: {lst}')

lst.reverse()
print(f'String list is reversed : {lst}')

min_val = min(ls)
print(f'Minimum for the string list is {min_val}')

max_val = max(ls)
print(f'Minimum for the string list is {max_val}')



"""l = [1,5,5,6,3,9]
m = []
n = []
for i in a:
    if type(i) == int:
      m.append(i)
    else:
       n.append(i)
       
print(m ,n)"""

"""m.insert(1 ,99)
print(m)
n.reverse()
print(n)
l.reverse()
print(l)
nlst.remove()
print(nlst)
print(type(ls))"""



"""a = ['z', 1, 5, 6, 4, 9, 'b', 'e', 'w', 'z', 'm', 'kunal']

integers = [value for value in a if isinstance(value, int)]
strings = [value for value in a if isinstance(value, str)]

strings.reverse()  # Using the reverse() function on the 'strings' list

print("Integers:", integers)
print("Reversed Strings:", strings)

lst.reverse()
print(lst)"""