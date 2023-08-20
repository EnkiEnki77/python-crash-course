magicians = ["houdini", "david", "natsu"]

# For loops are used to loop through lists in python.And run code for each item. all indented code after the loop is run
# the loop variable should have a name that indicates the data being a single item in the list being looped. 
# the end of the code in the for loop is indicated by the first line not indented.
# The colon at the end of a for loop statement tells python to interpret the next line as the start of the loop. 
# It must be indented.
for magician in magicians:
    print(f"{magician.title()}, that was a great trick.")
    print(f"I can't wait to see the next one {magician.title()}\n")

# Unindented lines after the for loop have access to the for loops variable, but they will only be run once, and only get
# access to the last item in the list that was being looped through.
print(f"That was a great show {magician}")
print(f"That was a great show {magician}")
print(f"That was a great show ")
print(f"That was a great show {magician}")