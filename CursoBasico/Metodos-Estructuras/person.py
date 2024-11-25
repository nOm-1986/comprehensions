class Persona:
    def __init__(self, nombre: str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        # Devuelve una representación amigable para el usuario
        return f"Persona: {self.nombre}, {self.edad} años"

    def __repr__(self) -> str:
        # Devuelve una representación detallada del objeto para depuración
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"
    
    def __eq__(self, value: object) -> bool:
        # Compara si dos personas son iguales en función del nombre
        return self.nombre == value.nombre and self.edad == value.edad
    
    def __lt__(self, otra_persona) -> bool:
        #Compara si una persona es "menor" que otra en función de la edad
        return self.edad < otra_persona.edad
    
    def __add__(self, otra_persona):
        #Sobrecarga el operador para sumar las eades de dos personas
        return self.edad + otra_persona.edad
    

p1 = Persona("Ana", 28)
p2 = Persona("Luis", 35)
p3 = Persona("Ana", 28)

# __str___: Representación legible
print(p1)
print(repr(p2))
