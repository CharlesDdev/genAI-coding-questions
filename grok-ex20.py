# Write a function is_all_caps
# that takes a string as input
# and returns True if all letters in the string are uppercase,
# and False if any are lowercase.
# Use a loop to check each character.
# (Ignore non-letters like spaces or numbers.)
# Example:
# is_all_caps("HELLO") → True

# is_all_caps("Hello") → False

# is_all_caps("HI THERE") → True

def is_all_caps(word):
    for letters in word:
        if letter.isalpya() and not letters.isupper(): # if its a letter and not uppercase
            return False
        else
    return True #all letters passed the uppercase test
