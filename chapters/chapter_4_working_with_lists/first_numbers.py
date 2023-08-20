# The range function allows you to generate a series of numbers to loop through, when looping through a range, the loop
# will stop one number before the specified end of the range. So if we utilize range(1, 5) the loop would print 1,2,3,4
for num in range(1, 5):
    print(num)
print(f"\n")

# Pass range only one argument, and it will start the count from 0, and the argument will act as the end point
for num in range(6):
    print(num)

# You can convert the output of the range function into a list using the list function
numbers = list(range(6))
print(numbers)