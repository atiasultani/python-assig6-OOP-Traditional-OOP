# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. 
# Write a function check_age(age) that raises 
# this exception if age < 18. Handle it with try...except.


#define custom exception

class InvalidAgeError(Exception):
    """rise when the age is less than 18"""
    pass

#function that rise the exception

def check_age(age):
    if age < 18 :
        raise InvalidAgeError("Age must be at least 18")
    else:
        print("Age is valid")
#use try except to handle it 
try :
        user_Age=int(input("Enter Your Age : "))
        check_age(user_Age)

except InvalidAgeError as e :

    print("Invalid Error")

except ValueError:

    print("Please Enter a valid Number : ")