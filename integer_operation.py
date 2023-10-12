"""
Name : Kunal singh
Modified Date : 10/9/23
Company Name: Silver Oak College of Engineering and Technology
Description : Problems solving using loops
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