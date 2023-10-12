"""
Name : Kunal singh
Modified Date : 10/09/2023
Company Name: Silver Oak College of Engineering and Technology
Description : Problems solving using loops
"""

marks = int(input("Entre your marks :"))

if(90<marks<=100):
   print("According to your Marks your Grade is A")
elif(80<marks<=90):
   print("According to your Marks your Grade is B")
elif(60<marks<=80):
   print("According to your Marks your Grade is C")
elif(40<=marks<=60):
   print("According to your Marks your Grade is D")
elif(0<=marks<40):
   print("Not enough marks to get a grade , you are Failed")
else:
   print("Invalid Marks")