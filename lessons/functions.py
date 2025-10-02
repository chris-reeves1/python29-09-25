# repeatability
# abstraction

# def greet(name, age): # paramaters
#     print(f"hello {name}, aged: {age}") # use as vars, unpack as tuples or dictionaries. 

# greet("c", 10)


# defaults after positional args
# def greet(first_name, last_name="r", age=20): # paramaters
#     print(f"hello {first_name}, aged: {age}") # use as vars, unpack as tuples or dictionaries. 

# greet("c", age=10)


# *args
# Tuple of args passed through when we dont know how many args there will be. 

# def make_pizza(size, *toppings):
#     print(f"Order for {size} pizza - with the following toppings:")
#     for topping in toppings:
#         print(topping)

# make_pizza("med", "peppers", "mushroom")

# **kwargs - unknown keyword args

# def order(**items):
#     print("order:")
#     for k, v in items.items():
#         print(f"{k} - {v}")

# order(drink="wine", main="pasta")

# def combined(*args, **kwargs):
#     print(f"args = {args}")
#     print(f"kwrags = {kwargs}")

# combined(1, 2, 3, b=4)


# / and * (purely syntax)
# all args before / must be positional
# all args after * must be keyword
# ENFORCED

# def example(a, b, /, *, c, d):
#     print(f"a is {a}, b is {b}, c is = {c}, d is {d}")

# example(1, 2, d=3, c=4)

# def math_ops(a, b, /, operation="add", *, decimal_place=None):
#     if operation == "add":
#         result = a + b
#     elif operation == "subtract":
#         result = a - b
#     else:
#          raise TypeError("Must be add or subtract")
#     return round(result, decimal_place)

# print(math_ops(10, 5))
# #math_ops(10, 5, "subtract")
# # math_ops(10, 5, operation="add")
# print(math_ops(10.25555, 5.255565, decimal_place=3))

# recurrsion

#stack/frame

# def factorial(n):
#     if n == 1:
#         return 1 # base case
#     else:
#         n * factorial(n - 1)

# print(factorial(5))

# factorial(5) wait....
# factorial(4) wait...
# factorial(3) wait...
# factorial(2)  wait.... 
# factorial(1)  return 1

# Frame: 
# - reprsents a function call
# - locals(), globals()
# - code object (f_code)
# - calling context

# Stack:
# - Stack of frames, ordered from recent to oldest
# - pops the fucntion (deletes + returns its return) 

# import inspect

# def test_function():
#     print("name: ", inspect.currentframe().f_code.co_name)
#     print("stack: ", inspect.stack()[1].function)
#     x = "hello"
#     print(locals())
#     print("full stack")
#     for frame in inspect.stack():
#         print(frame.function)

# def call():
#     test_function()


# call()
# print(locals()) # printing globals
# print(globals() == locals()) # true

# lambdas/functools(wraps/caching)

# lambda
# unnamed and discrete.
# lambda args : expression (iterable)
# add_function = lambda x, y : x + y
# print(add_function(2, 3))

# numbers = [1, 2, 3, 4]
# squared = map(lambda x: x**2, numbers)

# print(list(squared))

# higher order func

# def square(x):
#     return x * x

# def apply_function(func, value):
#     return func(value)

# print(apply_function(square, 10))

# def get_input():
#     return input("Enter something")

# for item in iter(get_input, "quit"):
#     print(f"ENTERED: {item}")

# iter.__next__

# it = iter()
# next(it)

#functools
# wrap - prserves metadata for inpecting/logging/tesing/docs


# def simple_wrapper(func):
#     def wrapped(*args, **kwargs):
#         print("Calling wrapped function")
#         return func(*args, **kwargs)
#     return wrapped

# @simple_wrapper
# def greet(name, age):
#     """ Greets with a name and age"""
#     print(f"hello {name} age is {age}")


# print("function name ", greet.__name__)
# print("doc string is: ", greet.__doc__)
# greet("c", 20)

# from functools import wraps

# def simple_wrapper(func):
#     @wraps(func)
#     def wrapped(*args, **kwargs):
#         print("Calling wrapped function")
#         return func(*args, **kwargs)
#     return wrapped

# @simple_wrapper
# def greet(name, age):
#     """ Greets with a name and age"""
#     print(f"hello {name} age is {age}")


# print("function name ", greet.__name__)
# print("doc string is: ", greet.__doc__)
# greet("c", 20)

# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)
# def add(a, b):
#     print(f"computing....")
#     time.sleep(10)
#     return a + b

# print(add(3,4))
# print(add(3,4))



TODO:

lab 5
lab 6 (stretch: use caching/wrappers)
optional: simple function exercises
Rock/paper/scissor app using functions:
    - user input vs computer
    - computer chooses randomly
    - logic determine winner (few lines as possible)
    - loop to track rounds played, wins, loses.
    - conditionals for play again/quiting logic. 
Finish previous labs 
Research functools
Reseacxh asynchio