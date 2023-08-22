# You can prompt for as much input as you need on each pass through of a while loop.
# You can then store that data in a dictionary to associate input with a specific user.

responses = {}

# Remember you can use a flag to end a while loop if there are many different conditions. Or if you need the loop to run
# for an unspecified number of iterations.
polling_active = True

while polling_active:
    # You can request user input in the loop
    name = input("\nWhat is your name?: ")
    response = input("Which mountain would you like to climb someday?: ")

    # Then store the data in a dictionarie, asking for the users name allows you to store other input under a name key.
    responses[name] = response

    # You can use a conditional to end the loop based on user input
    repeat = input("Would like to let anyone else take the poll (yes/no) ")
    if repeat == "no":
        polling_active = False

print("---Polling results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")

