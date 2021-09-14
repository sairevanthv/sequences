                              #Tuple ()
"""
Ordeered collection of items
Immutable
Allows duplicate items
Similar as lists
Use parenthesis() to group elements
Main Difference:
  We cannot change the elements of the tuple once it is assigned
Can we keep one tuple inside another tuple ? 
  Yes
  Also known as nested tuple or multidimensional tuples
"""
# Tuples can also be created without parenthesis
  #Then what if we have only one item in the tuple - It will become String
  #We need to put comma to make it as a tuple
''' 
Accessing tuple elements
  Indexing
  Index Error,Type Error
  Nested tuples are accessed using nested indexing
  Negative indexing is also same
  Slicing to get range of values is also same
'''
#Changing tuple
  #Tuples are immutable
  #Elements of a tuple cannot be changed once they are assigned but if the element itself is a mutable data type like list,then it can be changed
#Deleting a tuple
  #since tuples are immutable,we can't delete elements from it
  #Instead,we can delete entire tuple using del keyword
#Converting a list to tuple
  #List can be converted to tuple
  #tuple(list)
#Built-in methods
  #index(value) - Returns index of the given value
  #count(value) - Returns the frequency  of ocurence of a specified value
  
marks = (20,50,80,97,67)
friends = ("Anand","Suresh","Raju","Sonu",[20,40,60,80])
print(type(friends))
print(marks[0])
print(marks[-1])
print(friends[1])
# IndexError: tuple index out of range 
# print(friends[10])

# TypeError: tuple indices must be integers or slices, not float      
# print(friends[1.52])

#TypeError: 'tuple' object does not support item assignment
#friends[0] = "revanth"

friends[4][0] = "Ram"
print(friends)

