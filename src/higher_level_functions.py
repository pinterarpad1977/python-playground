def operate(func, a, b):
    result = func(a,b)
    return result

def add(x,y):
    return x + y

def subtract(a, b):
    return a - b

""" 
print(operate(add, 2, 4))
print(operate(subtract, 2, 6))
print(operate(lambda x, y: x * y, 10, 5)) """


# Create a closure
def make_power(n):
    def func(x):
        return x ** n
    return func

square = make_power(2)
print(square(2))

cube = make_power(3)
print(cube(5))
