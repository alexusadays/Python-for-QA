# this is a comment, code will ignore it

age = 30          # variable 'age' refers to the value 30 (an int)
name = "Alex"     # variable 'name' refers to a string

print("Age:", age)
print("Name:", name)

# Python is dynamically typed: the same name can later refer to a different type
age = "thirty"    # now 'age' refers to a string, not an int
print("Age after change:", age)

# Recommended style (PEP 8):
# https://peps.python.org/pep-0008/

# Valid names:
response_time_ms = 200      # descriptive snake_case name
MAX_RETRIES = 3             # constants in ALL_CAPS

# Invalid names (shown as comments only, they would cause syntax errors):
# 1user = "bad"             # cannot start with a digit
# test result = "bad"       # spaces are not allowed
# class = "bad"             # 'class' is a reserved keyword