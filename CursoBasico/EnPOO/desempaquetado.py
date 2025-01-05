#Desempaquetado === desctructuración en JS
def add(*arg) -> int:
    return sum(arg)

values = (1, 3, 4)
print(add(*values))
print(add(1,3,4,5,2))

a = [1, 3, *values]
print(a)

def show_info(name: str, age: str) : 
    print(f"Name: {name}, Age: {age}")


# Para empaquetar utilizo **variable
data = {'name': 'Fabian', 'age': '38'}
show_info(**data)