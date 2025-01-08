class Order:
    
    @staticmethod #Los métodos estaticos pueden ser accedidos sin necesidad de instanciar la clase
    def calculate_tax(amount, tax_rate):
        return amount * (tax_rate / 100)
    
# Tenemos un atributo global dentro de la clase, queremos cambiarlo pero no queremos instanciar el objeto
class Order2:
    global_discount = 10

    def __init__(self, amount):
        self.amount = amount
    
    @classmethod #Para que funcione debo utilizar en el 1er parametro cls
    def update_global_discount(cls, new_dicount):
        cls.global_discount = new_dicount


Order2.global_discount = 30
print(Order2.global_discount)
Order2.update_global_discount(17)
print(Order2.global_discount)