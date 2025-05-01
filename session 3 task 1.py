contacts = {
    "Omar": "123-456-7890",
    "Ahmed": "987-654-3210",
    "Ali": "555-123-4567"
}

print("contact names:")
for name in contacts:
    print(name)

name_lookup = input("enter a name to search for: ")
if name_lookup in contacts:
    print(f"{name_lookup}'s phone number is {contacts[name_lookup]}")
else:
    print(f"{name_lookup} name not found.")