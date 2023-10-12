a = 5
b = 5

def check(a,b):
    c = 3
    d = 2
   
    print(a==b)
    print(a is b)

check(a,b)
print('..................................')

print(a==b)
print(a is b)


x =["apple" , "banana"]
y = ["apple" , "banana"]
z = x

print(x == y)
# true

print(x is z)
#true

print(x is y)
#false

print(x is not z)
#false

print(x != y)
#false

print(x is not y)
#true

# for string

s = 'hello'
t = 'hello'

print( s is t)


print(end="           ")

print("membership operator")

m = 'hello world123@'

print('h' in m)
print('H' not in m)
print('2' in m)
print('@' in m)
print(' ' in m)