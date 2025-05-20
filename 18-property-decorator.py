# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. 
# Use @property to get the price, @price.setter to update it, 
# and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        print("Getting the price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            print("Setting the price...")
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting the price...")
        del self._price

# Test the class
p = Product(100)

# Get the price
print(p.price)  # Getting the price... 100

# Set the price
p.price = 150   # Setting the price...

# Get the updated price
print(p.price)  # Getting the price... 150

# Delete the price
del p.price     # Deleting the price...
