# Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name)
# that allows changing the bank name. Show that it affects all instances.

class Bank:
#  bank_name is class variable
    baank_name="HBL"
# classmethod use to change class variable assign name . @classmethod with cls take first argumment. 
    @classmethod
    def change_bank_name(cls,name):
        cls.baank_name=name
# it function show output.
    def display(self):
        print(f"The bank name is {self.baank_name}")


# now create intance or object . use class Bank.
bnk1=Bank()
bnk2=Bank()

# here we use display function to show output
bnk1.display()
bnk2.display()

# if we want to change bank name so we use change bank name function 
Bank.change_bank_name("UBL")
# again display intances to seen update bank name 
bnk1.display()
bnk2.display()
