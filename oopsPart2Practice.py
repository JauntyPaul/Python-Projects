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
        
# class Engineer(Employee):
    # def __init__(self, role, dept, sal,name,role):
        
emp1=Employee("Rep","CS",85000)
emp1.showdetails()