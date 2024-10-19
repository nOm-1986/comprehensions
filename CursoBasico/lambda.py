add = lambda a,b: a + b
print(add(2,3))

mult = lambda a,b,c=1: a * b *c
print(mult(2,3))

#Cuadrado de cada número
number = range(1, 21)
squared_numbers = list(map(lambda x: x**2, number))
squared_numbers2 = [ map(lambda x: x**2, number) ] # Se debe castear a una lista para que funciones.
#print(number)
print(squared_numbers)
print(squared_numbers2)

# Evens
even_numbers = list(filter(lambda x: x%2 ==0, number))
odd_numbers = list(filter(lambda x: x%2!=0, number))
print(even_numbers)
print(odd_numbers)