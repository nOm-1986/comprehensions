"""
Implementar un sistema de gestión de pedidos utilizando colecciones y enumeraciones.
1 - Utilizar Defaultdict para llevar el registro de los productos.
2 - Utilizar Enum para ver el estado de la orden.
3 - Contador para realizar el conteo de cada uno de los productos.
"""
from enum import Enum
from collections import defaultdict, Counter

class OrderStatus(Enum):
    PENDING = 1 #Pendiente
    SHIPPED = 2 #Enviado
    DELIVERED = 3 #Entregado

def check_order_status(status: OrderStatus):
    # Comprueba el estado del pedido y devuelve un mensaje
    if status == OrderStatus.PENDING:
        return "Order is still pending."
    elif status == OrderStatus.SHIPPED:
        return "Order has been shipped."
    elif status == OrderStatus.DELIVERED:
        return "Order has been delivered."


availables_products = { 'Banano': 35, 'Mango': 22, 'Papaya': 10, 'Pina': 14}


def count_products(orders: list[str]) -> defaultdict:
    print(OrderStatus.PENDING)
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] += 1
    return product_count


def left_products(list_order_produc, stored_products) -> list:
    print(OrderStatus.SHIPPED)
    despachados = list
    for k, v in list_order_produc.items():
        if k in stored_products:
            stored_products[k] -= v
            despachados = delivered_products(k, v)
    print(OrderStatus.DELIVERED)
    return despachados


def delivered_products(product: str, amount: int) -> list:
    product_delivered = list
    product_delivered[product] = amount
    return product_delivered


try:
    order_1 = {
    'products': ['Banano', 'Mango', 'Papaya', 'Banano', 'Mango', 'Mango'],
    'status': OrderStatus.PENDING
}
    print(f'Productos disponibles: ', availables_products)
    ordenar = count_products(order_1)
    productos_despachados = left_products(ordenar, availables_products)
    print(f'Productos despachados: ', productos_despachados)
    print(f'Productos disponibles: ', availables_products)
    
except Exception as e:
    print(e)
