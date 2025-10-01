# If, else, elif (else if)

# eval()
# compile()
# exec()

# on_holiday = True
# is_admin = False
# is_verifed = False
                    
                                     
# if (is_admin or is_verifed) and on_holiday:
#     print("access allowed")

# import dis 

# def example():
#     x = 0
#     while x < 3:
#         print("something")
#         x += 1

# dis.dis(example)


# temp = 15

# if temp >= 30:
#     print("Very hot")
# elif temp >= 20:
#     print("quite hot")
# elif temp > 10:
#     print("ok")
# else:
#     print("not good")


# mulitiple comparators:

# deposit = 20
# password = "password"

# if 0 < deposit < 100 and password == "password":
#     print("deposited")
# else:
#     print("failed")

# if not 0 < deposit < 100 and password != "password":
#     print("failed")
# else:
#     print("deposit")


# user =  "root"

# # if name in ("root", "admin", "user"):
# #     print("invlaid")
# # else:
# #     print("accepted")

# if name not in ("root", "admin", "user"):
#     print("accepted")
# else:
#     print("invalid")


# Exercise:
# weight converter app
# - user to input weight
# - user to input a unit kgs or lbs
# - logic: check unit
# - logic: do a conversion
# - print out the result
# - stretch: error handling for unit type(upper/lower, else/while loop)
# - optional: error handling for non-numeric inputs for weight. 

# try:
#     result = 10 / 0
# except ZeroDivisionError as e: 
#     print(f"[ERROR] divison by zero not allowed - {str(e)}")
# except Exception as e:
#     print(f"[ERROR] divison by zero not allowed - {str(e)}")
# finally:
#     ("clean up actions go here")

import sys

while True:
    try:
        weight = float(input("Enter a weight: "))
        break
    except ValueError:
        print("Must be numeric input")
        sys.exit()

while True:
    unit = (input("Enter the unit 'k' or 'l'")).lower()

    if unit == "k":
        converted_weight = weight * 2.2
        print(converted_weight)
        break
    elif unit == "l":
        converted_weight = weight / 2.2
        print(converted_weight)
        break
    else:
        ("PLS enter a k or l")
