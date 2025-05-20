# 16. Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called"
# before a function executes. 
# Apply it to a function say_hello().

# decorator fincton
def log_function_call(func):
    def Wrapper():
        print("Function is being called")
        return func() # excute orignal functiom here
    return Wrapper

# apply the decorator
@log_function_call


def say_hello():
        print("Hello!")

say_hello()