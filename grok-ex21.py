# Write a function count_words that takes a string as input
# and returns the number of words in it.
# Assume words are separated by a single space, and use a loop to count them.
# (Hint: Count spaces and adjust.)
# Example:
# count_words("hello world") → 2

# count_words("I am here") → 3

# count_words("hi") → 1

def count_words(string):
    number_of_words = 1  # Start with 1 for the first word
    for char in string:
        if char == " ":  # Count spaces to separate words
            number_of_words += 1
    return number_of_words
