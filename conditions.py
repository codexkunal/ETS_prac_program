"""
Name : Kunal singh
Modified Date : 27/07/2023
Description : Problems solving using loops
"""

"""
1)
"""

first_char = input("Enter first character : ")

try:
     if(first_char == 'a' or first_char == 'b' or first_char == 'c'):
        print("you have entered :", first_char)
     else:
        print("you have entered the invalid character")
except ValueError:
    print("Invalid input . Please enter a valid number.")
           
"""
2)
"""
marks = int(input("Entre your marks :"))

if(90<marks<=100):
   print("Grade A")
elif(80<marks<=90):
   print("Grade B")
elif(60<marks<=80):
   print("Grade C")
elif(40<=marks<=60):
   print("Grade D")
elif(0<=marks<40):
   print("Fail")
else:
   print("Invalid Marks")


"""
3)
"""   
try:
    num = int(input("Enter a number: "))

    if num > 0:
        if num % 2 == 0:
            constant = 2.5  # Floating point constant for even numbers
            result = num * constant
            print("The number is positive and even, so {} multiplied by {} is: {}".format(num, constant, result))
        else:
            constant = 5  # Integer constant for odd numbers
            result = num + constant
            print("The number is positive and odd, so {} plus {} is: {}".format(num, constant, result))
    elif num < 0:
        print("The number is negative.")
        if num % 2 == 0:
            constant = 2.5  # Floating point constant for even numbers
            result = num * constant
            print("The number is negative and even, so {} divided by {} is: {}".format(num, constant, result))
        else:
            constant = 5  # Integer constant for odd numbers
            result = num / constant
            print("The number is negative and odd, so {} subtract {} is: {}".format(num, constant, result))
    else:
        print("The number is zero.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
