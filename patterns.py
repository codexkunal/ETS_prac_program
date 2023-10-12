num = int(input("enter the number :"))

num = int(input("enter the number :"))
for i in range(0,num+1):
    for j in range(0,num+1):
        if(i==0 or j==0 or j==num or i==num or i+j==(num)/2 or j-i==(num)/2 or i-j==(num)/2 or i+j==(num+(num/2)) or i+j>(num)/2 or i-j>(num)/2 or j-i<(num)/2):
            print("*", end='')
        else:
            print(end=" ")
    print()
"""rombus"""
for i in range(0,num+1):
    for j in range(0,num+1):
        if(i+j==(num)/2 or j-i==(num)/2 or i-j==(num)/2 or i+j==(num+(num/2)) or (i+j>=num/2 and j-i<num/2 and i<num/2) or (i-j<num/2 and i+j<(num+(num/2)) and i>num/2)):
            print("*", end='')
        else:
            print(end=" ")
    print()


for i in range(0,num+1):
    for j in range(0,num+1):
        if(i+j==num/2 or j-i==num/2 or (i+j>num/2 and j-i<num/2 and i==3)):
            print("*", end='')
        else:
            print(end=" ")
    print()


for i in range(0,num):
    for j in range(0,num):
        if(i==0 or j==0 or i==num-1 or j==num-1):
            print("*", end='')
        else:
            print(end=" ")
    print()


for i in range(0,num+1):
    for j in range(0,num+1):
        if(i+j==num or i-j==num or i==num):
            print("*", end='')
        else:
            print(end=" ")
    print()