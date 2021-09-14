""" 
                                  Dictionary
Unordered collection of items
Mutable
Does it allow duplicates?
                     Yes  (but with a condition)

When do we use dictionary ?
- If we want to know the meaning of some unknown word
We search meaning of word based on character(this character will act as key here)
- Dictionary holds key:value pair instead of a single element like other data types"""

'''    Creating dictionary
- Dictionaries can be created by placing elements inside {} curly braces
- Syntax: friends = {key:value,key:value,key:value}
- Values can be of any type and can be duplicated, where as key's can't be repeated/duplicated
- Keys must be unique and must be immutable like (string ,number,or a tuple with mutable elements)
- We can also use dict() to create a dictionary
'''

"""             Nested Dictionary
- Creating dictionary inside a dictionary is called nested dictionary
- nestedDic = {1,'one',2:{20:'twenty',40:'fourty'}}
"""
#Creating a Dictionary
person_information = {'city':'Hyderabad','name':'Revanth','food':'Biryani'}
print(type(person_information))
#Get the values in a Dictionary

print(person_information['food'])
#You can also use the get method to retrieve the values in a dict. The only difference is that in the get method, you can set a default value. In direct referencing, if the key is not present, the interpreter throws KeyError.

alphabets = {1:'a'}
print(alphabets.get(1))   #a

# get the value with key 2. Pass “default” as default. Since key 2 does not exist, you get “default” as the return value.
print(alphabets.get(2,"default"))

#Add elements to a dictionary
person1_info = {}
person1_info['city'] = "Bangalore"
print(person1_info)

# add another key, value information with key “name”
person1_info["name"] = "revanth"
print(person1_info)

# add another key, value information with key “food”
person1_info['food'] = "Biryani"
print(person1_info)
#{'city': 'Bangalore', 'name': 'Kusheel', 'food': 'Biryani'}

#Combine two dictionaries to get a larger dictionary using the update method.
remain_info = {'mouse':'Logitech','tv':'Samsung'}
#Update method
person1_info.update(remain_info)
print(person1_info)

# Delete del method
person1_info = {'city': 'Bangalore', 'name': 'revanth', 'food': 'Biryani'}
del person1_info['food']
print(person1_info)

#A disadvantage is that it gives KeyError if you try to delete a nonexistent key.
person1_info = {'city': 'Bangalore', 'name': 'revanth', 'food': 'Biryani'}
# deleting a non existent key gives key error.
# del person1_info['ac'] #KeyError: 'ac'
print(person1_info)

#Pop()
  #So, instead of the del statement you can use the pop method. This method takes in the key as the parameter. 
    #As a second argument, you can pass the default value if the key is not present.
person1_info = {'city': 'Bangalore', 'name': 'revanth', 'food': 'Biryani'}
print(person1_info.pop("food",None))
print(person1_info)

print(person1_info.pop("food",None))
#Clear
person1_info.clear()
print(person1_info)
