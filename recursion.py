# Recursion is the concept of calling a function within itself

def show(n):
    if n>0:    # Here n>0 is the base case where the recursion stops, generally this is where return case is shown
        print(n)
        show(n-1)

show(5)


print("\n")

# Factorial using recursion

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)
    
    
print(factorial(6))