# ==========================================================
# Basic for loop with range()
# ==========================================================

print("Using range(5):")

for i in range(5):
    print(i)


# ==========================================================
# Repeat actions multiple times
# ==========================================================

print("\nRunning test iterations:")

for i in range(3):
    print(f"Running test iteration {i}")


# ==========================================================
# range(start, stop)
# ==========================================================

print("\nrange(2, 6):")

for i in range(2, 6):
    print(i)


# ==========================================================
# range(start, stop, step)
# ==========================================================

print("\nrange(0, 10, 2):")

for i in range(0, 10, 2):
    print(i)


# ==========================================================
# Looping through a list with indexes
# ==========================================================

users_list = ["admin", "guest", "tester"]

print("\nLooping through list with indexes:")

for i in range(len(users_list)):
    print(f"User at index {i}: value at that index is {users_list[i]}")


# ==========================================================
# Looping through a tuple with indexes
# ==========================================================

users_tuple = ("admin", "guest", "tester")

print("\nLooping through tuple with indexes:")

for i in range(len(users_tuple)):
    print(f"User at index {i}: value at that index is {users_tuple[i]}")


# ==========================================================
# QA-style example with status codes
# ==========================================================

status_codes = [200, 201, 400, 500]

print("\nChecking status codes:")

for i in range(len(status_codes)):
    print(f"Status code at index {i}: {status_codes[i]}")


# ==========================================================
# QA-style example with expected values
# ==========================================================

expected_values = ("Success", "Completed", "Approved")

print("\nExpected values:")

for i in range(len(expected_values)):
    print(f"Expected value at index {i}: {expected_values[i]}")