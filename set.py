"""
  Unordered collection of items
  Mutable
  Does not allow duplicate items(every element is unique)
  - Best at performance to find whether a specified element is available in the list ?
"""
#Creating a set
  #{} - curly braces
  #built in set() function
#Note: Can have any number of items and they may be of different types(integer,float,tuple,string) but cannot have mutable 
       #elements like lists,sets,dictionaries as it's elements      #anchors = {'Shiva','Sudheer','Suma','Pradeep',[1,2,3]} 
                                                                    # TypeError: unhashable type: 'list'
#How to create an empty set ? 
#Empty set {} ?
#Use set() to create an empty set
''' Accessing element from set 
Indexing ?
Since they are unordered, we cannot use indexing or slicing
We can iterate over set using loops  '''

                #Add/update 
#add() method is used to add single element to the set
#update() method is used to add multiple elements.It can take tuples,
       # lists,strings or other sets as arguments
                #Removing
#discard(item)-specified item will be removed from the set
#remove(item)-specified item will be removed from the set
#Difference
#  discard(item) does not give error 
#  remove(item) gives key error

                #Pop()
#Remove and returns an item from the set
#You will know what item is going to be popped up
#Clear()
 #To remove all the items from the set 
                #Set operations
  #Mathematical operations like union,intersection,difference,symmetric difference
  #We can either use operators or methods
    #Set of all the elements from both the sets .union()
  #Difference
  #a-b (set of elements that are only in a but not in b)
  #Symmetric difference
   #elements present in either of the two sets, but not common to both the sets

anchors = {'Shiva','Sudheer','Suma','Pradeep','Shiva'}
print('anchors:',type(anchors))
print(anchors)

emptySet = set()
print(type(emptySet))

anchors.add('udaya banu')
print(anchors)

anchors.update(['Akhil','Soheil'])
print(anchors)

anchors.discard("Dinesh")
print(anchors)
# anchors.remove("Dinesh")  # KeyError: 'Dinesh'
print(anchors)  

print(anchors.pop())

anchors.clear()
print(anchors)

a = {10,20,30,40}
b = {20,80,70,100}

abUnion = a.union(b)
print(abUnion)

abIntersection = a.intersection(b)  # a & b
print(abIntersection)               #20

abDifference = a.difference(b)  #a-b
print(abDifference)             #{40,10,30}

abSymmetricDiff = a.symmetric_difference(b)   # a^b
print(abSymmetricDiff)    #{100, 70, 40, 10, 80, 30}

set(["Mississippi"])