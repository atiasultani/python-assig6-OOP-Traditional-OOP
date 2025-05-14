# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum.
# No class or instance variables should be used.

class MathUtils:
#  in static method or function we not use constractor or classmethod . it have simple function 
    @staticmethod
    def add(a,b):
        return a+b
# deric use class with function in vari able 
m1=MathUtils.add(5,3)
print("The sum of to arrgument ",m1)