# Creating dictionaries
user = {
    "username": "admin",
    "status": "active",
    "age": 30
}

print("User dictionary:", user)


# Accessing dictionary values
print("\nUsername:", user["username"])
print("Status:", user["status"])


# Adding new key-value pairs
user["role"] = "tester"

print("\nAfter adding role:", user)


# Updating values
user["status"] = "inactive"

print("\nAfter updating status:", user)


# Removing values
del user["age"]

print("\nAfter deleting age:", user)


# Checking if a key exists
if "username" in user:
    print("\nusername key exists")


# Looping through dictionary keys
print("\nDictionary keys:")

for key in user:
    print(key)


# Looping through dictionary values
print("\nDictionary values:")

for value in user.values():
    print(value)


# Looping through key-value pairs
print("\nDictionary items:")

for key, value in user.items():
    print(f"{key}: {value}")


# QA-style API response example
response = {
    "status": 200,
    "message": "Success",
    "user_id": 15
}

print("\nAPI response:", response)

if response["status"] == 200:
    print("Request successful")


# QA-style request payload example
payload = {
    "username": "admin",
    "password": "Secret123"
}

print("\nRequest payload:", payload)