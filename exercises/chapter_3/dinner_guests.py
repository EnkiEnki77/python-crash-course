guests = ["mitch", "gpa", "vessel"]

cant_make_it = guests.pop(0)

guests.insert(0, "johnny")

guests.insert(0, "deadpool")

guests.insert(1, "john")

# You can't insert an item into the end of a list, you have to use append
guests.append("bat")

print(f"there will be {len(guests)} guests.")