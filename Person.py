class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    def set_age(self, age):
        try:
            self.__age = int(age)
        except:
            print("Invalid age. Please enter a valid integer.")
        finally:
            print("Age update attempted.")

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.__age} years old."