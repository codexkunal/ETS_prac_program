def fact(x):
    if x == 1 or x == 0:
        return x
    else:
        return x * fact(x-1)



num = int(input("Enter the number:"))

print(fact(num))


