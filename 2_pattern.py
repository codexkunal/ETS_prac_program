"""
NAME : Kunal singh
date : 10/9/23
Company Name: Silver Oak College of Engineering and Technology
description : pattern program of ppds
"""

num = int(input("Enter the number of rows : "))
n = 1
for i in range(1, num+1):
    for j in range(1, i+1):
        print(n , end=' ')
        n = n+1
    print()