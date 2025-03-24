# Write a function starts_with that takes a string and a character (as a single-letter string, e.g., "a") as input,
# and returns True if the string starts with that character, and False otherwise.
# Use a loop to check the first character (don’t use direct indexing like string[0]—just for practice!).
# Example:
# starts_with("hello", "h") → True

# starts_with("cat", "d") → False

# starts_with("a", "a") → True

def starts_with(word, char):
    for chars in word:
        if chars == char:# if 1st char matches
            return True
        return False # first char doesn't match, stop
    return False # empty string case
