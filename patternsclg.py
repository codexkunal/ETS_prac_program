"""
NAME : Kunal singh
date : 27/7/23
description : pattern program of ppds
"""

"""
1)
"""

"""
2)
"""
# num = int(input("Enter the number of rows : "))
# for i in range(num+1):
#     print('1' * i)


"""
3)
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
num = int(input("Enter the number of rows : "))
print("  ")
for i in range(num,0,-1):
    print('*' * i)

    # """rombus"""
# num = int(input("Enter the number of rows : "))
# for i in range(0,num+2):
#     for j in range(0,num+2):
#         if(i+j==(num)/2 or j-i==(num)/2 or i-j==(num)/2 or i+j==(num+(num/2)) or (i+j>=num/2 and j-i<=num/2 and i<=num/2) or (i-j<=num/2 and i+j<=(num+(num/2)) and i>=num/2)):
#             print("*", end='')
#         else:
#             print(end=" ")
#     print()


"""counting numbers"""

# num = int(input("Enter the number of rows : "))
# n = 1
# for i in range(1, num+1):
#     for j in range(1, i+1):
#         print(n, end='')
#         n = n+1
#     print()