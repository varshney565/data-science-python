lst = ['shivam','vishal','riya','rahul']

#accessing elements
print("Accessing elements----------")
print(lst)
print(lst[0],lst[-1],sep=" ")

#changing values
print("Changing values-------------")
lst[0] = 'sv'

#slicing
print("Slicing---------------------")
print(lst[0:3])
print(lst[::-1])
print(lst[3:0:-1])

#appending
print("Appending-------------------")
lst.append('bhalu')
print(lst)

#removing
print("Removing--------------------")
lst.remove('riya')
print(lst)

#inserting
print("Inserting-------------------")
lst.insert(1,'ankit')
print(lst)

#length
print("Length----------------------")
print(len(lst))

#sort
print("Sorting---------------------")
lst2 = [5,3,8,1,4]
lst1 = sorted(lst2)  #does not change original list
print(lst1)
print(lst2)
lst2.sort()          #changes original list
print(lst2)

#Finding index
print("Finding index--------------")
print(lst.index('sv'))

#counting occurrences
print("Counting occurrences-------")
lst3 = [1,2,3,1,4,1,5,1]
print(lst3.count(1))

#finding elemet presence
print("Finding element presence---")
print(3 in lst3)
print(6 in lst3)


#extending
print("Extending------------------")
lst4 = [6,7,8]
lst3.extend(lst4)
print(lst3)

#min max
print("Min and Max----------------")
print(min(lst3))
print(max(lst3))    

lst3 = [1,2,3,4]
#iterating
print("Iterating-------------------")
for i in lst3:
    print(i,end=" ")
print()

#iterating with range   
print("Iterating with range-------")
for i in range(len(lst3)):
    print(lst3[i],end=" ")  
print()
#iterating with index
print("Iterating with index--------")
for index, value in enumerate(lst3):
    print(index, value) 


#iterating with index from specific number
print("Iterating with index--------")
for index, value in enumerate(lst3, start=1):
    print(index, value) 