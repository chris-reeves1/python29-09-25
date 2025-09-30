# Vars + data types + misc

# data types:
# strings: "text...." words, no limits
# int: 10 
# floats 0.77
# booleans: True/False, 1/0, something/nothing

# vars (reference)

# a reference - set a value with "=", data storted in memory   

# Interning (up to 256) - local caching optimization.
# x = 256 
# y = 256

# print(id(x))
# print(id(y))

# print(x is y) # True - is checks the objects - == checks value.

# def test():
#     a = int(str(257))
#     return a

# def test1():
#     b = int(str(257))
#     return b

# print(test() is test1()) # False

# naming convention
# Descriptive, consitant, style-guide, simple, explain with comments.

# snake_case(vars, func. methods), camelCase(same), PascalCase(class names)
# Cant start with a numer + no keywords. 

# 1var = 
# var1 =
# PI = 3.14 # not enforced by python

# Scope (global vs local, shadowing, global(never use, really - rebinding mechansim).)

# global_variable = "Accessible everywhere"


# def test():
#     local_variable = "accessible only within this function"
#     global global_variable
#     global_variable = "rebinded version of the glob var"
#     print(global_variable) # local global_var is used 

# test()
# print(global_variable) # actual global var is called
# print(local_variable) # out of scope. 

# mutation - no need to be rebinded.

# obj_list = [] 

# def test1(x):
#     obj_list.append(x) # mutation - x changes but doesnt get rebuilt. 

# test1("obj1")
# test1("obj2")

# # print(obj_list)

# # mutations + rebinding

# obj_list = [] 

# def add_item(x):
#     obj_list.append(x) # mutation - x changes but doesnt get rebuilt. 

# add_item("obj1")
# add_item("obj2")

# def rebind_list():
#     global obj_list
#     obj_list = ["newObj"]

# rebind_list()
# print(obj_list)

# nonlocal 

# def outer():
#     x = 10
#     def inner():
#         nonlocal x
#         x += 5
#     inner()
#     print(x)

# outer()

# inspect() traceback()
# built-ins
# bodmas (maths)
# concat
# escape chars
# f-strings
# string methods
        
# import traceback
# import inspect

# def function_a():
#     return function_b()

# def function_b():
#     return function_c()

# def function_c():
#     print("the call stack is....")
#     traceback.print_stack()

# function_a()

# Guessing not included.

# Guessing this is included.
# This will test if inspect can retrieve in line comments. 
# def example(num1, num2):
#     """
#         Description: Just an example function.
#         inputs: num1 is an interger, num2 also an integer. 
#         outputs: num1 + num2 as an integer. 
#     """
#     return num1 + num2



#print(inspect.getdoc(example))
#print(inspect.getcomments(example))
#print(inspect.signature(example))
#print(inspect.getsource(example))


# in-builts
# import sys

# with open("file.txt", "w") as file:
#     sys.stdout = file
#     print("go to the file!!") 

# concatenation:

# age = int(input("Ener an age: ")) 
# name = input("enter name: ")

# # print("name is " + name + " age is " + str(age))
# # print("name is ", name, " age is ", age)
# # print("name is {}, age is {}".format(name, age))
# print(f"name is {name.upper()}, age is {age**2}")

# pi = 3.146589

# print(f"{pi:.2f}")
# print(f"{pi:10.3f}")
# print(f"{"text":^10}")

# escape chars
# \ - \n (newline), \t (tab) \u (unicode), \U(extended emojis)


# print("Person 1: \thello how are you\nPerson 2 \tim good thanks! \U0001f604")

# BODMAS (order of presedence)
         #(12)
# x = 3 + 5 * 9 / 5
# % 10%3 = 1  
# // 10//3 = 3
# print(x)




