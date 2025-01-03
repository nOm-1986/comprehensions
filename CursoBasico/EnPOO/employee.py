class Employee:
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skills = args
        self.details = kwargs

    def show_employee(self):
        print(f"Employee: {self.name}")
        print(f"Skills: {self.skills}")
        print("Skills:", self.skills )
        print('Details', self.details)

employee = Employee('Jose', 'Js', 'Python', 'PHP', 'CSS', 'Golang', 'ReactNative', age=30, city='Bogotá')
employee.show_employee()