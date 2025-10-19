#list comprehension
print("List Comprehension---------------------")
squares = [x**2 for x in range(10)]
print(squares)

div2 = [i for i in squares if i%2 == 0]
print(div2)

arr = [j+i for i in range(5) for j in range(0,i) if(i*j == 12)]
print(arr)

# i = 0, j = x
# i = 1, j = 0
# i = 2, j = 0,1
# i = 3, j = 0,1,2
# i = 4, j = 0,1,2,3

#multidimensional list comprehension
print("Multidimensional List Comprehension----")
matrix = [[1,2,3],[4,5,6],[7,8,9]]
flat = [num for row in matrix for num in row]
print(flat)


b = [[j for j in range(10)]for i in range(2)]
print(b)