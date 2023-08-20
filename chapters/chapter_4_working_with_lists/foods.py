
# You can create a copy of a list by using the slice operator with no arguments
fav_foods = ["Pizza", "Ice cream", "Pad thai"]
friend_foods = fav_foods[:]

print(fav_foods)
print(friend_foods)

# Copying a list makes the two variables completely seperate lists. This would not be the case if we had just
# assigned fav_foods to friend_foods, the variables would then just be pointing to the same list in memory.

