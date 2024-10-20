class Vehicle:
    def __init__(self, brand, model, price) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"Estas comprando el vehiculo {self.brand}.")
        else:
            print(f"El vehiculo {self.brand}. No esta disponible.")
    
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    

# PAra indicar herencia
class Car(Vehicle):
    def __init__(self, brand, model, price, engine: bool) -> None:
        super().__init__(brand, model, price)
        self.engine = engine
    
    def start_engine(self):
        if self.engine:
            print(f"Iniciando el motor de carro {self.brand} {self.model}.")
    
    def stop_engine(self):
        if self.engine:
            print(f"Deteniendo el motor de carro {self.brand} {self.model}.")


class Bike(Vehicle):
    def __init__(self, brand, model, price, engine) -> None:
        super().__init__(brand, model, price)
        self.engine = engine

    def start_engine(self):
        print(f"Es una cicla peee, dale pedal")
    
    def stop_engine(self):
        print(f"Sin frenoos!!!!. Te juiteeeeeeee")


class Truck(Vehicle):
    def __init__(self, brand, model, price, engine: bool) -> None:
        super().__init__(brand, model, price)
        self.engine = engine
    
    def start_engine(self):
        if self.engine:
            print(f"Iniciando el motor de camión {self.brand} {self.model}.")
    
    def stop_engine(self):
        if self.engine:
            print(f"Deteniendo el motor de camión {self.brand} {self.model}.")


class Customer:
    def __init__(self, name) -> None:
        self.name = name
        self.purchased_vehicles = list()
    
    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
            vehicle.start_engine()
            vehicle.stop_engine()
        else:
            print(f"El vehiculo {vehicle.brand} {vehicle.model} no esta disponible")
    
    def inquire_vehicle(self, vehicle: Vehicle):
        availability = "disponible" if vehicle.check_available() else "no esta disponible"   
        print(f"El coche {vehicle.brand} {vehicle.model} esta {availability} y cuesta {vehicle.get_price()}")


class Dealership:
    def __init__(self):
        self.inventory = []
        self.costumers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El coche {vehicle.brand} {vehicle.model} ha sido agragado al inventario")

    def register_custumer(self, custumer: Customer):
        self.costumers.append(custumer)
        print(f"El cliente {custumer.name} ha sido registrado")

    def show_available_vehicles(self):
        print("Coches disponibles en la concesionaria:")
        for car in self.inventory:
            if car.check_available():
                print(f"\t - {car.brand} {car.model} por {car.price}")

try:
    car1 = Car("Toyota", "Corolla", "20000", True)
    car2 = Car("Honda","Civic", "22,000", True)
    truck1 = Truck("Volvo","FH18", "105,000", True)
    bike1 = Bike("GW", "BMX", "2000", False)

    customer1 = Customer("Fabian")
    dealership = Dealership()
    dealership.add_vehicle(car1)
    dealership.add_vehicle(car2)
    dealership.add_vehicle(truck1)
    dealership.add_vehicle(bike1)
    
    #imprimir lista
    dealership.show_available_vehicles()

    #cliente compra
    customer1.inquire_vehicle(car1)
    customer1.buy_vehicle(car1)
    customer1.buy_vehicle(bike1)
except Exception as e:
    print(f"Woopss!!. There has been an error. ", e)
else:
    print(f"Mucho flow mucho flow.")