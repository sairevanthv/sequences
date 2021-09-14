                                            #Strings 
""" You cant update/delete a characters from a string as they are immutable
    (elements cannot be changed once assigned)
    Only new strings can be assigned to the same name
We cannot delete or remove characters from strings
We can delete them all together
name = "revanth"
del name[0]  - not possible
del name  - possible
"""
name = 'Sai Revanth'
#Indexing
print(name[1])
print(name[-2])
                       #Slicing [start:end:step]
print(name[:11:2])         #if we dont give start it will take from starting                  #SiRvnh
print(name[0::2])          #If we dont give ending it will take to last                       #SiRvnh
print(name[::2])           #If we dont give start and end it will take all                    #SiRvnh
                      #Reverse a String
print(name[::-1])        #It is printing start to end but in reverse order          #htnaveR iaS

name = "my name is revanth"
if "revanth" in name:
    print("True")
# Membership operators(in,not in)
print("revanth" in name)