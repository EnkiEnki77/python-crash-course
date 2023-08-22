# The * operator assigns a tuple to a param of an arbitrary length of values, the ** operator assigns a dictionary of 
# arbitrary length of key-value arguments. 
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything about a user"""
    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info

user_profile = build_profile("enki", "layman", location="Roanoke", sport="climbing")

print(user_profile)

# You might see **kwargs which is used to collect non specific keyword arguments.

