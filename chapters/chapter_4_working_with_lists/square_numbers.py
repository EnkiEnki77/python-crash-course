# You can make almost any kind of list of numbers youd like. This is how youd make a list of the squares of the nums 1 - 10
squares = []
for num in range(1, 11):
    # The ** is how to indicate exponents in python
    square = num ** 2
    # The append method is similar to push in JS.
    squares.append(square)

print(squares)

# There are various functions that help you work with lists, such as min, max, and sum
print(f"This is the smallest element in the array: {min(squares)}")
print(f"This is the largest element in the array: {max(squares)}")
print(f"This is the sum of all the elements in the array: {sum(squares)}")

# List comprehensions allow you to put the declaration of a list and the appendment of items into the list from a for 
# loop all into one line. This is really useful when you are looping through a range manipulating each number in some way
# and then appending to a list. First you define the expression for the values youd like to store in the list. Then 
# you define the for loop that feeds values into the expression.
squaresComp = [square ** 10 for square in squares]
print(f"This is a list comprehension: {squaresComp}")