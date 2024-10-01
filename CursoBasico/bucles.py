def cicloWhile():
    LIMITE = 10
    contador = 0
    # EL CICLO WHILE
    while contador < LIMITE:
        print(2**contador )
        #print('2 elevado a ' + str(contador) + ' es igual a: ' + potencia_2)
        contador += 1


def cicloFor():
    for contador in range(1, 1001, 2):
        print(contador)

def run():
    #cicloWhile()
    cicloFor()


if __name__ == '__main__':
    run()




