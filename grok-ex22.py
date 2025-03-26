# Write a function has_space that takes a string as input
# returns True if it contains a space, False otherwise.
# Use a loop to check each character.
# Example:
# has_space("hello world") → True

# has_space("hi") → False

# has_space(" ") → True

def has_space(word):
    for chars in word:
        if chars == " ":
            return True
    return False # this checks only after everything else
