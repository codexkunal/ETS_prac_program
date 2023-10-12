<<<<<<< HEAD:task1.py

=======
"""
NAME : Kunal singh
date : 10/9/23
Company Name: Silver Oak College of Engineering and Technology
description : String program of ppds
"""
>>>>>>> b5d1e94 (practical):seperation.py
a = input('Enter the numbers or strings: ')
ls1 = a.split()
print(ls1)

ls = []
lst = []

ls = [int(i) for i in ls1 if i.isnumeric()]
lst =[str(i) for i in ls1 if i.isalpha()]

print(f'Seperated list of the integers: {ls}')
print(f'Seperated list of the Strings: {lst}')


<<<<<<< HEAD:task1.py
a = input("Enter the values :")
ls1 = a.split(" ")
print(ls1)
ls, lst = [], []
ls = [int(i) for i in ls1 if i.isdigit()]
lst = [str(i) for i in ls1 if i.isalpha()]
print(f'Separated list of the integers:{ls}')
print(f'Separated list of the Strings: {lst}')

=======
>>>>>>> b5d1e94 (practical):seperation.py
lst.reverse()
print("String list is reversed ", lst)
print(f'Maximum and Minimum for the string list is {max(ls)} and {min(ls)}')