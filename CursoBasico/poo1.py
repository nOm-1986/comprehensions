class Person:
    #Constructor
    def __init__(self, name, age='0') -> None:
        self.name = name
        self.age = age

    def greet(self):
        try:
            print(f"Hello, my name is {self.name} and I'm {self.age}")
        except:
            print("Gotcha the second exception")


try:
    personOne = Person("Fabian")
    personOne.greet()
except TypeError as e:
    print(f"There has been an error: ", e)
