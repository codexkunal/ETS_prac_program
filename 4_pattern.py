"""
NAME : Kunal singh
date : 10/9/23
Company Name: Silver Oak College of Engineering and Technology
description : pattern program of ppds
"""

num = int(input("Enter the number of rows : "))
m = num-1

for i in range(num):
    for j in range(m):
        print(end=" ")
    m = m-1

    for j in range(0, i+1):
        print(" *", end="")
    print('\r')