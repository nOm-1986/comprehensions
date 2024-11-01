FILE_URL: str = "d:/Development/Python/Python/CursoBasico/Decoradores/log.txt"

def log_employee_action(func):
    def wrapper(employee):
        with open(FILE_URL, 'a') as my_file:
            my_file.write(f"1 - {employee.name} --> Action: {employee.accion}")
            my_file.write('\n')
        return func(employee)
    return wrapper

class Employee:
    name: str
    accion: str

    def __init__(self, name: str, accion: str) -> str:
        self.name = name
        self.accion = accion

    @log_employee_action
    def acciones(self):
        print(f'2 - {self.name} realizo la accion {self.accion}')

emp1 = Employee('Mike', 'ingresa')
emp2 = Employee('Mike', 'sale')
emp1.acciones()
emp2.acciones()

