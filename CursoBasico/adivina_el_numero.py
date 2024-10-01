import random


def run():
    intentos = 1
    num_aleatorio = random.randint(1, 100)
    numero = int(input('Escribe un numero: '))
    while num_aleatorio != numero:
        intentos += 1
        if numero < num_aleatorio:
            print('Escribe un numero más grande')
        else:
            print('Escribe un numero más pequeño')
        numero = int(input('Escribe otro numero: '))

    print('¡¡¡ ---  Excelente Ganastes --- !!!')
    print('Numero de intentos: ', intentos, ' xD\n' )


if __name__ == '__main__':
    run()