FILE_URL: str = "d:/Development/Python/Python/CursoBasico/Decoradores/log_pizza.txt"

def log_pizza_action(func):
    def wrapper(pizza):
        with open(FILE_URL, 'a') as my_file:
            my_file.write(f"1 - {pizza.name} --> accion: {pizza.ingredients}")
            my_file.write('\n')
            func(pizza)
    return wrapper

class Pizza:
    name: str
    ingredients: str

    def __init__(self, name, ingredients: str):
        self.name = name
        self.ingredients = ingredients
    @log_pizza_action
    def makePizza(self):
        print(f' 2 - Pizza de tipo: {self.name}, con ingredientes {self.ingredients}')


try:
    piz1 = Pizza('Napolitada', 'Queso, peperoni, masa')
    piz1.makePizza()

except Exception as e:
    print(f"Error: {e}")