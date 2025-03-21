# Write a function called first_half
# that takes a string as input
# and returns a new string containing only the first half of the original string.
# Use a loop to build the result, and for simplicity,
# if the string has an odd length, round down (e.g., for a 5-character string, take the first 2 characters).

def first_half(string):
    new_string = ""
    half_length = len(string) // 2 # gets half, round down
    for i in range((half_length)): # loops only half
        new_string += string[i] # adds each char
    return new_string
