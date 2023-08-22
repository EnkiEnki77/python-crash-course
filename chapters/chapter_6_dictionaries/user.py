user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi"
}

# You can loop through a dictionaray using a for loop, the for loop is given two variables, the first will be all the
# keys, the second, all the values. you must then call the items method on the dictionary
for key, value in user_0.items():
    print(f"Key: {key}")
    print(f"Value: {value}\n")

# Use descriptive names for the variables
user_1 = {
    "sophie": "C",
    "enki": "Python",
    "bat": "Rust"
}

for name, language in user_1.items():
    print(f"Name: {name.title()}")
    print(f"Language: {language}\n")

# You can use the keys method to just get all the keys in a dictionary
for name in user_1.keys():
    print(name)
    # You can access the associated value using the key
    print(user_1[name])

# The keys method isnt just for looping though, it returns a sequence of keys. SO you can use it in conditionals to 
# check if a key exists
if "erin" not in user_1.keys():
    print("Good, fuck erin")

# Dictionaries are looped in the same order they were inserted, but sometimes you want to loop in a different order.
# One way is to sort the keys using the sorted function
for name in sorted(user_1.keys()):
    print(name)

# If youre just interested in the values of a dictionary you can use the values method instead of keys when looping
for language in user_1.values():
    print(language)

# To do the above without repeating values you can use the set function. It returns back a Set of the values. A 
# Set is a data structure with no repeating values
for language in set(user_1.values()):
    print(language)

# You can create a set directly by assigning a list to a variable but using curlies instead of straight brackets
my_set = {"python", "c", "python"}
print(my_set)

# You can nest dictionaries into lists, and vice versa.
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "green", "points": 5}
alien_2 = {"color": "red", "points": 5}

aliens = [alien_0, alien_1, alien_2]
print(aliens)

# Generate a list of dictionaries dynamically.
# empty list of aliens
aliens = []

# Make 30 green aliens
for alien in range(30):
    new_alien = {"color": "green"}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)

# Each object may have the same keys but they are considered seperate objects, meaning we can modify them seperately.

# You can then loop through slices of the list and modify dictionaries conditionally
for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"

# When storing multiple dictionaries in a list each dictionarie should have a similar structure, so you can loop through
# the list and work on each dictionary the same way. 

# We can nest a list in a dictionay anytime we need a key to hold more than one value
pizza = {
    "crust": "thick",
    "toppings": ["pepperoni", "olives"]
}

print(f"You order a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza["toppings"]:
    print(topping)


favourite_languages = {
    "enki": ["python", "java", "javascript"],
    "bat": ["korean", "japanese"]
}

for name, languages in favourite_languages.items():
    print(f"\n{name.title()}'s favorite language(s) are:")
    for language in languages:
        print(f"\t{language.title()}")

# You can nest dictionaries in dictionaries, just make sure the nested ones have similar keys to make looping easier.  