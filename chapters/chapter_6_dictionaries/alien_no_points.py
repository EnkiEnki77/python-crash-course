alien_0 = {"x_position": 0, "y_position": 0, "speed": "slow"}

# When attempting to access a key if the key doesnt exist youll get a traceback error. So instead use the get method
# Its first argument specifies the key youd like to retrieve, the second argument specifies a value to return if it 
# doesnt exist. If you leave out the second argument, python will return the value None, which means no value exists.
point_value = alien_0.get("points", "No point value assigned")
print(point_value)

