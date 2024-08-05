### OOPS Part2 Practice questions ###

#Q1. Class Circle, used to create a cirlce of radius r, methods area() and perimeter()

class Circle:
    def __init__(self,rad):
        self.rad=rad
    
    def area(self):
        return(self.rad*self.rad*3.14)
    
    def perimeter(self):
        return(round(2*3.14*self.rad,5))
    
c1=Circle(5)
print("The area is ",c1.area())
print("The perimeter is ",c1.perimeter())

#############################################################################################################

print("\n")
#Q2. Class Employee, attr-> role, dept, sal , methods-> show details,
#       class Engineer that inherits from Employee has extra attr name and age

class Employee:
    def __init__(self,role,dept,sal):
        self.role=role
        self.dept=dept
        self.sal=sal
    
    def showdetails(self):
        print("Role is ",self.role)
        print("Dept is ",self.dept)
        print("Salary is ",self.sal)
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","CS","1,00,000")

        
emp1=Employee("Rep","CS",85000)
emp1.showdetails()

engg1=Engineer("John",45)
engg1.showdetails()


##################################################################################################


print("\n")


#Q3. Class order which has the items and prices

class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    def __gt__(self,odr2):
        if(self.price>ord2.price):
            print("Order 1 > Order 2")
        elif(self.price<ord2.price):
            print("Order 2 > Order 1")
        
ord1=Order("Chips",20)
ord2=Order("Pepsi",45)

ord1.__gt__(ord2)
# Here above the __gt__ is a dunder function, so direct calling odr1 > ord2 also works 

ord1>ord2

