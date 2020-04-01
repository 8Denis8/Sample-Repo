import math
from os import rename
import sys
import requests

# name = input("Your name? ")
# print("Hello,", name)

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    # test = "Test"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet("World"))
# print(greet("Coret"))

r = requests.get("https://www.trafficschool.com/course/en/login.asp")
print(r.status_code)

# print("--------------------------")

# age = 18

# if age >= 21:
#     print("You can buy booze")
# else:
#     print("YOU CAN'T BUY BOOZE!")

# print("--------------------------")

# m = 21

# if m > 0 and m <= 31:
#     print("Valid date")
# else:
#     print("Invalid date")
