#multi mdict
mdict = {1 : {"name" : "shivam", "age" : 26}, 2 : {"name" : "varshney", "age" : 36}}
print(mdict)

#accessing elements
print("\nAccessing elements----------------------------")
print(mdict[1])
print(mdict[1]['name'])
print(mdict[2]['age'])


#adding, updating and deleting elements
print("\nAdding, updating and deleting elements--------")
mdict[3] = {"name" : "riya", "age" : 29}    #adding
mdict[1]['age'] = 27                        #updating
del mdict[2]['name']                        #deleting
print(mdict)


#iterating through multimdict
from collections.abc import Iterable
print("\nIterating through multimdict------------------")
mdict[1]['marks'] = {'hin' : 99, 'eng' : -10}  #adding nested mdict
mdict['god'] = "krishna"                       #adding simple key-value pair

for i in mdict.keys():
    print(i,end="==>",)
    if isinstance(mdict[i],dict):
        for j in mdict[i].keys():
            print(j,mdict[i][j],sep=":",end=",")
    else:
        print(mdict[i],end="")
    print()



#check presence of key
print("\nCheck presence of key-------------------------")   
print(2 in mdict)
print('name' in mdict[1])
print('marks' in mdict[1])
print('maths' in mdict[1].get('marks',{}))

