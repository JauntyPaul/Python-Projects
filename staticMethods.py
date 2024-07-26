# Static methods 

# These are methods which are used at class level and does not use self/object attributes

# For static methods we use decorator

# @staticmethod is a decorator used to convert methods into static methods

class Student:
    def __init__(self,name):
        self.name = name
        
   #def college():
   #     print("IIT Bombay")        This method will give an error, since it does not use self as an attribute
   
   # To avoid this error and turn the above method into statis, we use decorator
   
    @staticmethod
    def college():
        print("IIT Bombay")
        

Student.college()           # This calls the static method college
 
 
 
 