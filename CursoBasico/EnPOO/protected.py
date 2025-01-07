class BaseClass:
    def __init__(self):
        self._protected_variable = "Protected variable"
        self.__private_variable = 'Privada'

    def _protected_method(self):
        print('This is a protected method')
    
    def __private_method(self):
        print("This is a private method")

    def public_method(self):
        self.__private_method()
    
base = BaseClass()
base._protected_variable =  'Changed value of variable'
print(base._protected_variable)
base._protected_method()
print('='*20)
#base.__private_method()
base.public_method()