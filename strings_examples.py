#Python Strings
# A string is text wrapped in quotes (single or double)
message_1 = "Login successful"
message_2 = 'Login successful'
url = "https://alexusadays.com"

print("Message 1:", message_1)
print("Message 2:", message_2)
print("URL:", url)

# Strings are SEQUENCES of characters (each char has an index)
# Strings are immutable: you can’t modify characters in place
# text[0] = "p"  # TypeError
text = "Python"
# P  y  t  h  o  n
# 0  1  2  3  4  5
print("text:", text)


# Working with Characters in a String
# Access characters by index

first = text[0]     # 'P'
last = text[-1]     # 'n'
print("first:", first)
print("last:", last)

# Get the length of a string
length = len(text)  # 6
print("length:", length)

# Slicing (substrings) — end index is NOT included
print("text[0:3]:", text[0:3])  # 'Pyt'
print("text[3:]:", text[3:])    # 'hon'

# Building Messages for Test Logs
# print() can take multiple arguments and separates them with a space

status = 200
print("Status code:", status)   # Status code: 200

# For logs and assertions, f-strings are cleaner
method = "GET"
endpoint = "/login"
msg = f"Sending {method} request to {endpoint}"
print(msg)  # Sending GET request to /login

# Useful String Operations in Tests
# ==========================================================

# Change case for case-insensitive checks
message = "ERROR: Invalid password"
message_lower = message.lower()
print("message_lower:", message_lower)

# Strip whitespace/newlines
# \n → newline escape sequence
raw_value = "   ERROR: Invalid password   \n"
print("raw_value:", raw_value)
cleaned = raw_value.strip()
print("cleaned:", cleaned)

# Split into parts (limit to 1 split)
header = "Content-Type: application/json"
name, value = header.split(": ", 1)
print("header name:", name)
print("header value:", value)

# Replace text (normalize multi-line logs)
multi_line = "ERROR:\nSomething failed\nCheck  \" config"
print("multi_line:", multi_line)
single_line = multi_line.replace("\n", " ")
print("single_line:", single_line)
