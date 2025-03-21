# Write a function called repeat_last
#  that takes a string as input and returns a new string
#  where the last character is repeated three times.
# Use a loop to build the result.
# Example:
# repeat_last("hello") → "ooo"

# repeat_last("cat") → "ttt"

# repeat_last("z") → "zzz"

def repeat_last(string):
    new_string = "" # start with an empty string
    last_char = string[-1] # this isolates the last char
    for i in range(3): # loop 3 times
        new_string += last_char # adds last char
    return new_string
