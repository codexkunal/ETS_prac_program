def rec(num):
    if num == 1:
        return num
    else:
        return num * rec(num-1)



num = int(input("Entre number"))
print(rec(num))