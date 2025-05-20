# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. 
# Use aggregation by having a Department object store a reference to 
# an Employee object that exists independently of it.

class Department:
    def __init__ (self,name,empolyee):
        self.name=name
        self.empolyee=empolyee  #Agreegation  to take or hold empolyee instance  
    def showinfo(self):
        print(f"Department Name: {self.name} \n Empolyee Details : {self.empolyee.display()}")

class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def display(self):
        return f"\n Name : {self.name} \n Age: {self.age} \n Salary: {self.salary}"
    
#emp instance
emp1=Employee("Hamza",32,32000)
#dep instance
dep1=Department("Computer Science Department",emp1)
#dep method
dep1.showinfo() 
        

