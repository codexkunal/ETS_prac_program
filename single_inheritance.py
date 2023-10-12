class Parent1:  
    def func_1(self):  
        print ("This function is defined inside the parent class.")  
  
  
class Child1(Parent1):  
    def func_2(self):  
        print ("This function is defined inside the child class.")  
  

object = Child1()  
object.func_1()  
object.func_2()  