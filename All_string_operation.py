"""
Name: kunal singh
Date: 10/09/2023
Company Name: Silver Oak College of Engineering and Technology
description: Below code is for all the string task are given in the lecture such as replace , join , reverse, reverse with words , character interchange.

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
print(f"Sentence after all words are changed : {interchange_letter}")
print()

# Replacing space  with Asterisk (*) sign
sign_replace = "*".join(b)
print(f"Sentence after replacing with asterisk sign: {sign_replace}")
print()

# Replacing  'is'  with 'was'
replaced = s.replace(" is ", " was ")
print(f"Sentence after replacing is with was': {replaced}")