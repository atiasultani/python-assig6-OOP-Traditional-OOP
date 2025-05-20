# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.

class A:

   def show(self):
      print("A have show () method")

class B(A):#that inherit from A and override show()

   def show(self):
      print("B have show () method")

class C (A): #that inherit from A and override show()

   def show(self):
      print("C have show () method")

class D (B,C): # D that inherits from both B and C.
    pass


obj1=D()

obj1.show()

#MRO print 
print(D.__mro__)