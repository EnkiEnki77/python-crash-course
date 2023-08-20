# You can work with a specific group of items in a list, known as a slice. The syntax is to specify the starting index
# of the slice, and the ending index sepereated by a :. The last element included in the slice is the one right before 
# the ending index, just like with the range function.
players = ["charles", "enki", "bat", "bob", "janette"]

print(players[1:4])

# If you dont include a starting index the slice begins at the start of the list
print(players[:4])

# Without an ending index the slice goes all the way to the end of the list.
print(players[1:])

# You can use a negative number to indicate indexes starting from the end of the list.
print(players[-2:])

# You can skip items in a list when creating a slice by passing in another : and a third number which indicates the skip
# amount
print(players[1:4:2])

# You can loop through a slice
for player in players[:3]:
    print(f"Yes {player}")

      

