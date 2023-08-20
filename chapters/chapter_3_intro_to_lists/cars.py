# To permanently sort a list use the sort method
cars = ["toyota", "audi", "bmw", "aston martin"]
print(cars)
cars.sort()
print(cars)

# Sort in reversed order by passing the argument reverse=True
cars.sort(reverse=True)
print(cars)

# To sort a list without permanently mutating it use the sorted function
cars = ["toyota", "audi", "bmw", "aston martin"]
print("\nHere is the unsorted list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the unsorted list again:")
print(cars)
print("\nHere is the sorted list again, but reversed:")
print(sorted(cars, reverse=True))

# You can permanently reverse the order of a list using the reverse method
print(f"\n{cars}")
cars.reverse()
print(cars)

# To find the length of a list use the len function
print(len(cars))