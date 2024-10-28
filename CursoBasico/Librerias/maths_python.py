import math
import random

#Hallar el area y perimetro de un circulo
radius = 5
area = math.pi * radius**2
perimeter = 2 * math.pi * radius

print(f"Area: {area}")
print(f"Perimetro: {perimeter}")

# Generar un numero entero aleatorio.
random_number = random.randint(1, 100)
print(random_number)

#Elegir colores aleatorios
colors = ['Rojo', 'Azul','Verde','Amarillo','Morado','Violeta','Blanco','Negro']
random_color = random.choice(colors)
print(random_color)

#Barajar una lista de cartas
cards = ['As','2','3','4','5','6','7','8','9','10','J','Q','K']
random.shuffle(cards)
print(cards)


