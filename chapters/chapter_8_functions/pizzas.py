# You can allow a function to accept an arbitrary amount of arguments using the * operator on a param. 
# Python will store a tuple of all the arguments in this param.
def make_pizza(size, *toppings):
    print(f"Youd like a {size} inch pizza with these toppings: ")
    for toppng in toppings:
        print(toppng)

make_pizza("12", "pepperoni", "mushroom", "olives")

# You can use positional params with arbitrary params, the arbitrary param must come last though
