# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor.
# Define a __call__() method that multiplies an input by the factor.
# Test it with callable() and by calling the object like a function.

class  Multiplier:
    def __init__(self,factor):
        self.factor=factor
    
    def __call__(self,value):
        return self.factor *  value

#instance     
m1=Multiplier(3)

#call() with value m1=3 -* __call__ parameter value(3) here we use or print instance like function or method callback
print (m1(3))

#check the instance or object  is callable or not 
print(callable(m1))
