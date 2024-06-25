phones = {"Alice":5551212, "Jill":5556789, "Bob":5559999}

finding_jill = phones["Jill"] 
print(finding_jill) # Prints phone 

try:
    finding_xav = phones["Xavier"] 
    print(finding_xav) # Returns Key Error as Xavier is not in key of phones dictionary
except KeyError as e:
    print("Key Error:", e)

print(phones.get("Alice")) # returns value of Alice
print(phones.get("Mike")) # returns None if no value provided

print(phones.get("Alice", "Nah")) # returns value of Alice
print(phones.get("Timmy", "Nah")) # returns nah since Timmy wasn't found

phones["Xavier"] = 5556666 # Adding new key-value pair to dictionary
print(phones)

phones["Alice"] = 5554263 # Updating phone of Alice
print(phones)

del phones["Alice"] # Removing the Alice key-value pair
print("Deletion:", phones) # Alice won't be here

# Looping through dictionary
for k in phones:
    print(k, phones.get(k)) # prints just the keys