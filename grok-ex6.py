# Question 6 (Loop Review)

# temps = [32, 45, 28, 39]

# Find the index of the first temp below 30,
# print it (or -1 if none).

# Expected output: 2

# Hint: Use a variable like found = -1, check < 30,
# and break when you find it.

temps = [32, 45, 28, 39]

below_30 = -1

for i in range(len(temps)):
    if temps[i] < 30:
        below_30 = i # stores the index not the value
        break
print(below_30)
