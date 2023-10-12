"""
Name : Kunal singh
Modified Date : 10/9/23
Company Name: Silver Oak College of Engineering and Technology
Description : Problems solving using loops
"""


first_char = input("Enter first character : ")
try:
     if(first_char == 'a' or first_char == 'b' or first_char == 'c'):
        print("you have entered :", first_char)
     else:
        print("you have entered the invalid character")
except ValueError:
    print("Invalid input . Please enter a valid number.")