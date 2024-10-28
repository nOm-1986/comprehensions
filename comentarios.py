
def calculate_average(numbers: list) -> float:
    """
    Calcula el promedio de una lista de números

    Parámetros:
    numbers( list): Una lista de números enteros o flotantes

    Retorno:
    float: El promedio de los números en la lista
    """
    return sum(numbers) / len(numbers)

print(f"Promedio: ", calculate_average([1,3,5,6,6,7,33,45,5,3,5,34,5,3,2,43])) # Imprime el resultado