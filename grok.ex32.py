# Write a function has_two_vowels that takes a string
# and returns True if it contains at least two vowels (a, e, i, o, u), False otherwise.
# Use a loop to check each character.
# Example:
# has_two_vowels("hello") → True (e, o)

# has_two_vowels("cat") → False (a only)

# has_two_vowels("audio") → True (a, u, i)

def has_two_vowels(word):
    how_many_vowels = 0
    for char in word:
        if char in "aeiou":
            how_many_vowels += 1
        if how_many_vowels >= 2:
            return True
