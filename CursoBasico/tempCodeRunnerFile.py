def greet(name="Sin nombre", last_name="Sin apellido"):
    print("Hola", name, last_name)

final = True

while final:
    print('xx'*10, "Bienvenido a Saludar", 'xx'*10)
    finalizar = int(input("Finalizar == 1, Seguir == 2. \n"))
    if finalizar == 1:
        break
    else:
        nombre = input("Ingrese su nombre. \n")
        apellido = input("Ingrese su apellido. \n")
        greet(nombre, apellido)