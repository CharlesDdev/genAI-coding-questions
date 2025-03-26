# Write a function is_short that takes a string
# and returns True if it has fewer than 4 characters, False otherwise.
# Use a loop to count (no len()).
# Example:
# is_short("cat") → True (3 chars)

# is_short("hello") → False (5 chars)

# is_short("") → True (0 chars)

def is_short(word):
    char_count = 0
    for char in word:
        char_count += 1
    if char_count < 4:
        return True
    return False
