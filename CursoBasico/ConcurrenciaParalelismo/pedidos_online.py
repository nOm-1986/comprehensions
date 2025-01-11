import time, random, multiprocessing, asyncio

#Función asyncrona para verificar inventario.
async def check_inventory(item):
    print(f'Checking inventory to {item} ....')
    await asyncio.sleep(random.randint(3, 5))
    print(f'Inventory checked for {item}')
    #Simular disponibilidad del producto
    return random.choice([True, False])

# Función asíncrona para procesar el pago
async def process_payment(order_id):
    print(f'Processing payment to order {order_id} ....')
    await asyncio.sleep(random.randint(2,4))
    
    if random.choice([True, False]):
        print(f'Payment processed to order {order_id}')
        return True
    else:
        print(f'Payment can not be processed to order {order_id}... Please try again')
        return False
        
# Función intensiva en CPU para calcular el costo total del pedido
def calculate_total(items):
    print(f'Calculating total cost to {len(items)} articulos ....')
    time.sleep(5)
    total = sum(item['price'] for item in items)
    print(f'Total cost calculated: {total}')
    return total

async def process_order(order_id, items):
    print(f'Iniciando el procesamiento de la orden {order_id} ....')
    # Verificar inventario para cada artículo
    inventory_check = [check_inventory(item['name']) for item in items]
    inventory_results = await asyncio.gather(*inventory_check)