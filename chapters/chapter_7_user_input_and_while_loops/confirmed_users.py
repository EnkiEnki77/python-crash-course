# You should use a while loop when modifying lists

unconfirmed_users = ["alice", "brian", "candice"]
confirmed_users = []

# Empty arrays are falsey, so the ending condition will be when the array is empty.
while unconfirmed_users:
    # Pop removes the last element of an array, and returns it to be stored in a variable for use later.
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for user in confirmed_users:
    print(user.title())