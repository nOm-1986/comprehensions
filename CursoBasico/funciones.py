# def imprimir_mensaje():
"""  print('Mensaje especial: ')
    print('¡Estoy aprendiedn a usar funciones!')

    imprimir_mensaje()
    imprimir_mensaje()
"""

def conversacion(mensaje):
    print('Hola')
    print('Cómo estás?')
    print('Elegiste la opción ' + mensaje)
    print('Adiós')


opcion = int(input('Elige una opción (1,2,3)'))
if opcion == 1:
    conversacion('1')
elif opcion == 2:
    conversacion('2')
elif opcion == 3:
    conversacion('3')
else:
    print('Elija solo una de esas 3 opciones')
