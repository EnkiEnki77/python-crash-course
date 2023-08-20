# To compare if two values are not equal use the != operator
requested_toppings = "mushrooms"

if requested_toppings != "anchovies":
    print("Hold the anchovies!")

# numerical comparisons are also a thing

21 == 21
21 != 32
32 < 21
32 >= 23

# The && operator in Python is just and
1 > 9 and 9 < 10

# The || operator in Python is or
1 == 9 or 9 < 10

# use parens around the two expressions to make things more readable
(1 < 9) or (9 < 10)

# if-elif-else is useful if you just want one block of code to run based on a condition, but if you want code to run
# based on any condition being true just use multiple if statements.

# Checking that a list is not empty before looping through it. If a list is empty it is a falsey value.
toppings = ["peppers"]

if toppings:
    for topping in toppings:
        print(f"{topping.title()} added.")
else:
    print("Are you sure you want a plain pizza?")

# Working with multiple lists
available_toppings = ["pepperoni", "olives", "sausage"]
requested_toppings = ["pepperoni", "olives", "fries"]

if requested_toppings:
    for topping in requested_toppings:
        if topping in available_toppings:
            print(f"{topping.title()} added.")
        else:
            print(f"{topping.title()} is not available.")
else:
    print("Are you sure you want a plain pizza?")