"""
    Operaciones con conjuntos
"""

set_a = {'col','mex','bol'}
set_b = {'pe','bol','chl'}

#Union
set_c = set_a.union(set_b)
set_d = set_a | set_b
print(set_c, set_d)

#Intersección
set_e = set_a.intersection(set_b)
set_f = set_a & set_b
print(set_e, set_f)

#Diferencia
set_g = set_a.difference(set_b)
set_h = set_b - set_a
print(set_g, set_h)

#Diferencia Simétrica => Union sin los elementos que se intersectan.
set_i = set_a.symmetric_difference(set_b)
set_j = set_a ^ set_b
set_b.symmetric_difference_update(set_a)
print(set_i, set_j, set_b)