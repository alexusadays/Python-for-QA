# int – whole numbers
status_code = 200
print(type(status_code))

# float – decimal numbers
price_usd = 19.99
print(type(price_usd))

# bool – True / False
is_success = True
has_error = False
print(type(is_success))

# str – text
message = "Login successful"
print(type(message))

# None – “no value yet”
response_body = None
print(type(response_body))

# ---- Preview of collections ----
# list – ordered collection (mutable)
status_codes = [200, 201, 400, 500]

# tuple – ordered collection (immutable)
credentials = ("test.user@example.com", "SuperSecret123")

# dict – key/value mapping, great for JSON-like data
user = {
    "email": "test.user@example.com",
    "role": "admin",
    "active": True,
}

# set – unique values
unique_statuses = {200, 201, 400, 400}  # 400 will be stored once

print("Status codes list:", status_codes)
print("Credentials tuple:", credentials)
print("User dict:", user)
print("Unique statuses:", unique_statuses)