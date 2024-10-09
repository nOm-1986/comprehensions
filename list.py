to_do = [
    'Dirigirnos al hotel',
    'Ir a almorzar',
    'Visitar un museo',
    'Volver al hotel',
    ]
print(to_do)

numbers = [1,2,3,4,5,'seis']
print(type(numbers))

mix = ['uno', 2, 3.14, True, [1,2,3]]
print(mix)

print(len(mix))
# ---------------------------  Metodos  ------------------------
mix.append(False)
print(mix[len(mix) -2][2])

mix.append(['a', 'b', 'c'])
print(mix)

# Insert cuando queremos añadir en una posición específica.
mix.insert(0, 'Insertado')
print(mix)

# Las listas se copian por referencia. Pero si lo que quiero es simplemente copiar los valores lo hago por slicing
a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(a)
print(b)
print(id(a))
print(id(b))

c = a[:]
print(id(a))
print(id(c))
del c[4]