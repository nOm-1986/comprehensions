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


def greet(name="Sin nombre", last_name="Sin apellido"):
    print("Hola", name, last_name)

while True:
    print('xx'*10, "Bienvenido a Saludar", 'xx'*10)
    finalizar = int(input("Finalizar == 1, Seguir == 2. \n"))
    if finalizar == 1:
        print("Saliendo. \n")
        break
    else:
        nombre = input("Ingrese su nombre. \n")
        apellido = input("Ingrese su apellido. \n")
        greet(nombre, apellido)
