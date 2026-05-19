# ==========================================================
# Creating sets
# ==========================================================
emails = {"admin@test.com", "guest@test.com", "admin@test.com"}
print("Emails set:", emails)
# Duplicate values are removed automatically

# ==========================================================
# Sets contain unique values
# ==========================================================
numbers = {1, 2, 2, 3, 3, 3}
print("\nNumbers set:", numbers)

# ==========================================================
# Adding values to a set
# ==========================================================
status_codes = {200, 201, 400}
print("\nOriginal status codes:", status_codes)
status_codes.add(500)
print("After adding 500:", status_codes)

# ==========================================================
# Removing values from a set
# ==========================================================
status_codes.remove(201)
print("After removing 201:", status_codes)

# ==========================================================
# Checking if a value exists
# ==========================================================
if 500 in status_codes:
    print("\n500 status code found")


# ==========================================================
# Sets are not indexed
# ==========================================================
users = {"admin", "guest", "tester"}
print("\nUsers set:", users)
# This would fail because sets are not indexed
# print(users[0])

# ==========================================================
# QA-style example — detecting duplicates
# ==========================================================
usernames = ["admin", "guest", "admin", "tester"]
print("\nOriginal usernames list:", usernames)
unique_usernames = set(usernames)
print("Unique usernames:", unique_usernames)
if len(usernames) != len(unique_usernames):
    print("Duplicate usernames detected")

# ==========================================================
# QA-style example — comparing values
# ==========================================================
expected_roles = {"admin", "guest", "tester"}
actual_roles = {"guest", "tester", "admin"}
print("\nExpected roles:", expected_roles)
print("Actual roles:", actual_roles)
if expected_roles == actual_roles:
    print("Roles match")

# ==========================================================
# Converting between list and set
# ==========================================================
numbers_list = [1, 2, 2, 3, 3, 4]
print("\nOriginal list:", numbers_list)

unique_numbers = set(numbers_list)
print("Converted to set:", unique_numbers)

back_to_list = list(unique_numbers)
print("Converted back to list:", back_to_list)