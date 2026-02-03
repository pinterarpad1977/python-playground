# define a function which takes a number and 
# returns the double of that number

def double(x):
    return x*2

""" for i in range(1,11):
    print(double(i)) """


#define a function which returns True if a number is even, 
# use it in a loop from 1-20 to print only the even numbers

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
# More pythonic solution is just return the condition itself, 
# because it is already True or False

def is_even_better(x):
    return x % 2 == 0
    
""" for i in range(1,21):
    if is_even(i):
        print(i) """


# Arguments - positional or keyword or mixed, but then positional first
def describe_person(name, age, city):
    return f"{name} is {age} old and lives in {city}"

joe = describe_person("Joe", 22, "Birmingham")
sue = describe_person(name="Sue", age=38, city="New York")
arpad = describe_person("Arpad", 49, city="Budaörs")

""" print(joe)
print(sue)
print(arpad)
 """

# **kwargs
# Define a function with **kwargs, print each key and value on its own line

def debug_log(**kwargs):
    message = ""
    for key, value in kwargs.items():
        message += f"{key} = {value}\n"
    return message

log = debug_log(event = "login", user = "Arpad", success = True, is_pro = True)
#print(log)

# Define a function with args, compute the sum, return the result

def total(*args):
    result = 0
    for num in args:
        result += num
    return result

args2 = total(1,1)
args5 = total(12, 45, -100, 54,3)
args_mix = total(1.3, 3, 4.14)

""" print(args2)
print(args5)
print(args_mix)
 """

# design a function with all parameter types
def demo(a, b, *args, debug=False, **kwargs):
    print(f"a = {a}, b = {b}")
    print(f"args: {args}")
    print("debug =", debug)
    kwargs_string = ""
    for key, value in kwargs.items():
        kwargs_string += f"{key}: {value} \n"
    print(kwargs_string)

# More pythonic solution:
def demo(a, b, *args, debug=False, **kwargs):
    print(f"a = {a}, b = {b}")
    print(f"args: {args}")
    print("debug =", debug)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


#demo(1, 2, 3, 4, 5, debug=True, mode="test", verbose=True)


# Create a function which multiplies unknown number of numbers
# Paste 3 numbers both as args and kwargs

def multiply(*args, **kwargs):
    product = 1
    if len(args) > 0:
        for a in args:
            product *= a
    elif len(kwargs) > 0:
        for key, value in kwargs.items():
            product *= value
    else:
        return None
    return product


'''
More pythonic way:
Not necessary to check the length, 
if any of the arguments are empty python returns false.
Don"t use a in args, it might be the same as an input in kwargs
Key is unused in kwargs, use only the values'''
def multiply(*args, **kwargs):
    product = 1

    # multiply positional args
    for value in args:
        product *= value

    # multiply keyword values
    for value in kwargs.values():
        product *= value

    return product

nums_list = [2,3,4,5]
nums_dict = {"a" : 2, "b" : 3, "c" : 4, "d" : 5}

print(multiply(*nums_list))
print(multiply(**nums_dict))
print(multiply(*nums_list, **nums_dict))