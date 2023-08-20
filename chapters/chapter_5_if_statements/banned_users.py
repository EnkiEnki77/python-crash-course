# You can check if a value exists in a list using the in operator.
requested_toppings = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_toppings)
print("pizza" in requested_toppings)

# You can use the not keyword along with in to check if  a value is not in a list or not
banned_users = ["bat", "enki", "james"]
user = "enki"

if user not in banned_users:
    print(f"{user.title()}, you can post a response.")
else:
    print(f"{user.title()}, you are banned.")

# Use boolean expressions to track the state of your program
game_active = True
can_edit = False