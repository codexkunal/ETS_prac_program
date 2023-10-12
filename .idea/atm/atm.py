from cardholder import cardHolder


def print_menu():
    ## print option for the user
    print("Please choose from one of the options..")
    print("1. Deposit")
    print("2. withdraw")
    print("3. show Balance")
    print("4. Exit")

def deposit(cardHolder):
    try:
        deposit = float(input("How much money u want to deposit : "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("Thank you for your $$. Your new balance is: ", str(cardHolder.get_balance()))
    except:
        print("Invalid Input")

def withdraw(cardHolder):
    try:
        withdraw = float(input("How much money you want to withdraw :"))
        if(cardHolder.get_balance() < withdraw):
            print("Balance is too Low , Please check and Re-enter the amount :")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
    except:
        print("Invalid Input")

def check_balance(cardHolder):
    print(cardHolder.get_balance())

if __name__ == "__main__":
    current_user = cardHolder("","","","","")

    ###create a repo of cardholder
    list_of_cardHolder = []
    list_of_cardHolder.append(cardHolder("2201030600023", 20, "Kunal", "singh", 150.2))
    list_of_cardHolder.append(cardHolder("2201030600024", 21, "Amit", "das", 145.2))
    list_of_cardHolder.append(cardHolder("2201030600025", 22, "Dip", "verma", 155.2))
    list_of_cardHolder.append(cardHolder("2201030600026", 25, "Sumit", "gupta", 10.2))
    list_of_cardHolder.append(cardHolder("2201030600027", 28, "Dev", "sharma", 100.2))

    ### Promt user for debit card number

    debitCardNum = ""

    while True:
        try:
            debitCardNum = input("Please insert your debit card: ")
            debitMatch = [holder for holder in list_of_cardHolder if holder.cardNum == debitCardNum]
            if(len(debitMatch) > 0):
                current_user = debitMatch[0]
                break
            else:
                print("Card number not Recognized. Please try again")
        except:
            print("Card number not recognized. please try again.")

    
    while True:
        try:
            userpin = int(input("Enter the pin: ").strip())
            if(current_user.get_pin() == userpin):
                break
            else:
                print("Invalid Pin. ")
        except:
            print("Invalid Pin. Please Try again")

    print("Welcome", current_user.get_firstName())

    option = 0
    while(True):
      print_menu()
      try:
        option = int(input())
      except:
        print("Invalid Input")

    
      if(option == 1):
        deposit(current_user)
      elif(option == 2):
        withdraw(current_user)
      elif(option == 3):
        check_balance(current_user)
      elif(option == 4):
        break
      else:
        option = 0
    print("Thank you.Have a nice dayn :)")