
# Arithematic operators
add = 5 + 2
print(add)
subtract = 5 - 2
print(subtract)
multiply = 5 * 2
print(multiply)
divide = 5 / 2
print(divide)
exponents = 5 ** 2
print(exponents)


# Python supports order of operations
ooo = 2 + 3 * 4
print(ooo)

# Use parens to alter the ooo
ooo_altered = (2 + 3) * 4
print(ooo_altered)


# Floats are any numbers with a decimal point
# They work about how youd expect, be careful though, sometimes youll get an arbitrary amount of decimal places
expected = 0.1 + 0.1
print(expected)
unexpected = 0.2 + 0.1
print(unexpected)


# If you divide any two numbers, even if theyre both integers you get a float
divide_int = 4/2
print(divide_int)

# Floats used in any other operation will also give a float
add_float = 1 + 2.0
print(add_float)


# When writing long numbers you can use underscores to make the numbers more readable. Python will ignore the underscores
long_number = 13_000_000
print(long_number)


# You can declare/initialize multiple variables with one line of code. This is most used when initializing a set of nums
x, y, z = 0, 1, 2
print(x)
print(y)
print(z)


# Python doesnt have native constants, but when you want a variable to be treated as one write its label in all caps
IS_CONSTANT = 50


# The philiosphy of python: import this in the interpreter -
