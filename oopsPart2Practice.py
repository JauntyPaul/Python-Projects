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