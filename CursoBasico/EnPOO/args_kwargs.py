"""
Argumentos *args y **kwargs
args = Cuando no especificamos la cantidad
kwargs = Pasamos la info de forma directa y parametros posicionales. Keyword argument.
"""

# UTILIZANDO ARGS
def sum_numbers(*args) -> int:
    return sum(args)

def count_args(*args) -> int:
    a = len(args)
    return a


# UTILIZANDO KWARGS
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}:{value}')


if __name__ == "__main__":
    print(f"========================= ARGS ========================")
    print(f"Resultado suma 1, 2, 3: {sum_numbers(1,2,3)} ")
    print(f"Resultado suma 1, 2, 3, 4: {sum_numbers(1, 2, 3, 4)} ")
    print(f"Resultado suma 1, 2, 3, 5: {sum_numbers(1, 2, 3, 5)} ")
    print(f"Resultado suma 1, 10,340, 43: {sum_numbers(1, 10,340, 43)}")
    print(count_args(1,3,5,6,7,7,7,12))
    print(f"========================= KWARGS ========================")
    print_info(name="Fabian", age=30, city="Barranca")    
    print(f"=========================")
    print_info(name="Fabian", age=30, city="Barranca", country='Colombia', currency='COP')    