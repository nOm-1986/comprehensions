def log_transaction(func):
    def wrapper():
        print('1 - Log of transaction ...')
        func()
        print('3 - After exec the function')
    return wrapper


#PAra usar el decorador utilizo @
@log_transaction
def process_payment():
    print('2 - Processing pay......')


process_payment()