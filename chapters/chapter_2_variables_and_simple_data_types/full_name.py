first_name = 'ada'
last_name = 'lovelace'
# This is a format string, it allows you to insert a variables value into a string. You must put the letter f before
# the opening quotation mark, and wrap the variables in curlies.
full_name = f"{first_name} {last_name}"
# Format strings are useful for composing complete messages with dynamic data.
print(f"Hello, my name is {full_name.title()}!")

# You can assign format strings to variables
greeting = f"Hello, {full_name.title()}"
print(greeting)


# RUN IN TERMINAL
# To add a tab to a string use \t
print("Python")
print("\tPython")


# RUN IN TERMINAL
# To add a new line to a string use \n
print("Languages: \nPython\nC\nJavascript")


# RUN IN TERMINAL
favorit_language = " Python "
# You can remove whitespace from a string with three different methods
# They are most often used to clean up user input
# They do not mutate the original string
# rstrip() removes whitespace from the right end of the string
print(favorit_language.rstrip())
# lstrip() removes whitespace from the left end of the string
print(favorit_language.lstrip())
# strip() removes whitespace from both ends of the string
print(favorit_language.strip())


# RUN IN TERMINAL
url = "https://enkienki.com"
# You can remove a prefix of a string, such as https:// on a url. 
# It only removes characters starting from the front of a string.
# The method does not mutate the original string, so you must save the return of the method in a new variable
short_url = url.removeprefix("https://")
print(short_url)

# When you see a url in the address bar, and the https:// part isnt showing, the browser is useing something like 
# removeprefix behind the scenes.




