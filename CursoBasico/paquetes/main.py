import ecommerce.sales
from ecommerce.inventory import add_product, remove_product

from challenge.inventory.stock import process_stock
from challenge.sales.orders import process_orders

add_product('Laptop', 10, 10)
remove_product("Laptop")
ecommerce.sales.process_sale('Laptop',2)


print('*'*30)

process_stock(10, 'Algo')
process_orders(1)

