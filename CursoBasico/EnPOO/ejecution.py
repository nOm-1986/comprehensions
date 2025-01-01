"""
Ejecución de código de forma directa.
"""

def Sumar(a ,b) -> int: 
    return a + b

def Restar(a, b) -> int:
    return a - b

def Multiplicar (a, b) -> int:
    return a * b

def Dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Error: El divisor no puede ser cero")
        print("Ha ocurrido un error: ", e)

"Para ejecutar de forma directa cuando ejecuto el archivo."
if __name__ == "__main__":
    print('Operaciones')
    res_1 = Sumar(3,5)
    res_2 = Restar(3,5)
    res_3 = Multiplicar(3,5)
    res_4 = Dividir(3,5)
    print(f"Suma: {res_1}, Resta: {res_2}, Multiplicación: {res_3}, División: {res_4}")
