# 13. Composition
# Assignment:
# Create a class Engine and a class Car. 
# Use composition by passing an Engine object to the Car class during initialization.
# Access a method of the Engine class via the Car class.

class Engine:
    def __init__(self,powerhours):
        self.powerhours=powerhours

    def start(self):
        return f"engine is start with {self.powerhours} hp"
class Car:
    def __init__(self,name,engine):
        self.name=name
        self.engine=engine      #composition
    def start_car(self):
                            #call the engine start method
     print (f"{self.name} : {self.engine.start()}")
#create Engine instance     
my_engine=Engine(16000)
#create Car instance        
car1=Car("Cultus",my_engine)
car1.start_car()