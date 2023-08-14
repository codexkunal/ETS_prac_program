<<<<<<< HEAD
try:
 num1 = int(input("Enter one number :"))
 num2 = int(input("Enter second number:"))
 print("Enter your choice : + , -, * , /")
 ch = input()
except:
   print("Invalid input")

add = lambda x,y : x+y
sub = lambda x,y : x-y
mul = lambda x,y : x*y
div = lambda x,y : x/y


try:
  if ch == '+':
      print(f'Addition of {num1} and {num2} is {add(num1,num2)}')
  elif ch == '-':
      print(f'Subtraction of {num1} and {num2} is {sub(num1,num2)}')
  elif ch == '*':
      print(f'Multiplication of {num1} and {num2} is {mul(num1,num2)}')
  elif ch == '/':
      print(f'Division of {num1} and {num2} is {div(num1,num2)}')
  else:
      print("invalid choice")
except:
  print("Enter Numeric values only")
=======
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

ch = input("Enter your choice : + , - , * , / , % ")

add = lambda x, y: x + y
sub = lambda x, y: x - y
mul = lambda x, y: x * y
div = lambda x, y: x / y
mod = lambda x, y: x % y


if ch == "+":
    print(add(num1, num2))
elif ch == "-":
    print(sub(num1, num2))
elif ch == "*":
    print(mul(num1, num2))
elif ch == "/":
    print(div(num1, num2))
elif ch == "%":
    print(mod(num1, num2))
else:
    print("Invalid choice")
>>>>>>> 3b6ce72 (add)
