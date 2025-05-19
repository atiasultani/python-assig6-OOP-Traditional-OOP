# Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().

from abc import ABC,abstractmethod
#ABC abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# implimantation abc in sub class 

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    
    def area(self): #abstract class humain batata hy k yaa function humain lazmi lihna hy like reminder
        return self.height*self.width
                
        

user1=Rectangle(4,5)
print(f"The area of Rectangle is : height * width = ",user1.area())

