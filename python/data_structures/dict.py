dct = {1 : "shivam", 2 : "varshney", 3 : "python",2 : "developer",'1':"engineer"}
print(dct)

#accessing elements
print("\nAccessing elements------------------------------------")
print(dct[1])
print(dct['1'])
print(dct.get(2))
print(dct.get('1'))


#adding and updating elements
print("\nAdding and updating-----------------------------------")
dct[4] = "krishna"  #adding
dct['4'] = "radha"  #adding
del dct[1]        #deleting
dct[2] = "full stack developer" #updating
print(dct)


#iterating through dictionary
print("\nIterating through dictionary--------------------------")
print(dct.keys())
print(dct.values())
print(dct.items())
print("\nKey-Value pairs---------------------------------------")
for key in dct.keys():
    print(key,dct[key],sep="=>",end = ", ")
print()
for key,value in dct.items():
    print(key,value,sep="->",end=", ")
#empty dictionary
print("\nEmpty dictionary--------------------------------------")
dct.clear()
print(dct)


#check presence of key
print("\nCheck presence of key---------------------------------")

dct = {1 : "shivam", 2 : "varshney", 3 : "python",'2' : "developer",'1':"engineer"}
print(2 in dct)
print('5' in dct)
print('varshney' in dct.values())


#updating the dictionaries
print("\nUpdating dictionaries---------------------------------")
dct1 = {1 : "a", 2 : "b"}
dct2 = {3 : "c", 4 : "d"}
dct1.update(dct2)
print(dct1)