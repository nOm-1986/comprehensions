number = {"llave":"valor", 1:"uno", 2:"dos", 3:"tres"}
print(number['llave'])

information = {
    'Persona 1': {
        'Nombre': 'Jose Fabian',
        'Apellido': 'Beltran Meza',
        'Altura': '1.70 mts',
        'Edad': '37'
    },
    'Persona 2' : {
        'Nombre': 'Maria Jose',
        'Apellido': 'Beltran Rivera',
        'Altura': '1.1 mts',
        'Edad': '5'
    }
}

print(information)
#Conocer las kyes
#print(information[0]['Nombre'])
claves = information.keys()
valores = information.values()
pares = information.items()
print("Claves: \n",claves)
print("\n ============================================= \n")
print("Valores: \n",valores)
print("\n ============================================= \n")
print("Pares: \n",pares)