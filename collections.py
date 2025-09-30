# Basic data structures
# lists - [] - mutable, any data type, indexed/ordered. ["1", 1, True, [], {}, ()]
# dictionaries - {} mutable, any data type, unordered/not indexed, key:value pairs.  
# tuples () or no brackets. immutable. 
# sets - {} unique values (mainly mathmetical methods.)

# x = hash("hello")
# y = x % (16-1)
# print(x)
# a = {} # 8 "buckets" - store 1 key/value pair. 
# {...7:"value"} #- rezised to 16 buckets


# import sys

# d = {}

# for i in range(20):
#     d[i] = i
#     print(sys.getsizeof(d))

# def x(h, b):
#     return h %(b-1)

# h = hash("hello")
# print(x(h, 5))
# print(x(h, 10))

# import time

# large_list = list(range(100_000_000))
# large_dict = {num : True for num in range(100_000_000)}

# target = 90_000_000

# start = time.time()
# l_list = target in large_list
# finish = time.time()
# print(f"result for list: {finish - start:.8f}")

# start = time.time()
# l_dict = target in large_dict
# finish = time.time()
# print(f"Result for Dictionary: {finish - start:.8f}")

# lists

# colours = ["blue", "red", "yellow", "green"]

# direct access:

# print(colours[1])
# print(colours[0:2])

# colours[0] = "orange"
# print(colours)

# nested lists
# numbers = [1, 2, 3, 4]
# letters = ["a", "b", "c", "d"]

# combined = [numbers, letters]

# print(combined[0][3], combined[1][1])

# # Methods
# colours.sort(key=len)
# print(colours)

# # join (string method)
# x = "#".join(colours)
# print(x)

# dictionaries

# drinks = {  "still": "water", 
#             "fizzy": "cola", 
#             "hot": "coffee"}

# print(drinks["still"])

# print(drinks.items())
# print(drinks.keys())
# print(drinks.values())

# print(drinks.get("hot1"))


# Exercise:
# Make a dictionary, with authors(2-3) + books(2-3 books)
# input to ask for an author
# print a string of the books
# error handling for incorrect keys
# try to only use things covered.  

