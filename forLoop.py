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