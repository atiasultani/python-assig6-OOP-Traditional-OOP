# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Empolyee:
    def __init(self,name,salary,ssn):
        self.Empolyee_Name=name     #public 
        self._Salary=salary         #protacted besauce we use one underscore _ 
        self.__Ssn=ssn              #private besauce we use before attributies double underscore __
    
emp1=Empolyee("hamza",15000,"10.5.2025")
print(emp1)
