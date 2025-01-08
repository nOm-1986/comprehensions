class Products:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.__price = price
        self.__stock = stock
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        else:
            self.__price = new_price

    @property
    def stock(self):
        return self.__stock
    
    @stock.setter
    def stock(self, new_stock):
        if new_stock < 0:
            raise ValueError("Stock cannot be negative")
        else:
            self.__stock = new_stock
    
    def total(self) -> float:
        return self.price * self.stock


product1 = Products('Monitor LG', 500000.19, 3)
print(product1.total())