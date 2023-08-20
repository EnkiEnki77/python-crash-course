# Python has a method very similar to removeprefix, but instead removing characters from the start of a string. It 
# removes them from the end.
# One use case is to remove file names
file_name = "file.py"
print(file_name)
print(file_name.removesuffix(".py"))

# With removeprefix, the string has to include the argument, and the first character of the argument has to be equal to 
# the first character of the string
# With removesuffix, the string has to include the argument, and the last character of the argument has to be equal to 
# the last character of the string  