# Types of Inheritance

# Single Inheritance

class Car:
    color="Silver White"
    @staticmethod
    def start():
        print("The Car started ...")
    
    @staticmethod    
    def stop():
        print("The Car Stopped.")
        
class Renault(Car):             # Renault inherited from Car
    def __init__(self,name):
        self.name=name
        

# Multi-level Inheritance

class Kwid(Renault):            # Kwid inherited from Renault from Car
    def __init__(self, mileage):
        self.mileage=mileage
        

# Multiple Inheritance (Multiple Parents)

class A:
    varA="Welcome to class A"
    
class B:
    varB="Welcome to class B"

class C(A,B):                   # C inherited from A and B
    varC="Welcome to class C"
    
    
c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)


print("\n")
#####################################################################

# Super method # Super means the parent class


class Car:
    def __init__(self,type):
        self.type=type
        
    @staticmethod
    def start():
        print("The Car started ...")
    
    @staticmethod    
    def stop():
        print("The Car Stopped.")
        
class Renault(Car):             
    def __init__(self,name,type):
        super().__init__(type)      # Here the constructer in the super class is called.
        self.name=name
        super().start()         # Calls the functions from the super class within the child class
        
        
car1=Renault("Kwid","Petrol")
print(car1.name)
print(car1.type)
car1.start()                   # Calls the function from the super class outside the class for an object