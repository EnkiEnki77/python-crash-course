# A dictionarie in python is an object containing related data. It utilizes curlies and key-value pairs. Keys are strings
# values are whatever data type youd like.
alien_0 = {"color": "green", "points": 5}

# You access the values of a dictionary using bracket notation just like with a list, but you pass in the key as argument
# instead of an index.
print(alien_0["color"])

# To add new key-value pairs to a dictionary use bracket notation with a new key name and the assignment operator.
alien_0["weapons"] = 5
print(alien_0)

# When storing user input you may start off with an empty dictionary and add in key-value pairs dynamically.

# you can reassign the values of a key
alien_0 = {"x_position": 0, "y_position": 0, "speed": "slow"}
print(f"The original position of the alien is {alien_0['x_position']}")

if alien_0["speed"] == "slow":
    alien_0["x_position"] += 1

print(f"New position: {alien_0['x_position']}")

# You can delete keys in a dictionary using the del keyword
del alien_0["speed"]
print(alien_0)

# You can use dictionaries to store mutiple different kinds of data about the same object, or to store the same kind of 
# data about multiple different objects.

# You should put key-values onto their own line for readability
readable = {
    "one": 1,
    "two": 2,
    "three": 3
}