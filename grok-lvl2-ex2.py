# Write a function called has_double that takes a string as input
# and returns True if it contains any letter that appears twice in a row (e.g., "aa" or "bb"),
# and False otherwise.
# Use a loop to check each pair of characters.
# Example:
# has_double("hello") → True (has “ll”)

# has_double("cat") → False (no doubles)

# has_double("book") → True (has “oo”)

def has_double(word):
    for i in range(len(word)-1): # stops one short
        if word[i] == word[i + 1]:# compare current index to next
            return True
    return False # no doubles found after checking all
