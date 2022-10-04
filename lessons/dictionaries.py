"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Assess a value by its key -- "lookup"
print(f"UNC has {schools['UNC']} students")
print(f"Duke has {schools['Duke']} students")
print(f"NCSU has {schools['NCSU']} students")