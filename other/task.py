# #Sam has been dumped by his girlfriend so he's gone into the local milk 
# #bar to drown his sorrows. He has a budget, and there's a choice of three (or more) 
# #milkshakes, 
# #differently priced. The barman says, "What can I fix you?" and Sam can reply with a 
# #number corresponding 
# #to the relevant flavour - this list is displayed every iteration. 
# #If he enters Q, he quits and leaves; the barman wishes him well in his search for love. 
# #If he orders but can't pay he's thrown out.

# # from typing import Dict

# # menu = Dict[str, tuple[int, str]]
# # shakes: menu = {}

# # shakes["1"] = (3, "milk")
# # shakes["2"] = ("3", "milk") # mypy will be checked 


# milkshakes = {
#     "1": (3, "Milk"),
#     "2": (5, "Choc"),
#     "3": (10, "Stawberry")
# }

# budget = 20

# while True:
#     print("Menu:")
#     for option, (price, flavour) in milkshakes.items():
#         print(f"{option} - {price}:{flavour}")

#     choice = input("choice 1-3 pls or quit(q): ")

#     # quiting
#     if choice.lower() == "q":
#         break
#     # invlaid choice
#     if choice not in milkshakes:
#         print("invalid choice")
#         continue
    
#     price, flavour = milkshakes[choice]
#     if price > budget:
#         print("get out")
#         break

#     print(f"{flavour} - milkshake served")
#     budget -= price
#     print(f"{budget}")