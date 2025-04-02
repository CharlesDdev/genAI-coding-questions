# Write a function count_a_from_user that:
# Asks the user to input a word (use input()).

# Counts how many "a"s are in it using a loop.

# Returns the count.

# Example:
# User types "banana" → 3

# User types "hi" → 0

# User types "apple" → 1

def count_a_from_user():
    user_input = input("Enter your word to see how many a's there are in your word: ")
    how_many_a = 0
    for char in user_input:
        if char == "a":
            how_many_a += 1
    return how_many_a
