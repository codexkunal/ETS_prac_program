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


"""
Author Name: Darsh Thakkar
Modified Date: 24 June 2023
Company Name: Silver Oak College of Engineering and Technology
Input Parameter: None
Created Date: 24 June 2023
Description: This program performs various string operations like reversing the string, reversing words in the string, 
             interchanging letters in words, replacing "is" with "was," and joining the string with asterisks.
"""

# String Reverse
s = "this is string example"
Reversed_word = s[::-1]
print(f"Sentence after reversed word : {Reversed_word}")
print()

# Word Reverse
b = s.split(" ")
char_reversed = b[0][::-1] + " " + b[1][::-1] + " " + b[2][::-1] + " " + b[3][::-1]
print(f"Sentence after two cahracter interchange : {char_reversed}")
print()

# Interchange Letters
interchange_letter = b[0][0:2][::-1] + b[0][2:4][::-1] + " " + b[1][0:1][::-1] + b[1][1:][::-1] + " " + b[2][0:4][::-1] + b[2][4:][::-1] + " " + b[3][0:5][::-1] + b[3][5:][::-1]
print(f"Sentence after all words are : {interchange_letter}")
print()

# Replace with Asterisk (*)
sign_replace = "*".join(b)
print(f"Replaced with Asterisk: {sign_replace}")
print()

# Replacing  'is'  with 'was'
replaced = s.replace(" is ", " was ")
print(f"Sentence after replacing is with was': {replaced}")