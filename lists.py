                              #Lists []
"""
Different types of Data ex- int,string,float
Ordered Collection of items -> Order does not change
Mutable
  we can change them 
   = (What is the operator?)  Assignment operator
  we can use assignment operator to change an item from list
"""
#Empty list?:list without any items is called empty list
#Can we keep one list inside another list ?
# Yes

#Also known as nested lists or Multidimensional lists
#Can access elements from nested lists
  #Accesing elements from list
  #Indexing -Index Error
            #with floating point number -Type Error
#we can use negitive indexing
"""      
Concatination & Repeating lists
  - Concatination(+)
  - Repeating (*)
Adding item/items to the list
  - Single item -append()
  - More than one item - extend()
How to add at specific position ?
  - insert(position,value)
Insert multiple elements at specific position using slicing
  - we use slicing[2:2]
Delete /Remove list items
  Use del keyword
  del[0]
  del list
  del list[1:3]
  remove(item): Used to remove an item from the list
  pop(index): remove and returns item at specified index
  pop(): remove and returns last item from the list 
Clear a list
  clear()
"""
friends = ['Ajay','Mohan','Yogesh','Kishore','Praveen']
print(friends)   
friends.append('Sreekanth')
print(friends)  

#friends.extend('Ranadheer','Yashwanth') #TypeError: extend() takes exactly one argument (2 given)

friends.extend(['Ranadheer','Yashwanth'])
print(friends)   

friends.insert(1,'Manoj')
print(friends)  

friends[1:1] = ['Shreyas','Praneeth']
print(friends)  

del friends[1]
print(friends)  

del friends[1:3]   
print(friends)    

friends.remove('Kishore')
print(friends)   

print(friends.pop())
print(friends.pop(1))

# print(type(friends))
# a= list(tuple)
# print(a)
                           #count()
l = [1,2,3,4]
print(l.count(20))
print(l.count(4))
l.append(10)
print(l)