# Write a function middle_char that takes a string
# and returns the middle character.
# If the string has an even length, return the first of the two middle characters.
# Use a loop to count the length (no len()), then find the middle.

# Example:
# middle_char("hello") → "l" (5 chars, middle is 3rd)

# middle_char("python") → "t" (6 chars, middle is 3rd/4th, take 3rd)

# middle_char("cat") → "a" (3 chars, middle is 2nd)

def middle_char(words):
    string_length = 0
    for char in words:
        string_length += 1 # counts length
    if string_length == 0: # edge case
        return ""
    if string_length % 2 == 0:
        middle_pos = (string_length // 2) - 1 # first of two middles
    else:
        middle_pos = string_length // 2 # exact middle
    pos = 0
    for char in words:
        if pos == middle_pos:
            return char
        pos += 1
    return ""
