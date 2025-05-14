# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor)
# and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        print("Logger created __init__ called constractor function")

    def __del__(self):
        print("Logger destroyed __del__ called destractor function")

# intances or object create
log=Logger()

#
del log 

