# Methods of Object

class College:
    def __init__(self,name,mark):
        self.name=name
        self.mark = mark
        
    def hello(self):                # Here we define the method which takes self as an attribute, adding self is must
        print("Hello",self.name)    # Here is how the method works
        
    def get_marks(self):
        return self.mark
        
s1=College("Harry",97)                 # This where we initiate the object s1.
s1.hello()                          # This is where we call the method hello.

print(s1.get_marks())


print('\n')


###########################################################

# Program to create a class Student that takes name and marks of 3 subjects as arguments in the constructor
# Then create a method to print the avg of the three

class Student:
    def __init__(self,name,mark):
        self.mark=mark
        self.name=name
     
    def avg(self):
        sum=0
        for i in self.mark:
            sum+=i
        print("Hi",self.name,"your avg score is:",sum/3)
            
        
a1=Student("Jim",[89,97,93])
a1.avg()

# Other than this, the attributes can be changes as well for eg

a1.name="Alex"
a1.avg()
        
    