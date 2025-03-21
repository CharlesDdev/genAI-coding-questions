# Write a function called count_chars
# that takes a string as input
# and returns the total number of characters in it.
# Use a loop to count each character (don’t use len()—just for practice!).
# Example:
# count_chars("dog") → 3

# count_chars("hi") → 2

# count_chars("") → 0

# Take a swing at it, and let me know your solution!
# I’ll guide you through the next question after.

def count_char(string):
    tot_char = 0
    for char in string:
        tot_char += 1
    return tot_char
