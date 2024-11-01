def check_access(func):
    def wrapper(employee):
        #Comprobar el rol 'admin'
        #if employee.get('role') == 'admin': ==== employee['role']
        if employee['role'] == 'admin':
            return func(employee)
        else:
            print('Acceso denegado. Solo los administradores pueden acceder.')
    return wrapper


@check_access
def delete_employee(employee):
    print(f'El empleado {employee['name']} ha sido eliminado')


admin = {'name': 'Carlos', 'role':'admin'}
client = {'name': 'Jose', 'role':'client'}

delete_employee(admin)
delete_employee(client)