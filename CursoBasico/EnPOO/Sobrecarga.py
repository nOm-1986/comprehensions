class Vector:
    """
        Imagina que puedes hacer que tus clases personalizadas en Python se comporten como números, 
        listas o cadenas de texto, permitiendo sumar objetos, compararlos y mucho más. 
        ¿Qué pasaría si pudieras redefinir cómo tus clases responden a operaciones comunes como +, -, ==, o incluso < ? 
        Esa es la magia de la sobrecarga de operadores.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """ 
        Agregando el metodo mágico __add__ podemos hacer que nuestra objeto interactue como suma
        al momento de utilizar el simbolo +
        """
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Mi vector({self.x}, {self.y})"
    

v1 = Vector(2, 3)
v2 = Vector(4, 1)
v3 = v1 + v2
print(v3)