# Write a function ends_with_e that takes a string and
# returns True if it ends with "e", False otherwise.
# Use a loop to find the last character (no [-1]).
# Example:
# ends_with_e("apple") → True

# ends_with_e("cat") → False

#ends_with_e("e") → True

def ends_with_e(word):
    last_char = ""
    for char in word:
        last_char = char
    if last_char == "e":
            return True
    return False
