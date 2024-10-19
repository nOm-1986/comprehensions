class BankAccount:
    def __init__(self, account_holder, balance) -> None:
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"Se ha depositado {amount} en la cuenta de {self.account_holder}. Saldo actual: {self.balance}")
        else:
            print("No se puede depositar, cuenta inactiva")
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Se ha retirado {amount} en la cuenta de {self.account_holder}. Saldo actual {self.balance}")

    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta de {self.account_holder} ha sido desactivada")
        self.current_balance()

    def activate_account(self):
        self.is_active = True
        print(f"La cuenta de {self.account_holder} ha sido activada")
        self.current_balance()
    
    def current_balance(self):
        print(f"Tu saldo actual es de: {self.balance}")
    
try:
    accountOne = BankAccount("Fabian", 1000)
    accountTwo = BankAccount('María José', 5000)

    accountOne.deposit(10000)
    accountOne.withdraw(6000)
    accountTwo.deposit(50000)
    accountTwo.withdraw(5000)

except TypeError as e:
    print("Hubo un error: ", e)