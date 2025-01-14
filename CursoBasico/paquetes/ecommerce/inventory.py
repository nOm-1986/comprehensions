# Agrega un producto al inventario
def add_product(product_name:str, stock:int, price:int):
    """"
    Función para agregar productos
    
    """
    print(f'Producto {product_name} agregado con {stock} unidades y precio {price}')

def remove_product(product_name):
    print(f'Producto {product_name} eliminado del inventario')