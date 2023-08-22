# Functions make your program easier to reason about by seperating your program into blocks. We can make it even easier
# By giving them descriptive names, and importing them in as modules. You do this by defining them in their own files.
# This allows you to hide the code of your functions and focus only on the highest level logic. It also allows you to 
# reuse your functions in multiple different programs.

# Every file ending in .py is a module. When python reads this file it copies all code from this file and pastes it to the
# one importing it. When importing modules this way every function in the module is available.  
import pizzas

# To use a module call the function youd like to call as a method of the module.
pizzas.make_pizza(14, "olives", "feta")

# You can also import specific functions from a module
from pizzas import make_pizza

make_pizza(16, "peppers")

# If importing a specific function would conflict with the name of something else you can assign an import alias
from pizzas import make_pizza as mp

mp(18, "anchovies")

# You can also give modules an alias, to shorten things up
import pizzas as p

p.make_pizza(20, "pizza")

# Use the asterisk to import every function from a module without having to use dot notation on the module
from pizzas import *

make_pizza(22, "sauce")

# Functions should have descriptive names and a docstring explaining what the function does. Other programmers should
# be able to use a function by only reading the docstring. It should describe the arguments it needs and what it returns

# If you specify a default value dont put spaces between the =. Same for keyword arguments

# Functions in a module should be seperated by two lines to make things more readable. 