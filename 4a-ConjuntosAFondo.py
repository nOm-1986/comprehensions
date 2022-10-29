"""
    Funciones de actualización de conjuntos
"""

#.add(elemt) -- Añadimos un elemt al conjunto
setA, setB = {1, 2, 3, 4}, {4, 5, 6}
setA.add(5)
print(setA)

#.remove(elemt) -- Elimina elemt SI ESTA PRESENTE, de lo contrario, eleva una excepción de tipo KeyError.
setA.remove(5)
print(setA)

#.discard(elemt) -- elimina elemt si esta presente, no eleva excepción alguna.
setA.discard(4)
setA.discard(0)
print(setA)

#.pop() -- elimina y devuelve un elemento arbitrario de setA. KeyError si el conjuto esta vacío.
setA.pop()
print(setA)

#.clear() -- elimina todos los elementos de setA
setA.clear()
print(setA)

#.update(*elemt) -- añade los elementos de un iterador al conjunto. |= para concatenar
setA.update(x for x in range(7))
print(setA)


setA = set(range(0,10))
setC = set(range(7,12))
setD = set(range (13,20))
#setA.difference_update(*elemt) -- elimina los elementos encontrados en el iterador elem, que estén en setA
#Se puede concatenar usando setA -= elementos1 | elementos2 | ...
setA.difference_update(setB, setC)
print(setA)
setA -= setC | setB
print(setA)


#col.intersection_update(*elemt) -- mantiene solo los elementos en común entre setA y el iterador elementos.
#puedo concatenar setA &= elementos | elementos2 | elementos3 | ...
colores1 = {'amarillo', 'azul','rojo'}
colores2 = {'verde', 'negro', 'amarillo','verde'}
colores3 = {'morado', 'rosado','purpura', 'amarillo'}
colores1.intersection_update(colores2, colores3)
print(colores1)

#setA.symmetric_difference_update(setB) -- actualiza setA manteniendo solo los elementos encontrados en setA o en setB pero que no esten en ambos.
colores3.symmetric_difference_update(colores2)
print(colores3)


"""
    Operadores para Conjuntos
    Nos ayudan a realizar comprobaciones sobre conjuntos, el tamaño, si
    un elemento pertenece o no, entre otros.
"""

# len(setA) -- número de elementos que tiene el conjunto

# elemt in setA -- True si el elemt está presente False en caso contrario.

# elemt not in setA -- True si el elemt no está presente False en caso contrario.

#setA.isdisjoint(setB) -- True si no existen elementos en común entre los dos conjuntos. No hay elementos en su intersección.

#setA.issubset(setB) -- True si todos los de setA estan en setB
# setA <= setB --- setA < setB

#setA.issuperset(setB) -- True si todos los elementos de de setB estan en setA
# setA >= setB --- setA > setB


