# Defining functions is similar to javascript, except you use the def keyword instead of function
def greet_user(user):
    """This is a doc string, used to document functions. Define what the function does."""
    print(f"Hey, {user}")

greet_user("enki")

def describe_pet(animal_type, name="default snek"):
    """Describe a pet"""
    print(f"{animal_type}: {name}")

# You can use key value arguments to specifiy exactly what param to assign an argument, so you dont have to worry about
# the order youre passing arguments.
describe_pet(name="hank", animal_type="snek")

# You can define a default value for a param that is used if an argument isnt passed for it. You need to list default
# params after params without defaults when defining a function.
describe_pet(animal_type="snek")

