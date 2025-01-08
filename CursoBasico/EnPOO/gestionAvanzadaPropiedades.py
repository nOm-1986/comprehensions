class Employee:
    def __init__(self, name, salary, salary2):
        self.name = name
        self._salary = salary
        self.__salary2 = salary2
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        else:
            self._salary = new_salary
    
    @salary.deleter
    def salary(self):
        print(f"The salary of {self.name} has been deleted")
        del self._salary


# Crear instancia de Employee
employee = Employee("Jose Bel", 1000, 2000)
print(employee.salary)

# Modificar el salario de forma controlada
employee.salary = 8000
print(employee.salary)

# intentar establecer un salario negativo
#employee.salary = -10000

# Eliminar un salario
del employee.salary

# Propias inquietudes con propiedades privadas
employee.__salary2 = 4000
print(employee.__salary2)

