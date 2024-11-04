"""
No funciona, la forma de utilizar decoradores en clases es distinta.
La vemos más adelante.
"""

def log_pizza_action(func):
        def wrapper(pizza):
            with open(self.FILE_URL, 'a') as my_logger:
                my_logger.write(f"1 - Processing order of {self.name}\n")
                my_logger.write(f" {self.makePizza()} ")
                my_logger.write("\n")
        return wrapper

class MakePizza:
    name: str
    ingredients: str
    FILE_URL: str

    def __init__(self, typeofpizza: str, ingredients: str) -> None:
        self.name = typeofpizza
        self.ingredients = ingredients
        self.FILE_URL = "d:/Development/Python/Python/CursoBasico/Decoradores/log_pizza2.txt"

    @log_pizza_action
    def makePizza(self)-> str:
        process = "Making pizzaaaaa type: ...."
        return process


try:
    piz1 = MakePizza('Napolitada', 'Queso, peperoni, masa')
    piz1.makePizza()

except Exception as e:
    print(f"Error: {e}")