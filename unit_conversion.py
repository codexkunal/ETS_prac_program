print(end="                       " )
print("Welcome to unit conversion")
print("What would you like to convert, please select options given below :")
print("1) length\n"  
      "2) Distance\n"
      "3) Weights\n"
      "4) Time")
before_con = int(input("Enter your choise :"))

if before_con == 1:
    exit = 'yes'
    while exit == 'yes':
       print("you have chosen length segment :")
       print("selection the preferable combination :")
       print('1) Km ----> M',end='       ')
       print('2) M ----> Km')
       print('3) Cm ----> M',end='       ')
       print('4) M ----> Cm')
       choise = int(input("Select your choose:"))
    
       if (choise == 1):
        user_input = float(input("Enter the number in Kilometer :"))
        ans = user_input * 1000
        print(f'{user_input} km is equal to {ans} meters')
        exit = input('Enter  to continue into Length segment else Enter no: ')
       elif choise == 2:
          user_input = float(input("Enter the number in meters :"))
          ans = user_input / 1000
          print(f'{user_input} m is equal to {ans} Kilometers ')
          exit = input('Enter yes to continue into Length segment else Enter no: ')
       elif choise == 3:
          user_input = float(input("Enter the number in Centimetrs :"))
          ans = user_input / 100
          print(f'{user_input} Centimeters is equal to {ans} meters')
          exit = input('Enter yes to continue into Length segment else Enter no: ')
       else:
          user_input = float(input("Enter the number in Meter :"))
          ans = user_input * 100
          print(f'{user_input} Meter is equal to {ans} Centimeters')
          exit = input('Enter yes to continue into Length segment else Enter no: ')
"""elif before_con == 2:
    print()
elif before_con == 3:
    print()
else:
    print()        """