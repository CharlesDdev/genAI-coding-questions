# Write a function ends_with_y that takes a string
# and returns True if it ends with "y", False otherwise.
# Use a loop (no [-1]).
# Example:
# ends_with_y("happy") → True

# ends_with_y("cat") → False

# ends_with_y("y") → True

def ends_with_y(word):
    last_char = ""
    for char in word:
        last_char = char # keeps the last one
    if last_char == "y":
        return True
    return False
