guests = ["mitch", "gpa", "vessel"]

cant_make_it = guests.pop(0)

guests.insert(0, "johnny")

guests.insert(0, "deadpool")

guests.insert(1, "john")

# You can't insert an item into the end of a list, you have to use append
guests.append("bat")

print(f"{cant_make_it.title()} can't make it to the party. Although, we found a bigger table")

print(f"Hey {guests[0].title()}, I'd like to invite you to my party.")
print(f"Hey {guests[1].title()}, I'd like to invite you to my party.")
print(f"Hey {guests[2].title()}, I'd like to invite you to my party.") 

print(f"Hey {guests[3].title()}, I'd like to invite you to my party.")
print(f"Hey {guests[4].title()}, I'd like to invite you to my party.")
print(f"Hey {guests[5].title()}, I'd like to invite you to my party.") 