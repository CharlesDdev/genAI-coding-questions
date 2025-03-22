# Write a function called has_vowel
# that takes a string as input and returns True if it contains at least one vowel (a, e, i, o, u),
# and False otherwise.
# Use a loop to check each character.
# Example:
# has_vowel("cat") → True (has ‘a’)

# has_vowel("sky") → True (has ‘y’—but traditionally not a vowel, so focus on a, e, i, o, u)

# has_vowel("rhythm") → False (no standard vowels)

def has_vowels(string):
    vowels = "aeiou"
    for char in string:
        if char in vowels:
            return True
    return False
