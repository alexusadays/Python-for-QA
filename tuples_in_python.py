# Creating a tuple
credentials = ("admin", "SuperSecret123")
print("Credentials:", credentials)

# Accessing values by index
print("Username:", credentials[0])
print("Password:", credentials[1])

# Tuple values often have meaning by position
# In this tuple, the first value represents the username and the second value represents the account status.
# The position itself has meaning.
user = ("admin", "active")
print("User tuple:", user)

# Tuples support slicing just like lists
numbers = (10, 20, 30, 40)

print("First two values:", numbers[0:2])
print("Last two values:", numbers[-2:])

# Attempting to modify a tuple will fail
try:
    user[0] = "hacker"
except TypeError as e:
    print("Cannot modify tuple:", e)

# Overwriting tuple (creating a new tuple)
user = ("admin", "inactive")
print("Updated user tuple:", user)

# The original tuple was not modified.
# We created a completely new tuple
# and reassigned the variable.