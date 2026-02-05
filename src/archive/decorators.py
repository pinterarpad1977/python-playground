'''
Create a decorator called debug that:
1. prints the function name
2. prints the arguments
3. calls the function
4. prints the return value
Then decorate a function of your choice.
'''

from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args = {args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned = {result}") 
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

add(2,3)

