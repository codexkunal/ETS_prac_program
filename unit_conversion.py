print(end="                       " )
print("Welcome to unit conversion")
print("What would you like to convert, please select options given below :")
print("1) length\n"  
      "2) Distance\n"
      "3) Weights\n"
<<<<<<< HEAD
      "4) Time"  )
=======
      "4) Time")
>>>>>>> 18c66ba77d6984aea84ee5a0f0822f57bba1190b
before_con = int(input("Enter your choise :"))

if before_con == 1:
    exit = 'yes'
    while exit == 'yes':
<<<<<<< HEAD
       print("you have choosen length segment :")
       print("selction the prefeable combination :")
=======
       print("you have chosen length segment :")
       print("selection the preferable combination :")
>>>>>>> 18c66ba77d6984aea84ee5a0f0822f57bba1190b
       print('1) Km ----> M',end='       ')
       print('2) M ----> Km')
       print('3) Cm ----> M',end='       ')
       print('4) M ----> Cm')
<<<<<<< HEAD
       choise = int(input("Select your choise:"))
    
       if choise == 1:
          user_input = float(input("Enter the number in Kilometer :"))
          ans = user_input * 1000
          print(f'{user_input} km is equal to {ans} meters')
          exit = input('Enter  to continue into Length segment else Enter no: ')
       elif choise ==2:
          user_input = float(input("Enter the number in meters :"))
          ans = user_input /1000
          print(f'{user_input} m is equal to {ans} Kilometers ')
          exit = input('Enter yes to continue into Length segment else Enter no: ')
       elif choise ==3:
          user_input = float(input("Enter the number in Centimetrs :"))
          ans = user_input /100
=======
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
>>>>>>> 18c66ba77d6984aea84ee5a0f0822f57bba1190b
          print(f'{user_input} Centimeters is equal to {ans} meters')
          exit = input('Enter yes to continue into Length segment else Enter no: ')
       else:
          user_input = float(input("Enter the number in Meter :"))
<<<<<<< HEAD
          ans = user_input *100
          print(f'{user_input} Meter is equal to {ans} Centimeters')
          exit = input('Enter yes to continue into Length segment else Enter no: ')
elif before_con == 2:
=======
          ans = user_input * 100
          print(f'{user_input} Meter is equal to {ans} Centimeters')
          exit = input('Enter yes to continue into Length segment else Enter no: ')
"""elif before_con == 2:
>>>>>>> 18c66ba77d6984aea84ee5a0f0822f57bba1190b
    print()
elif before_con == 3:
    print()
else:
<<<<<<< HEAD
    print()        
=======
    print()        """
>>>>>>> 18c66ba77d6984aea84ee5a0f0822f57bba1190b
