list = [[1,2,3],[4,5,6],[7,8,9]]
#accessing
print(list[0])    #first row
print(list[0][1]) #first row, second column

#updating
list[1][1] = 10
list[1] = ["shivam",25]
print(list) 

#slicing
print("Slicing------------------------")
print("first two rows ----------------")
print(list[0:2])  #first two rows
print("last two rows -----------------")
print(list[::2]) #alternate rows
print("first two columns -------------")
print(list[0][0:2]) #first two elements of first row
print("last two columns --------------")
print(list[0][::-1]) #first row in reverse order
print("alternate columns -------------")
print(list[0][2:0:-1]) #first row from index 2 to 1 in reverse order    
print("alternate columns with step 2 -")    
print(list[0][::-2]) #first row in reverse order with step 2


#appending
print("Appending----------------------")
list.append(['a','b','c'])
print(list)

#deleting
print("Deleting-----------------------")
del list[1]
print(list)

#length
print("Length-------------------------")
print(len(list))

#reversing  
print("Reversing----------------------")
# list.reverse()
#or
list = list[::-1]
print(list)

#nested loop
print("Nested loop--------------------")
for row in list:
    for item in row:
        print(item,end=" ")
    print()

#sorting    
print("Sorting------------------------")
list2 = [[3,1,2],[16,14,15],[9,7,8]]
print("Before sorting")
print(list2)
for row in list2:
    row.sort()
list2.sort()
print("After sorting")
print(list2)