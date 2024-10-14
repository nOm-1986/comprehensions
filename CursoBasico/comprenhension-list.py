squares = list( x**2 for x in range (1, 11))
#print(type(squares))
#print(squares)

celsius = [1, 10, 20, 30, 40, 50]
fahrenheit = [((9/5 * temperature)+32) for temperature in celsius]
#print('Temperature in F: ', fahrenheit)

# Even numberes
evens = list(x for x in range(1, 21) if x %2 ==0)
print(evens)


print([x for x in range(0,3)])
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
print(len(matrix[0]))
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)


#arbolito = [['x'*i for x in range(i)] for i in range(1,6)]
arbolito = ['a'*x for x in range(1,11)]
print(arbolito)