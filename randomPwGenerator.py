# Random Password generator

import random
import string

# print(string.ascii_letters)
# print(string.punctuation)
# print(string.digits)

pass_len= 12
password = ""
charValues= string.ascii_letters + string.digits + string.punctuation


for i in range(pass_len):
    password+= random.choice(charValues)

print("The Password is:",password)

# #The above process can be also done using List Comprehension

# result= password.join([random.choice(charValues) for i in range(pass_len)])
# #The above join command joins the elements in the list to the empty string password( or we can just write "".join()).

# print(result)