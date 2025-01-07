class Markert:
    def __init__(self, *args, **kwargs):
        self.products = args
        self.discounts = kwargs
    
    def total_bill(self):
        """
            Calcula el total de cada producto según su precio y cantidad
        """
        total = 0
        for product in self.products:
            if product['name'] in self.discounts:
                total += (product['value'] * product['cuantity']) / ((self.discounts[product['name']]/100) + 1)
                print(f"Producto: {product['name']}, cantidad: {product['cuantity']}, valor: {product['value']}, descuento: {self.discounts[product['name']]}%")
            else:
                total += product['value'] * product['cuantity']
                print(f"Producto: {product['name']}, cantidad: {product['cuantity']}, valor: {product['value']}")
        print(f"Total: {total}")
        
descuentos = { 'Manzanas':25, 'Bananos':4, 'Patilla':10 }

products = [ 
    { 
        "name": "Manzanas",
        "value": 20,
        "cuantity": 1,
    },   
    { 
        "name": "Bananos",
        "value": 10,
        "cuantity": 2,
    },
    { 
        "name": "Patilla",
        "value": 20,
        "cuantity": 4,
    },
    { 
        "name": "Pina",
        "value": 30,
        "cuantity": 1,
    },
    { 
        "name": "Mango",
        "value": 15,
        "cuantity": 1,
    },
    { 
        "name": "Pitaya",
        "value": 12,
        "cuantity": 2,
    },
    { 
        "name": "Melon",
        "value": 32,
        "cuantity": 2,
    },
    { 
        "name": "Uvas",
        "value": 40,
        "cuantity": 1,
    },
    { 
        "name": "Peras",
        "value": 4,
        "cuantity": 4,
    }
]

order1 = Markert(*products, **descuentos)
order1.total_bill()