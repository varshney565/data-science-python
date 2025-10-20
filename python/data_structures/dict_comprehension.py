#dict comprehension
dct = {i:i*i for i in range(1,6)}
print(dct)
print("-"*50)


#with condition
dct = {i:i**3 for i in range(1,11) if i%2==0}
print(dct)
print("-"*50)

#dict from lists
lis = ['apple','banana','kiwi','shivam','varshney','india']
dct = {lis[i]:len(lis[i]) for i in range(len(lis))}
print(dct)


dct = {f'num_{i}': i for i in range(1,11)}
print(dct)

dct_3 = {key:value for key,value in dct.items() if value%3 == 0}
print(dct_3)
print("-"*50)
#nested dict comprehension
lis = [[1,2,3],[4,5,6],[7,8,9]]
dct = {(i,j):lis[i][j] for i in range(len(lis)) for j in range(len(lis[i]))}
print(dct)
print("-"*50)