guests = ["mitch", "gpa", "vessel"]

cant_make_it = guests.pop(0)

guests.insert(0, "johnny")

print(f"Hey {guests[0].title()}, I'd like to invite you to my party.")
print(f"Hey {guests[1].title()}, I'd like to invite you to my party.")
print(f"Hey {guests[2].title()}, I'd like to invite you to my party.") 
print(f"{cant_make_it.title()} can't make it to the party.")