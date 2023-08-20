motorcycles = ["Suzuki", "Honda", "Yamaha"]
print(motorcycles) 

# You can reassign the value stored at the indexes of a list
motorcycles[0] = "Ducati"
print(motorcycles) 

# You can add an item to the end of the list 
motorcycles.append("Ninja")
print(motorcycles)

# You can add an item to any index of a list using insert. It takes two arguments, the index and the item.
# Insert doesnt delete any items, it simply shifts all items at and after the index argument over one index
motorcycles.insert(1, "H2")
print(motorcycles)

# You can use the del keyword to remove an item from a list
del motorcycles[1]
print(motorcycles)

# If you want to remove an item from an array, but still have access to that item after its removed use pop
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"The last motorcycle I owned was a {popped_motorcycle}")

# You can remove an item from a list at any index using pop
first_owned = motorcycles.pop(0)
print(motorcycles)
print(f"The first motorcycle I owned was a {first_owned.title()}")

# Use del to remove items from a list when you dont need to utilize the removed item, pop when you do.

# We can remove items from a list by value using the remove method
cars = ["nissan", "hyundai", "ford"]
print(cars)

too_expensive = "nissan"
cars.remove(too_expensive)
print(cars)
print(f"\nA {too_expensive.title()} is too expensive for me.")