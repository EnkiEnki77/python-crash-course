# The input function takes a a prompt string as an argument to tell the user what kind of input we're looking for, it then 
# Halts the running of the rest of the code until the user hits enter. It then returns whatever the user input, to be stored
# in a variable. You should define a seperate prompt variable that is passed into input to make things cleaner.
# prompt = "Tell us your name: "
# message = input(prompt)

# print(f"Hi, {message}")

# The input function only returns strings, so if you need to interpret an input as a number for computations use the int
# function. This parses strings int integers.
prompt = "What is your age?: "
age = int(input(prompt))

if age >= 18:
    print("You can do drugs, you're 18.")
else:
    print("You can't do drugs, you're still a kid.")