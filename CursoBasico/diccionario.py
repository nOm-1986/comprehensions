def run():
    mi_diccionario = {
        'llave1' : '1',
        'llave2' : '2',
        'llave3' : '3'
    }

    # print(mi_diccionario)
    # print(mi_diccionario['llave1'])
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    for llave in mi_diccionario.keys():
        print(llave)
    
    for valor in mi_diccionario.values():
        print(valor)
    
    for llave, valor in mi_diccionario.items():
        print(llave + ' - '+ valor)


if __name__ == '__main__':
    run()