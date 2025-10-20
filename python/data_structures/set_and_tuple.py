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


#clearing
my_set.clear()
print("After clearing:",my_set)
print("*"*50)


#tuple data structure
print("Tuple data structure---------------------------------")
my_tuple = (1,2,3,6)
print("Original tuple:",my_tuple)
print("Length of tuple:",len(my_tuple))
print("Accessing element at index 2:",my_tuple[2])
print("Slicing tuple from index 1 to 3:",my_tuple[1:3])
print("*"*50)


#concatenation
tuple_1 = (1,2,3)
tuple_2 = (4,5,6)
concatenated_tuple = tuple_1 + tuple_2
print("Concatenated tuple:",concatenated_tuple)
print("*"*50)


#iterating through tuple
print("Iterating through tuple:")
for elem in concatenated_tuple:
    print(elem,end=" ")
print()
print("*"*50)

#checking presence of element
print("Checking presence of element:")
print(5 in concatenated_tuple)
print(10 in concatenated_tuple)
print("*"*50)


#checking the count of an element
my_tuple = (1,2,3,2,4,2)
count_2 = my_tuple.count(2)
print("Count of 2 in tuple:",count_2)
print("*"*50)


#index of an element
index_3 = my_tuple.index(3)        #will raise ValueError if element not found
print("Index of 3 in tuple:",index_3)
print("*"*50)


#multiply tuple
my_tuple = (1,2,3)
multiplied_tuple = my_tuple * 3
print("Multiplied tuple:",multiplied_tuple)
print("*"*50)

#mutating a tuple by converting to list and back
my_tuple = (1,2,3)
temp_list = list(my_tuple)
temp_list.append(4)
my_tuple = tuple(temp_list)
print("Tuple after mutation:",my_tuple)
print("*"*50)