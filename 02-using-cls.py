# Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.

class Counter:
    # variable in class
    count=0
    # constractor or magic function __init__(self):
    def __init__(self):
    #  this line of code add increment in count variable of Counter class whenever it use
        Counter.count+=1
# @classmethod is use with cls ,cls is like self in it first arggrument use itself like cls
    @classmethod
    def display(cls):
     print(f"Total object created are : {cls.count}")
# intance or objects we created with the help of class.
c1=Counter()
c2=Counter()
c3=Counter()
c4=Counter()

# use class with display function 
Counter.display()

    
