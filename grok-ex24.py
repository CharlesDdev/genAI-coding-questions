#Write a function is_long that takes a string as input
# and returns True if it has more than 5 characters, False otherwise.
# Use a loop to count the characters (don’t use len()—just for practice!).
# Example:
# is_long("hello") → False (5 chars)

# is_long("hello there") → True (11 chars)

# is_long("hi") → False (2 chars)

def is_long(word):
    char_count = 0
    for char in word:
        char_count += 1
    if char_count > 5:
        return True
    else:
        return False
