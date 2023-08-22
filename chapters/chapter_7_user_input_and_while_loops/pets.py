pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]
print(pets)
# You can run a while loop for as long as a value exists in an array
while "cat" in pets: 
    # You can then use remove to remove the first instance of the element from the array, because the loop will 
    # continue iterating until "cat" is no longer in the list this allows you to remove all instances.
    pets.remove("cat")

print(f"list with 'cat' removed: {pets}")