"""
NAME : Kunal singh
date : 10/9/23
Company Name: Silver Oak College of Engineering and Technology
description : pattern program of ppds
"""

num = int(input("Enter the number of rows : "))
for i in range(0,num+1):
    for j in range(0,num+1):
        if(i+j==(num)/2 or j-i==(num)/2 or i-j==(num)/2 or i+j==(num+(num/2)) or (i+j>=num/2 and j-i<=num/2 and i<=num/2) or (i-j<=num/2 and i+j<=(num+(num/2)) and i>=num/2)):
            print("*", end='')
        else:
            print(end=" ")
    print()