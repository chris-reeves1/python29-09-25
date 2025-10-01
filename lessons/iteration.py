# while + for loops
# save time + code duplication. 

# while loops

# we need a condition to start a while loop
# We need a condition to be met to end the loop.
# Otherwise continues forever.

# x = 0
# while x < 6:
#     print(x)
#     x += 1            
   
# # break

# i = 0
# while i < 6:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# # Continue

# j = 0 
# while j < 6:
#     j += 1
#     if j == 3:
#         continue
#     print(j)

# for loops
# for iterates through an iterable. 

# my_fruits = ["apple", "kiwi", "pear", "orange"]

# for item in iterable:
#     code block

# for fruit in my_fruits:
#     print(fruit)


# l = 0
# while l < len(my_fruits):
#     print(my_fruits[l])
#     l += 1 

# # range

# for a in range(1, 11, 2):
#     print(a)

# String:

# for word in "hello world".split():
#     print(word)

# list comp:
# make new lists or change lists
#           expression   item            iterable     
#result = [  x**2    for      x      in         range(5)]
# result = [x**2 for x in range(5)]
# print(result)


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_squared_numbers = [x**2 for number in numbers if number % 2 == 0]

# dictionary

# for i in {"drink": "cola"}:
#     print(i)

# for i, y in {"drink": "cola"}.items():
#     print(i, y)

# for i in range(1,3):
#     for j in range(1,4):
#         print(i, "x", j, "=", i*j)

# exercise:
# loop to take 5 names
# then print name + "is awesome!"

# while loop
# for Loop
# list comp
# challenge - 1 line list comp

# inner list
#[input("Enter something: " for n in range(5))]

# outer list
#[print(f"{y} is in the list") for y in iterable]

# combined:
# x = [print(f"{y} is in the list") for y in [input("Enter something: ") for n in range(5)]]

# print(x)

# y = print("heelo")
# print(y)