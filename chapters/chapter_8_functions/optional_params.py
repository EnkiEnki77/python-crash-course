# You can use default params to make a param optional, just give an empty string as the default
def get_formatted_name(fname, lname, mname = ""):
    full_name = f"{fname} {mname} {lname}"
    return full_name.title()

musician = get_formatted_name("enki", mname="lee", lname="layman")
photographer = get_formatted_name("bat", lname="vest")

print(musician)
print(photographer)


# If you want utilize a list in a function, but dont want to modify the original you can pass the function a copy.
unprinted_designs = ["design1", "design2", "design3"]
printed_designs = []

def print_designs(list):
    while list:
        design = list.pop()
        printed_designs.append(design)

    return printed_designs

print(f"Unprinted designs: {unprinted_designs}")
print(f"Printed designs: {print_designs(unprinted_designs[:])}")
print(f"Unprinted designs for records: {unprinted_designs}")
