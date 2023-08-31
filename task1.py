
a = input('Enter the numbers or strings: ')


ls1 = a.split()
print(ls1)


ls = []
lst = []

ls = [int(i) for i in ls1 if i.isnumeric()]
lst =[str(i) for i in ls1 if i.isalpha()]

print(f'Seperated list of the integers: {ls}')
print(f'Seperated list of the Strings: {lst}')


a = input("Enter the values :")
ls1 = a.split(" ")
print(ls1)
ls, lst = [], []
ls = [int(i) for i in ls1 if i.isdigit()]
lst = [str(i) for i in ls1 if i.isalpha()]
print(f'Separated list of the integers:{ls}')
print(f'Separated list of the Strings: {lst}')

lst.reverse()
print("String list is reversed ", lst)
print(f'Maximum and Minimum for the string list is {max(ls)} and {min(ls)}')