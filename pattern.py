"""
NAME : Kunal singh
date : 27/7/23
description : pattern program of ppds
"""

"""
1)
"""
n = int(input("Enter the number of rows : "))

for i in range(n):
    print('*' * i)

"""
2)
"""
for i in range(n):
    print('1' * i)


"""
3)
"""
m = n-1

for i in range(n):
    for j in range(m):
        print(end=" ")
    m = m-1

    for j in range(0, i+1):
        print("* ", end="")
    print('\r')