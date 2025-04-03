# Create a new list long_names with names longer than 3 letters.

# Print long_names.

# Expected output: ["alice"]

names = ["bob", "alice", "eve"]
long_names = []
for i in range(len(names)):
    if len(names[i]) > 3: # check each length
        long_names.append(names[i]) # append the name
print(long_names)
