def palindromo(cadena):
    reverseString = cadena[::-1]
    if(reverseString == cadena):
        return True
    else:
        return False


def run():
    palabra = input('Ingresa una palabra: ')
    palabra = palabra.lower().replace(' ', '')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()


