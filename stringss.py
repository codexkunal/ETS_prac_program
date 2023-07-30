s = "this is stirng example"

#reverse the string
a=s[-1::-1]   #[::-1]
print(a)

# split and join
a=s.split(" ")
print(a)

c='*'
b=c.join(a)
print(b)

# replace is -> was
p=s.replace(" is "," was ")
print(p)

#word wise reverse
r=a[0][::-1]+a[1][::-1]+a[2][::-1]+a[3][::-1]
print(r)

#reverse with pairs

x=a[0][0:2][::-1]+ " " + a[0][2:4][::-1]+ " " + a[1][0:2][::-1]+ " " + a[1][2:3][::-1]+ " " + a[2][2:4][::-1] + " " + a[2][4:6][::-1]+ " " + a[2][6:8][::-1]+ " " +  a[3][0:2][::-1]+ " " + a[3][2:4][::-1]+ " " + a[3][4:6][::-1]+ " " + a[3][6:8][::-1]
print(x)