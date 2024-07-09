# Methods used on dictionary

dict = {
    "name":"Jaunty",
    "class":"4th Year",
    "CGPA":"8.5+"
}

keys=dict.keys() # used to get the keys of a dictionary
print(keys)

values = dict.values() # used to get the values of a dictionary
print(values)

items = dict.items() # used to get the key-value pair of a dictionary in form of tuple
print(items)

keydef = dict.get("name") # used to get the value/defintion for a given key,\n
print(keydef)             # different from dict("name") as this will return error if "name" key does not exist, \n
                          # whereas dict.get("name") would return none if "name" key does not exist.


dict.update({"city":"Mumbai"}) # update method is used to update the dictionary, can be done in 2 ways as shown below.
print(dict)


new_dict = {            # over here we first define a new dictionary then pass it to update method
    "Sex":"Male"
}
dict.update(new_dict)
print(dict)

                          