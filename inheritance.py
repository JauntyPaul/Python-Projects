# Inheritance 

# syntax class Child_class(Parent_class)

class Car:
    color="Silver White"
    @staticmethod
    def start():
        print("The Car started ...")
    
    @staticmethod    
    def stop():
        print("The Car Stopped.")
        
class Renault(Car):
    def __init__(self,name):
        self.name=name
        

car1=Renault("Kwid")
car2=Renault("Punch")      

print(car1.name) # This will print the name of the car which is defined in the child class
car1.start()  # This funtion calls the method that is declared in the parent class.
print(car1.color)

