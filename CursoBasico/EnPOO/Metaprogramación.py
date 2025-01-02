"""
Metaprogramación 
"""

class MultipierFactory:
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}")
        return super(MultipierFactory, cls).__new__(cls)
    
    def __init__(self, factor: int):
        print(f"Inicializando con factor {factor}")
        self.factor = factor

    def __call__(self, number: int) -> int:
        return number * self.factor
    
multiplier = MultipierFactory(5)
result = multiplier(10)
print(result)