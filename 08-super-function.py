# Assignment8: super()
# Create a class Person with a constructor that sets the name. 
# Inherit a class Teacher from it, add a subject field, and 
# use super() to call the base class constructor.
    
class Person:
    def __init__(self,name):
        self.name=name          #base costructor
    
    def display(self):
            print(f"the name is :{self.name}")

class Teacher(Person):
    def __init__(self, name,subject):
        super().__init__(name)   #call a base constructor
        self.subject=subject
    def display(self):
            print(f"here are  \"{self.name}\" is taking \"{self.subject}\" subject")

teacher1=Teacher("umaima","math")
teacher1.display()