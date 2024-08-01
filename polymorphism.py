# POLYMORPHISM  (Operator Overloading)

# Same Operator has different function depending on the condition  

print(1+2) #3
print("Hi "+"Jonathan") # Hi Jonathan (Concatenate)
print([1,2,3]+[4,5,6]) # Merge

# All the above cases are the implicit Operator Overloading, predefined in Python

#### Explicit Operator Overloading ####

# Example of Imaginary Numbers

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
        


    
