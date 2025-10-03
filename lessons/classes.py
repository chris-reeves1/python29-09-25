# classes:

# Classes extend the language.
# types - class allow us to define custom types. 
# custom tyes will have their own attributes and methods
# Class is the blueprint to type behaviour. 

# Classes also give us structure. 

# OOP:
# - polymorphism: different ways of implementing the same methods. 
# - encapsulation: Privacy - private fields public getters and setters.
# - inheritance: inherit all public fields and methods from parent to child. 
# - abstraction: i dont need to see the code.

# class Example:
#     # attributes
#     name = "Chris"
    
#     # methods
#     def speak(self):
#         print(f"hello")

# person = Example()

# print(person.name)
# person.speak()
# person.name = "c"
# print(person.name)
# person.age = 10

# print(person.age)
# person2 = Example()
# person2.id = 1222


# class Students:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age



# student1 = Students("chris", "reeves", 10)

# contructing attr in __init__
# class Students:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age
#         self.full = first + " " + last 



# student1 = Students("chris", "reeves", 10)


# make attr using method
# class Students:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

        
#     def fullName(self):
#         return self.first + " " + self.last


# student1 = Students("a", "smith", 10)
# print(student1.fullName())
# print(Students.fullName(student1))


# mehtods form outside the class
# from types import MethodType
# import builtins

# class Students:
#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

        
#     def fullName(self):
#         return self.first + " " + self.last


# student1 = Students("a", "smith", 10)
# print(student1)
# print(student1.fullName())
# print(Students.fullName(student1))

# def outside(self):
#     print(f"{self.first} called me")

# student1.outside = MethodType(outside, student1)
# student1.outside()

# def class_outside(self):
#     print(f"{self.first} called me")

# Students.class_outside = class_outside
# student1.class_outside()

# self class variables

# class Students:
#     age_increase_amount = 1     

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

        
#     def fullName(self):
#         return self.first + " " + self.last

#     def changeAge(self):
#         self.age = self.age + self.age_increase_amount

# student1 = Students("a", "smith", 10)
# student2 = Students("l", "smith", 12)

# print(student1.age)
# student1.changeAge()
# print(student1.age)

# print(student1.__dict__)
# print(student2.__dict__)
# #print(Students.__dict__)

# student1.age_increase_amount = 5

# student1.changeAge()
# student2.changeAge()
# print(student1.__dict__)
# print(student2.__dict__)


# non self class variables

# class Students:
#     age_increase_amount = 1  
#     __num_of_students = 0    

#     def __init__(self, first, last, age):
#         self.first = first
#         self.last = last
#         self.age = age

#         Students.__num_of_students += 1

        
#     def fullName(self):
#         return self.first + " " + self.last

#     def changeAge(self):
#         self.age = self.age + self.age_increase_amount

#     @classmethod
#     def get_num_of_students(cls):
#         return cls.__num_of_students


# student1 = Students("a", "smith", 10)
# student2 = Students("l", "smith", 12)

# print(Students.get_num_of_students())
# print(Students._Students__num_of_students)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print("{self.name} is eating")

    # developer friendly string
    def __repr__(self):
        return f"Animal({self.name!r}, {self.species!r})"

    # just a string
    def __str__(self):
        return self.__repr__()

# a = Animal("x", "y")
# #print(repr(a))
# b = eval(repr(a))
# print(b.name)
# print(b.species)

# class Cat(Animal):
#     def __init__(self, name, species, breed):
#         super().__init__(name, species)
#         self.breed = breed

#     def talk(self):
#         print("meow")
    
#     #def eat(self):
#      #   print("something diff")
    
#     def __repr__(self):
#         return super().__repr__() + f"- {self.breed}"

# cat1 = Cat("x", "y", "z")
# cat1.talk()
# cat1.eat()
# print(cat1)

Todo: 
classes lab 
class tasks 1-4 (below)
convert rps app into class based design. 



#1. Create a Rectangle class with attributes length and width. 
#Add methods to calculate the area and perimeter of the rectangle. 

#2. Create a BankAccount class with attributes account_number and balance. 
#Add methods to deposit and withdraw money from the account. 

#3. Create a Car class with attributes make, model, and year. 
#Add methods to get and set the values of the attributes. 

#4. Create a Product class with attributes name, price, and quantity. 
#Add methods to calculate the total value of the product (price * quantity) 
#and add or remove items from the product inventory. 