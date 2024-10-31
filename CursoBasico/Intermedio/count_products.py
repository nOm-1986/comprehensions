from collections import defaultdict, Counter, deque
from enum import Enum #default dict establece un valor por defecto si el diccionario no tiene dicho valor.

def count_products(orders: list[str]) -> defaultdict:
    #Crea un diccionario con valore por defecto 0 
    product_count = defaultdict(int)

    for product in orders:
        product_count[product] +=1
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet', 'tv', 'microwave', 'laptop', 'tv', 'PC monitor']
count = count_products(orders)
print(count)

#Contar utilizando Counter
def count_sales(products: list[str]) -> Counter:
    #Usa Counter para contar cuantos productos de cada tipo se han vendido
    return Counter(products)

result = count_sales(orders)
print(f'Resultado con Counter: ', result)


#DEQUE
def manage_delivery_queue() -> deque:
    # Crea una cola para gestionar entregas de productos
    delivery_queue = deque(["order_1", "order_2", "order_3"])
    delivery_queue.append("order_4")  # Agrega al final de la cola
    delivery_queue.appendleft("order_0")  # Agrega al principio de la cola
    delivery_queue.pop()  # Elimina del final
    delivery_queue.popleft()  # Elimina del principio
    return delivery_queue

queue = manage_delivery_queue()
print(queue) 

#Enum
class OrderStatus(Enum):
    PENDING = 1 #Pendiente
    SHIPPED = 2 #Enviado
    DELIVERED = 3 #Entregado

def check_order_status(status: int):
    # Comprueba el estado del pedido y devuelve un mensaje
    if status == OrderStatus.PENDING:
        return "Order is still pending."
    elif status == OrderStatus.SHIPPED:
        return "Order has been shipped."
    elif status == OrderStatus.DELIVERED:
        return "Order has been delivered."
    
print(check_order_status(OrderStatus.DELIVERED)) 