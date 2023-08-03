a = 'z', 1, 5, 6, 4, 9, 'b', 'e', 'w', 'z', 'm', 'kunal'

ls = []

lst = []

ls = [i for i in a  if type(i) == int]
lst =[i for i in a  if type(i) == str]

l = [1,5,5,6,3,9]
m = []
n = []
for i in a:
    if type(i) == int:
      m.append(i)
    else:
       n.append(i)
       
print(m ,n)

"""m.insert(1 ,99)
print(m)
n.reverse()
print(n)
l.reverse()
print(l)
nlst.remove()
print(nlst)
print(type(ls))"""



a = ['z', 1, 5, 6, 4, 9, 'b', 'e', 'w', 'z', 'm', 'kunal']

integers = [value for value in a if isinstance(value, int)]
strings = [value for value in a if isinstance(value, str)]

strings.reverse()  # Using the reverse() function on the 'strings' list

print("Integers:", integers)
print("Reversed Strings:", strings)

lst.reverse()
print(lst)