# 17. Class Decorators
# Assignment:
# Create a class decorator add_greeting that modifies a class 
# to add a greet() method returning "Hello from Decorator!".
#  Apply it to a class Person.

#class decoratoer (cls)

def add_greeting (cls):

# add a greet() method returning "Hello from Decorator!"

    def greet(self):
        return "Hello from Decorator!"
    cls.greet=greet
    return cls

# Apply decorator
@add_greeting
class Person:
    def __init__(self,name):
        self.name=name

p1=Person("Alip")
print(p1.greet())