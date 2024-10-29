def outer_function():
    x = 'Enclosing'
    def inner_function():
        nonlocal x
        x = 'Modified'
        print(f'El valor de inner es: {x}')
    inner_function()
    print(f'El valor outer: {x}')

outer_function()

employes = [
    {
    "name": "Fabian",
    "age": 12,
    "salary": 1000,
    },
    {
    "name": "Jose",
    "age": 14,
    "salary": 2000,
    },
    {
    "name": "Maria",
    "age": 15,
    "salary": 3000,
    },
    {
    "name": "Carli",
    "age": 33,
    "salary": 1500,
    }
]

def more_than_salary(employees: list, threshold: int = 2000) ->list:
    return list(filter(lambda x: x['salary'] > threshold, employees))

print(more_than_salary(employes))
