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

# # dictionaries

# # drinks = {  "still": "water", 
# #             "fizzy": "cola", 
# #             "hot": "coffee"}

# # print(drinks["still"])

# # print(drinks.items())
# # print(drinks.keys())
# # print(drinks.values())

# # print(drinks.get("hot1"))


# # Exercise:
# # Make a dictionary, with authors(2-3) + books(2-3 books)
# # input to ask for an author
# # print a string of the books
# # error handling for incorrect keys
# # try to only use things covered.  

# # book_dictionary = {
# # 	"N.T. Wright": ["The Bible for Everyone: A New Translation", "Surprised by Hope: Rethinking heaven, the resurrection and the mission of the Church"],
# # 	"Martin Luther": ["95 Theses", "The Bondage of the Will", "Table Talk"],
# # 	"Karl Barth": ["Church Dogmatics", "The Epistle to the Romans"]
# # }

# # author = input("Enter the name of the author: ")

# # if author in book_dictionary:
# # 	print("Books by " + author + ": ")
# # 	books = ", ".join(book_dictionary[author])
# # 	print(books)
# # else:
# # 	print("Cannot find any book by the author.")

# booklist = {

#     "J.K. Rowling": [
#         "Harry Potter and the Sorcerer's Stone",
#         "Harry Potter and the Chamber of Secrets",
#         "Harry Potter and the Prisoner of Azkaban"
#     ],
#     "Roald Dahl": [
#         "Charlie and the Chocolate Factory",
#         "Matilda",
#         "James and the Giant Peach"
#     ],
#     "Sheila McCullagh": [
#         "The Land of the Blue Flower",
#         "Tim and the Hidden People",
#         "The Village with Three Corners"
#     ]
# }

# print("Availible authors:")
# print(", ".join(booklist.keys()))

# author = input("please enter an authors name " )

# books = booklist.get(author, []) #or ["sorry no books found"] 

# print(", ".join(books) or "no books found")

# JacksBookshop = {
#   "author1": {
#   "name": "Rick Riordan",
#   "book1": "The Lightning Thief", 
#   "book2": "The Sea of Monsters", 
#   "book3": "The Last Olympian",
# },
#   "author2": {
#   "name": "Jonathan Haidt",
#   "book1": "The Happiness Hypothesis", 
#   "book2": "The Righteous Mind",
#   "book3": "The Anxious Generation",  
# },
#   "author3": {
#   "name": "Colleen Hoover", 
#   "book1": "It Ends With Us",
#   "book2": "Verity",
#   "book3": "Hopeless",    
# }
# }
# y = JacksBookshop.get("author2").get("name")
# print(y)

# record  = JacksBookshop.get("author2")

# list_to_print = []

# for a, b in record.items():
#     if "book" in a:
#         list_to_print.append(b)

# print(", ".join(list_to_print))