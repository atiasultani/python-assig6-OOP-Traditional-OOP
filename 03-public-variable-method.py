# Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    # constractor or magic function 
    def __init__(self,brand):
        self.brand=brand
    
    def start(self):
        print(f"The {self.brand} car is start")


# Instance or objects create with the help of class 
# we use class to make or create instance like my_car1 it is called instance
my_car1=Car("toyota")
my_car1.start()

