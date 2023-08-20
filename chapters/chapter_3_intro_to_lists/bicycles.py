
# This is a list
bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles) 

# Access any element of a list by using bracket notation with the index of the element as argument
print(bicycles[2]) # redline

# You can format the array elements
print(bicycles[2].title()) # Redline

# To access items from a list starting from the end use negative numbers
print(bicycles[-1].capitalize()) # Gives the last item in the list

# You can use list items within format strings, just as you would variables
message = f"My first bicycle was a {bicycles[0].title()}"
print(message)