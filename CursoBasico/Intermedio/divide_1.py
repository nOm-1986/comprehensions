def divide(a: int, b: int) -> float:
    #División con validación
    if not isinstance(a, int) or not isinstance(b, int):
        #print("Error: ambos parametros deben ser enteros o flotantes")
        raise TypeError('Ambos parámetros deben ser enteros')
        return None
    #Verificacmos
    if b== 0:
        #print("Error: el divisor no puede ser cero")
        raise ValueError('Pailas papu, divisor no puede ser cero')
        return None
    
    return a/b

try:    
    #rest_1 = divide(2,0)
    #rest_2 = divide(2,"0")
    rest_3 = divide(2,20)
    print(rest_3)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
finally:
    print("Logica papi, logica. Te falta calle.")
    