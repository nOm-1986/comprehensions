class Counter:
    count = 0

    @classmethod #Definimos que el metodo a continuación modifica algo de la clase
    def increment(cls):
        cls.count += 1


Counter.increment()
Counter.increment()
Counter.increment()
print(Counter.count)


class Circle:
    
    def __init__(self, radius: float) -> None:
        self._radius = radius

    @property # Nos permite acceder a un método como si fuese una atributo de la clase
    def area(self) -> float:
        return 3.1416 * (self._radius ** 2)
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter #Como si fuese un setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError('El radio no puede ser negativo')
        self._radius = value

    

cir1 = Circle(5)
print(cir1.area)
cir1.radius = 10
print(cir1.area)

