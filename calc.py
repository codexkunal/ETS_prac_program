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
