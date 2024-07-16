# Usage of for_loop in Python

nums = [1,2,3,4,5]
for val in nums:
    print(val)
    
veggies = ["Potato","Tomato","Bringal","Carrot"]
for veggie in veggies:
    print(veggie)
    
print("\n")
# For Loop works in tuple and strings as well

# FOR LOOP WITH ELSE

str = "Jonathan"
for char in str:
    print(char)
    if(char == "b"):                # Here if instead of "a", the letter searched was "b", \n
        print("char found")         # output would be all the letters in Jonathan, along with char not Found
        break
else:
    print("char not Found")
    
    
print("\n")

# Range in Python

seq = range(5) # Gives a sequence of numbers starting from 0 to End index -1
for i in seq:
    print(i)
    
# Above command can be written in more simpler way
for i in range(10):
    print(i)
print("\n")    
# Generic syntax is range(start,stop,step)

# WAP to print all even number from 1 to 100
print("Even Numbers")
for i in range(2,101,2):
    print(i)
    
print("\n")

# Pass Command
for i in range(5):
    pass            # It is a null statement that does simply nothing, just like you.
                    # Used for future hold, portion of code which is handled later on.
                    
# LOOP PRACTICE PROGRAMS


# WAP to find the factorial of a number
num = int(input("Enter the no. "))
fact = 1
i=1
while i<=num:
    for i in range(1,num+1):
        fact *=i
        i += 1
print("Fatorial of ",num,"is:",fact)
