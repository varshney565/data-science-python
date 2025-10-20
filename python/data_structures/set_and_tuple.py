#set (unordered and mutable) and tuple (ordered and immutable) data structures in python

#Set data structure
print("Set data structure-----------------------------------")
my_set = {10,2,3,4,4,5,5,5,6}
print(my_set)  #duplicates will be removed
print("*"*50)

#adding elements
my_set.add(7)
my_set.add(3)  #adding duplicate element, will have no effect
print("After adding elements:",my_set)  
print("*"*50)

#removing elements
my_set.remove(2)  #if element not found, raises KeyError
my_set.discard(10) #if element not found, no error raised
print("After removing elements:",my_set)
print("*"*50)

#pop element
popped_element = my_set.pop()  #removes and returns an arbitrary element    
print("Popped element:",popped_element)
print("Set after popping an element:",my_set)
print("*"*50)

#iterating through set
print("Iterating through set:")
for elem in my_set: 
    print(elem,end=" ")
print()
print("*"*50)

#checking presence of element
print("Checking presence of element:")
print(5 in my_set)
print(10 in my_set)
print("*"*50)


set_1 = {1,2,3,4}
set_2 = {3,4,5,6}
#set operations
print("set_1:", set_1)
print("set_2:", set_2)
print("union:", set_1 | set_2)
print("intersection:", set_1 & set_2)
print("difference:", set_1 - set_2)
print("symmetric difference:", set_1 ^ set_2)
print("*"*50)