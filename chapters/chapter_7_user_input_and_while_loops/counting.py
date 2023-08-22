# The for loop takes a collection of items, and executes a block of code for each item in the colelction. The while loop on
# the other hand executes while a condition continues to be true.

# You can write a while that only stops running if a user inputs a certain string.
# prompt = "Type something, and i'll repeat it back to you.\nType 'quit' to end the program"

# message = ""
# while message != "quit":
#     message = input(prompt)
#     print(message)

# For a program that should run only as long as many conditions are true you can use a single variable called a flag to
# indicate the program is active. Our flag will start as true, and our program stops running if any of the many conditions
# sets the flag to false. This makes it where the while loop only needs to keep track of one condition, the flag state.

prompt = "Type a number, and i'll tell you what that number raise to the power of 12 is."
prompt += "\nEnter 'quit' to end the program. "

# Give the message variable an empty string, so the while loop has an initial value to check.
# active = True
# while active:
#     message = input(prompt)

#     if(prompt == "quit"):
#         active = False
#     else: 
#         print(int(message)**12)

# You can use the break keyword to automatically stop and exit a while loop 
# prompt = "Please enter a city youve visited: "
# prompt += "\n(Enter quit when youre done)"

# # Will run forever unless a break statement is hit
# while True:
#     message = input(prompt)

#     if message == "quit":
#         break
#     else: 
#         print(message)

# The continue keyword allows you to start a loop over, you can use this restart a loop based on certain conditions.
# For example, if youre looping through a set of numbers, but want to print out only the odd ones, you can use continue
# whenever the current number is even

current_num = 1
print(current_num)

while current_num < 10:
    current_num += 1
    if current_num % 2 == 0:
        continue

    print(current_num)


# A for loop is effective for looping through a list or dictionarie, but you shouldnt modify a list in a for loop, because
# Python will have trouble keeping track of the items, use a while loop instead.

