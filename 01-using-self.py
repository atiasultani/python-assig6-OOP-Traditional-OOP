# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize 
# these values via a constructor. Add a method display() that prints student details.

class Student():
    #  constactor or magic function
    def __init__(self,name,marks):
        self.StudentName=name
        self.StudentMarks=marks
    # method 
    def display(self):
        print(f"Student Name : {self.StudentName}")
        print(f"Student Marks: {self.StudentMarks}")



s1=Student("Anam",50)
s1.display()

s2=Student("zara",30)
s2.display()


print("\n----------------------------\n")
# make record list .

studentRecord=[
    Student("hamza",30),
    Student("maaz",50),
    Student("azeem",50),
    Student("azam",40)]

# for list display we use FOR Loop for indexing 

for students in studentRecord:
    students.display() 
