# Mini Project

###  GUESS THE NUMBER ### 

import random # A predefined library for generating random values

target=random.randint(1,100)

while True:
    answer=input("Enter the number: or Quit(Q) ")
    if(answer=="Q"):
        break
    
    answer=int(answer)
    if(answer>target):
        print("Your number is greater than the target")
    elif(answer<target):
        print("Your number is less than the target")
    else:
        print("You have won the game")
        break
    
print("---GAME OVER---")