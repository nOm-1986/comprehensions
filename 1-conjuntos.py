""" Conjuntos
    Agrupan elementos que tienen cosas en común.

    * - Se pueden modificar
    * - No tienen un orden
    * - No pueden tener elementos duplicados
"""

set_countries = {'col','mex','bol','usa','pan','arg'}
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,2,443,25}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

#crear un conjunto a partir de un string
set_from_string = set('Hola mundo')
print(set_from_string)

#conjunto from tuplas
set_from_tuplas = set(('ca','ba','ll','ero','ca','ra'))
print(set_from_tuplas)

numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
unique_numbers = list(set_numbers)
print(unique_numbers)

