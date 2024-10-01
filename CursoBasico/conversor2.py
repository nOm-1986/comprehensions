def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿Cuántos pesos " + tipo_pesos +  " tienes? :"))
    dolares = str(round((pesos / valor_dolar), 3))
    print("Tienes "+dolares+ "dólares")

menu = """
Bienvenido al conversor de monedas ¯\_(ツ)_/¯
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos
Elige una opción: """

opcion = int(input(menu))
if opcion == 1:
    conversor('Colombianos', 3875)
elif opcion == 2:
    conversor('Argentinos', 65)
elif opcion == 3:
    conversor('Mexicanos', 24)
else:
    print("Ingresa alguna opción valida")



