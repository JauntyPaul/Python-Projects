# Class methods

# Methods used to alter the atrributes of the class rather than the object of a class

class Student:
    name="anonymous"
    
    def nameChange(self,name):
        self.name=name       # This changes the name of the object but not the name at the class.
        self.__class__.name="Kuttan"  #This changes the name of the the variable name of the class.
        
p1=Student()
p1.nameChange("Sunil")
print(p1.name)
print(Student.name)     # Here this prints anonymous coz the self.name only changes the object's attribute
                        # After changing it to self.__class__.name, the attribute of the class changes
                        


##################################################################################

# Till now was the static method decorator use, that is changing class attribute using the self keyword
# Now we will use @classmethod decorator

# In class method we use the key word cls which denotes to the class

class Student:
    name="anonymous"
    
    @classmethod        # This is the class decorator
    def changeName(cls,name):   # This method changes the atrribute of the class using the cls keyword
          cls.name=name
  
  
p1=Student()
p1.changeName("Sunil")
print(p1.name)
print(Student.name) 


###############################################################################################

# Now we'll use property decorator

# Property decorator is used to make attributes that are variable, that actually affect the output of an function.

class Kids:
    def __init__(self,math,chem,phy):
        self.math=math
        self.chem=chem
        self.phy=phy
        self.percentage=((self.math + self.chem + self.phy)/3) 
        # This will save the intial value of percentage, change in the value of marks won't reflect in the percentage
        
    @property   #This converts the attribute into a function
    def percent(self):
        return((self.math + self.chem + self.phy)/3)
    
    # Above here the percent attribute is dynamic
        
        
        
s1=Kids(98,97,95)
print(s1.percentage)
s1.phy=83
print(s1.percentage) # There is no change in the value of percentage
print(s1.percent)
